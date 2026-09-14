"""Nonlinear three-law depth witness used in the current theory development.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from law_genesis.core import (
    class_sizes,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    protocol_cost_uniform,
    raw_disagreement_count,
)

N = (0, 0, 1, 2, 3)

SYSTEM_A = (
    (3, 0, 1, 1, 4),
    (3, 4, 4, 1, 0),
    (3, 0, 2, 0, 2),
)

SYSTEM_B = (
    (1, 3, 0, 4, 2),
    (4, 3, 1, 0, 0),
    (2, 3, 0, 0, 4),
)

INTERVENTIONS = {"N": N}


def summary(system):
    rows = []
    for depth in range(3):
        word = "N" * depth
        transformed = system if depth == 0 else None
        cost = law_genesis_cost_uniform(system) if depth == 0 else protocol_cost_uniform(system, INTERVENTIONS, word)
        if depth == 0:
            laws = system
        else:
            from law_genesis.core import apply_word
            laws = tuple(apply_word(law, INTERVENTIONS, word) for law in system)
        partition = least_common_law_congruence(laws)
        rows.append(
            {
                "depth": depth,
                "word": word,
                "gamma_bits": cost,
                "class_sizes": class_sizes(partition),
                "raw_disagreement_pairs": raw_disagreement_count(laws),
            }
        )
    return rows


if __name__ == "__main__":
    print("System A")
    for row in summary(SYSTEM_A):
        print(row)
    print("System B")
    for row in summary(SYSTEM_B):
        print(row)
