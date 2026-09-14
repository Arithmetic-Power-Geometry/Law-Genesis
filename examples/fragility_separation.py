"""Finite family separating Law Genesis Cost from critical seed rank.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

from math import log2

from law_genesis.core import law_genesis_cost_uniform
from law_genesis.metrics import critical_seed_rank


def build_systems(n: int):
    if n < 2:
        raise ValueError("n must be at least 2")
    identity = tuple(range(n))
    cycle = tuple((x + 1) % n for x in range(n))
    constant = (0,) * n
    system_a = (cycle, constant)
    system_b = (identity, constant)
    return system_a, system_b


def evaluate(n: int) -> dict[str, float | int]:
    system_a, system_b = build_systems(n)
    gamma_a = law_genesis_cost_uniform(system_a)
    gamma_b = law_genesis_cost_uniform(system_b)
    beta_a = critical_seed_rank(system_a)
    beta_b = critical_seed_rank(system_b)
    return {
        "n": n,
        "gamma_a": gamma_a,
        "gamma_b": gamma_b,
        "expected_gamma": log2(n),
        "beta_a": beta_a,
        "beta_b": beta_b,
        "beta_ratio": beta_b / beta_a,
    }


if __name__ == "__main__":
    for n in range(2, 9):
        print(evaluate(n))
