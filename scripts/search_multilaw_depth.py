"""Exhaustive search for a nonlinear multi-law depth separation.

The search enumerates all unordered three-law families on a three-state carrier
and every three-state intervention.  It looks for two systems using the same
intervention whose low-depth Law-Genesis summaries agree but whose next-depth
Law Genesis Costs differ.

This is a falsification/search utility, not a novelty claim.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from itertools import combinations_with_replacement, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from law_genesis.core import (
    apply_word,
    class_sizes,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    raw_disagreement_count,
)
from law_genesis.metrics import critical_seed_rank, fragility_spectrum_uniform


def transformations(n: int):
    yield from product(range(n), repeat=n)


def transformed(laws, intervention, depth: int):
    if depth == 0:
        return tuple(laws)
    interventions = {"N": intervention}
    word = "N" * depth
    return tuple(apply_word(law, interventions, word) for law in laws)


def one_seed_fragility_signature(laws):
    spectrum = fragility_spectrum_uniform(laws, max_order=1)
    return tuple(round(x, 12) for x in spectrum[1])


def depth_summary(laws, intervention, depth: int):
    current = transformed(laws, intervention, depth)
    partition = least_common_law_congruence(current)
    return {
        "gamma": round(law_genesis_cost_uniform(current), 12),
        "class_sizes": class_sizes(partition),
        "raw_disagreement_pairs": raw_disagreement_count(current),
        "beta": critical_seed_rank(current),
        "fragility_order1": one_seed_fragility_signature(current),
    }


def low_depth_key(laws, intervention):
    s0 = depth_summary(laws, intervention, 0)
    s1 = depth_summary(laws, intervention, 1)
    # Match all of these low-order observables at depths 0 and 1.
    return (
        s0["gamma"], s0["class_sizes"], s0["raw_disagreement_pairs"], s0["beta"], s0["fragility_order1"],
        s1["gamma"], s1["class_sizes"], s1["raw_disagreement_pairs"], s1["beta"], s1["fragility_order1"],
    )


def find_witness(n: int = 3):
    maps = list(transformations(n))
    families = list(combinations_with_replacement(maps, 3))
    examined = 0

    for intervention in maps:
        buckets = defaultdict(list)
        for laws in families:
            examined += 1
            key = low_depth_key(laws, intervention)
            s2 = depth_summary(laws, intervention, 2)
            # At separating depth also force equal raw disagreement magnitude.
            sep_key = s2["raw_disagreement_pairs"]
            bucket_key = (key, sep_key)
            for previous_laws, previous_s2 in buckets[bucket_key]:
                if previous_s2["gamma"] != s2["gamma"]:
                    return {
                        "state_count": n,
                        "three_law_families": len(families),
                        "interventions": len(maps),
                        "family_intervention_cases_examined": examined,
                        "intervention": list(intervention),
                        "system_A": [list(x) for x in previous_laws],
                        "system_B": [list(x) for x in laws],
                        "depth_0_A": depth_summary(previous_laws, intervention, 0),
                        "depth_0_B": depth_summary(laws, intervention, 0),
                        "depth_1_A": depth_summary(previous_laws, intervention, 1),
                        "depth_1_B": depth_summary(laws, intervention, 1),
                        "depth_2_A": previous_s2,
                        "depth_2_B": s2,
                    }
            buckets[bucket_key].append((laws, s2))
    return None


def main() -> None:
    witness = find_witness(3)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    path = out / "multilaw_depth_search_n3.json"
    payload = {
        "search": "all unordered three-law families on three states x all three-state interventions",
        "matching_constraints": [
            "same intervention",
            "same Gamma at depths 0 and 1",
            "same common-law class-size profiles at depths 0 and 1",
            "same raw disagreement counts at depths 0 and 1",
            "same critical seed rank beta at depths 0 and 1",
            "same complete one-seed fragility spectrum at depths 0 and 1",
            "same raw disagreement count at depth 2",
        ],
        "witness": witness,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if witness is None:
        print("NO_WITNESS_FOUND")
    else:
        print("WITNESS_FOUND")


if __name__ == "__main__":
    main()
