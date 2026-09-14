"""Permutation-only intrinsic Law-Genesis depth witness.

The two systems use the same four-state carrier and the same permutation
intervention.  They match through depths 0, 1, and 2 on Gamma, common-law
class-size profile, raw disagreement count, critical seed rank, and the complete
one-seed fragility spectrum, but separate in Gamma at depth 3.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from law_genesis.core import (
    apply_word,
    class_sizes,
    disagreement_pairs,
    least_common_law_congruence,
    law_genesis_cost_uniform,
)
from law_genesis.metrics import critical_seed_rank, fragility_spectrum_uniform

P = (1, 2, 3, 0)
INTERVENTIONS = {"P": P}

SYSTEM_A = (
    (3, 2, 1, 3),
    (3, 0, 3, 3),
    (0, 2, 1, 1),
)

SYSTEM_B = (
    (2, 2, 3, 0),
    (0, 2, 3, 1),
    (1, 0, 3, 2),
)


def transformed(system, depth: int):
    return tuple(apply_word(law, INTERVENTIONS, "P" * depth) for law in system)


def diagnostics(system, depth: int) -> dict:
    laws = transformed(system, depth)
    part = least_common_law_congruence(laws)
    spectrum = fragility_spectrum_uniform(laws, max_order=1)[1]
    return {
        "depth": depth,
        "gamma_bits": law_genesis_cost_uniform(laws),
        "class_sizes": class_sizes(part),
        "raw_disagreement_count": len(disagreement_pairs(laws)),
        "raw_disagreement_relation": tuple(sorted(disagreement_pairs(laws))),
        "beta": critical_seed_rank(laws),
        "fragility_order1": tuple(round(x, 12) for x in spectrum),
    }


def summary(system):
    return [diagnostics(system, depth) for depth in range(4)]


if __name__ == "__main__":
    print("System A")
    for row in summary(SYSTEM_A):
        print(row)
    print("System B")
    for row in summary(SYSTEM_B):
        print(row)
