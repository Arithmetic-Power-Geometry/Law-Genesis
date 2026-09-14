"""Arbitrary-delay lift of the nonlinear Law-Genesis depth witness.

This construction does not introduce a new local mechanism.  It is a delay-line
lift of the verified five-state nonlinear witness.  Its purpose is to establish
an exact scalable statement: Law-Genesis separation can be postponed to any
prescribed finite depth while the two systems share the same intervention and
match Gamma, common-law class profiles, and raw disagreement counts at every
earlier depth.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose

from examples.nonlinear_depth_witness import N as BASE_N, SYSTEM_A as BASE_A, SYSTEM_B as BASE_B
from law_genesis.core import (
    apply_word,
    class_sizes,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    raw_disagreement_count,
)

BASE_N_STATES = 5


def encode(x: int, layer: int, layers: int) -> int:
    return layer * BASE_N_STATES + x


def decode(state: int) -> tuple[int, int]:
    return state % BASE_N_STATES, state // BASE_N_STATES


@dataclass(frozen=True)
class DelayedPair:
    delay: int
    laws_a: tuple[tuple[int, ...], ...]
    laws_b: tuple[tuple[int, ...], ...]
    intervention: tuple[int, ...]

    @property
    def separating_depth(self) -> int:
        return self.delay + 2

    @property
    def interventions(self):
        return {"T": self.intervention}


def _lift_laws(base_system, delay: int):
    layers = delay + 1
    n = BASE_N_STATES * layers
    lifted = []
    for base_law in base_system:
        values = []
        for state in range(n):
            x, _layer = decode(state)
            values.append(encode(base_law[x], delay, layers))
        lifted.append(tuple(values))
    return tuple(lifted)


def _delay_intervention(delay: int):
    layers = delay + 1
    n = BASE_N_STATES * layers
    values = []
    for state in range(n):
        x, layer = decode(state)
        if layer > 0:
            values.append(encode(x, layer - 1, layers))
        else:
            values.append(encode(BASE_N[x], 0, layers))
    return tuple(values)


def build_delayed_pair(delay: int) -> DelayedPair:
    if delay < 0:
        raise ValueError("delay must be nonnegative")
    return DelayedPair(
        delay=delay,
        laws_a=_lift_laws(BASE_A, delay),
        laws_b=_lift_laws(BASE_B, delay),
        intervention=_delay_intervention(delay),
    )


def transformed(laws, pair: DelayedPair, depth: int):
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    word = "T" * depth
    return tuple(apply_word(law, pair.interventions, word) for law in laws)


def diagnostics(pair: DelayedPair, system: str, depth: int) -> dict:
    laws = pair.laws_a if system == "A" else pair.laws_b
    current = transformed(laws, pair, depth)
    partition = least_common_law_congruence(current)
    return {
        "system": system,
        "delay": pair.delay,
        "depth": depth,
        "gamma_bits": law_genesis_cost_uniform(current),
        "class_sizes": class_sizes(partition),
        "raw_disagreement_pairs": raw_disagreement_count(current),
    }


def verify_depth_family(delay: int, tol: float = 1e-12) -> dict:
    """Verify the exact delayed-separation pattern for one delay value.

    The base witness matches at base depths 0 and 1 and separates at base depth
    2.  The lift inserts ``delay`` neutral layers before those base dynamics are
    reached.  Thus the first separation occurs at depth ``delay + 2``.
    """
    pair = build_delayed_pair(delay)
    sep = pair.separating_depth
    rows_a = [diagnostics(pair, "A", t) for t in range(sep + 1)]
    rows_b = [diagnostics(pair, "B", t) for t in range(sep + 1)]

    prior_match = True
    for a, b in zip(rows_a[:-1], rows_b[:-1]):
        prior_match &= isclose(a["gamma_bits"], b["gamma_bits"], rel_tol=tol, abs_tol=tol)
        prior_match &= a["class_sizes"] == b["class_sizes"]
        prior_match &= a["raw_disagreement_pairs"] == b["raw_disagreement_pairs"]

    last_a, last_b = rows_a[-1], rows_b[-1]
    separates = not isclose(last_a["gamma_bits"], last_b["gamma_bits"], rel_tol=tol, abs_tol=tol)

    return {
        "delay": delay,
        "state_count": BASE_N_STATES * (delay + 1),
        "separating_depth": sep,
        "all_prior_observables_match": bool(prior_match),
        "separates_in_gamma": bool(separates),
        "gamma_a_at_separation": last_a["gamma_bits"],
        "gamma_b_at_separation": last_b["gamma_bits"],
        "class_sizes_a_at_separation": last_a["class_sizes"],
        "class_sizes_b_at_separation": last_b["class_sizes"],
        "rows_a": rows_a,
        "rows_b": rows_b,
    }


if __name__ == "__main__":
    for delay in range(6):
        print(verify_depth_family(delay))
