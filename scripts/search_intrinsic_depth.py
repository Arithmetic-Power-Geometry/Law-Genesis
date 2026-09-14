"""Deterministic search for clock-free nonlinear Law-Genesis depth separation.

This search deliberately excludes the explicit delay-layer lift.  It restricts the
shared intervention to a permutation of a four-state carrier, so there are no
transient countdown layers.  Candidate pairs must match cheap Law-Genesis
observables through depth 2 and separate in Gamma at depth 3.  Stronger
fragility checks are then applied only to candidate collisions.

A positive result is a finite computational witness, not a novelty proof.  A
negative result is only a negative result for the stated deterministic search
budget and intervention class.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

import json
import random
from collections import defaultdict
from itertools import permutations
from pathlib import Path

from law_genesis.core import (
    apply_word,
    class_sizes,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    raw_disagreement_count,
)
from law_genesis.metrics import critical_seed_rank, fragility_spectrum_uniform

N = 4
LAW_COUNT = 3
SAMPLES_PER_INTERVENTION = 2500
RNG_SEED = 20260914


def random_law(rng: random.Random) -> tuple[int, ...]:
    return tuple(rng.randrange(N) for _ in range(N))


def transformed(laws, intervention, depth: int):
    interventions = {"P": intervention}
    word = "P" * depth
    return tuple(apply_word(law, interventions, word) for law in laws)


def cheap_signature(laws, intervention, max_depth: int = 2):
    rows = []
    for depth in range(max_depth + 1):
        cur = transformed(laws, intervention, depth)
        part = least_common_law_congruence(cur)
        rows.append(
            (
                round(law_genesis_cost_uniform(cur), 12),
                class_sizes(part),
                raw_disagreement_count(cur),
            )
        )
    return tuple(rows)


def strong_signature(laws, intervention, max_depth: int = 2):
    rows = []
    for depth in range(max_depth + 1):
        cur = transformed(laws, intervention, depth)
        one = tuple(round(x, 12) for x in fragility_spectrum_uniform(cur, max_order=1)[1])
        rows.append((critical_seed_rank(cur), one))
    return tuple(rows)


def gamma_at(laws, intervention, depth: int) -> float:
    return law_genesis_cost_uniform(transformed(laws, intervention, depth))


def search() -> dict:
    rng = random.Random(RNG_SEED)
    tested = 0
    cheap_collisions = 0
    strong_collisions = 0

    for intervention in permutations(range(N)):
        buckets: dict[tuple, list[tuple[tuple[int, ...], ...]]] = defaultdict(list)
        for _ in range(SAMPLES_PER_INTERVENTION):
            laws = tuple(random_law(rng) for _ in range(LAW_COUNT))
            key = cheap_signature(laws, intervention)
            bucket = buckets[key]
            tested += 1

            if bucket:
                cheap_collisions += 1
                sig = strong_signature(laws, intervention)
                g3 = round(gamma_at(laws, intervention, 3), 12)
                for other in bucket[:8]:
                    if strong_signature(other, intervention) != sig:
                        continue
                    strong_collisions += 1
                    other_g3 = round(gamma_at(other, intervention, 3), 12)
                    if other_g3 != g3:
                        return {
                            "status": "WITNESS_FOUND",
                            "carrier_size": N,
                            "law_count": LAW_COUNT,
                            "intervention_class": "permutations only; no transient delay layers",
                            "intervention": list(intervention),
                            "system_a": [list(x) for x in other],
                            "system_b": [list(x) for x in laws],
                            "matched_depths": [0, 1, 2],
                            "separating_depth": 3,
                            "cheap_signature": key,
                            "strong_signature": sig,
                            "gamma_a_depth3": other_g3,
                            "gamma_b_depth3": g3,
                            "tested_random_systems": tested,
                            "cheap_collisions": cheap_collisions,
                            "strong_collisions": strong_collisions,
                            "seed": RNG_SEED,
                        }
            if len(bucket) < 12:
                bucket.append(laws)

    return {
        "status": "NO_WITNESS_FOUND",
        "carrier_size": N,
        "law_count": LAW_COUNT,
        "intervention_class": "all 24 permutations of four states; no transient delay layers",
        "samples_per_intervention": SAMPLES_PER_INTERVENTION,
        "tested_random_systems": tested,
        "cheap_collisions": cheap_collisions,
        "strong_collisions": strong_collisions,
        "matched_depths_required": [0, 1, 2],
        "target_separating_depth": 3,
        "seed": RNG_SEED,
        "scope_note": "Negative only for this deterministic sampled search domain; not a theorem of impossibility.",
    }


def main() -> None:
    result = search()
    out = Path("results")
    out.mkdir(exist_ok=True)
    path = out / "intrinsic_depth_search.json"
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
