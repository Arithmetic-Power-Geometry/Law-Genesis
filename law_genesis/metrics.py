"""Derived finite-system metrics for Law Genesis.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

from itertools import combinations
from typing import Iterable, Mapping, Sequence

from .core import (
    Pair,
    Transformation,
    entropy_loss_uniform,
    partition_from_pairs,
    protocol_cost_uniform,
    seed_closure,
)


def all_unordered_pairs(n: int) -> tuple[Pair, ...]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return tuple(combinations(range(n), 2))


def is_universal_partition(partition: Sequence[Sequence[int]]) -> bool:
    return len(partition) == 1


def critical_seed_rank(laws: Sequence[Transformation]) -> int:
    """Minimum number of pair identifications whose congruence closure is universal.

    This exact implementation is intended for small finite systems.  It searches
    seed sets by increasing cardinality and therefore returns the true minimum.
    """
    if not laws:
        raise ValueError("at least one law is required")
    n = len(laws[0])
    if n <= 1:
        return 0
    pairs = all_unordered_pairs(n)
    for k in range(1, n):
        for seed in combinations(pairs, k):
            if is_universal_partition(seed_closure(laws, seed)):
                return k
    return n - 1


def seed_loss_uniform(n: int, seed_pairs: Iterable[Pair]) -> float:
    seed = tuple(seed_pairs)
    return entropy_loss_uniform(partition_from_pairs(n, seed), n)


def closure_loss_uniform(laws: Sequence[Transformation], seed_pairs: Iterable[Pair]) -> float:
    seed = tuple(seed_pairs)
    n = len(laws[0])
    return entropy_loss_uniform(seed_closure(laws, seed), n)


def fragility_spectrum_uniform(
    laws: Sequence[Transformation],
    max_order: int | None = None,
) -> dict[int, tuple[float, ...]]:
    """Exact loss spectrum over seed sets of each cardinality.

    Values are sorted and rounded only by the caller, never internally.  The
    routine is exponential and is deliberately restricted to small systems.
    """
    if not laws:
        raise ValueError("at least one law is required")
    n = len(laws[0])
    pairs = all_unordered_pairs(n)
    if max_order is None:
        max_order = n - 1
    max_order = min(max_order, len(pairs))
    out: dict[int, tuple[float, ...]] = {}
    for k in range(max_order + 1):
        values = []
        for seed in combinations(pairs, k):
            values.append(closure_loss_uniform(laws, seed))
        out[k] = tuple(sorted(values))
    return out


def interaction_uniform(
    laws: Sequence[Transformation],
    seed_a: Iterable[Pair],
    seed_b: Iterable[Pair],
) -> float:
    """Synergy of two seed interventions under forced abstraction.

    Sigma(A,B) = FA(A union B) - FA(A) - FA(B).
    """
    from .core import forced_abstraction_uniform

    a = tuple(seed_a)
    b = tuple(seed_b)
    union = tuple(sorted(set(a).union(b)))
    return (
        forced_abstraction_uniform(laws, union)
        - forced_abstraction_uniform(laws, a)
        - forced_abstraction_uniform(laws, b)
    )


def genesis_work_uniform(
    laws: Sequence[Transformation],
    interventions: Mapping[str, Transformation],
    word: str,
    include_initial: bool = False,
) -> float:
    """Sum protocol-conditioned Law Genesis Cost over prefixes.

    If include_initial is False, sum Gamma over nonempty prefixes.  If True,
    also include the pre-intervention cost Gamma(empty word).
    """
    total = protocol_cost_uniform(laws, interventions, "") if include_initial else 0.0
    for t in range(1, len(word) + 1):
        total += protocol_cost_uniform(laws, interventions, word[:t])
    return total


def protocol_profile_uniform(
    laws: Sequence[Transformation],
    interventions: Mapping[str, Transformation],
    word: str,
    include_initial: bool = True,
) -> tuple[float, ...]:
    """Return Gamma along successive prefixes of a protocol word."""
    values = []
    if include_initial:
        values.append(protocol_cost_uniform(laws, interventions, ""))
    for t in range(1, len(word) + 1):
        values.append(protocol_cost_uniform(laws, interventions, word[:t]))
    return tuple(values)
