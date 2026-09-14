"""Core finite-system computations for Law Genesis.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

from collections import defaultdict
from math import log2
from typing import Iterable, Mapping, Sequence

Transformation = Sequence[int]
Pair = tuple[int, int]


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def _validate_transformations(laws: Sequence[Transformation]) -> int:
    if not laws:
        raise ValueError("at least one law is required")
    n = len(laws[0])
    if n == 0:
        raise ValueError("state space must be nonempty")
    for law in laws:
        if len(law) != n:
            raise ValueError("all transformations must have equal size")
        if any((y < 0 or y >= n) for y in law):
            raise ValueError("transformation output outside state space")
    return n


def disagreement_pairs(laws: Sequence[Transformation]) -> set[Pair]:
    """Return all unordered output disagreements among microscopic laws."""
    n = _validate_transformations(laws)
    pairs: set[Pair] = set()
    for x in range(n):
        outputs = {law[x] for law in laws}
        out = sorted(outputs)
        for i, a in enumerate(out):
            for b in out[i + 1 :]:
                pairs.add((a, b))
    return pairs


def partition_from_pairs(n: int, pairs: Iterable[Pair]) -> tuple[tuple[int, ...], ...]:
    uf = UnionFind(n)
    for a, b in pairs:
        uf.union(a, b)
    groups: dict[int, list[int]] = defaultdict(list)
    for x in range(n):
        groups[uf.find(x)].append(x)
    return tuple(sorted((tuple(v) for v in groups.values()), key=lambda c: (c[0], len(c))))


def _uf_from_partition(n: int, partition: Sequence[Sequence[int]]) -> UnionFind:
    uf = UnionFind(n)
    for block in partition:
        if not block:
            continue
        root = block[0]
        for x in block[1:]:
            uf.union(root, x)
    return uf


def least_common_law_congruence(laws: Sequence[Transformation]) -> tuple[tuple[int, ...], ...]:
    """Compute the least congruence that makes all laws induce one quotient law.

    Start with all raw microscopic disagreement pairs and repeatedly close under
    compatibility with each microscopic transformation until a fixed point is
    reached.
    """
    n = _validate_transformations(laws)
    uf = UnionFind(n)
    for a, b in disagreement_pairs(laws):
        uf.union(a, b)

    changed = True
    while changed:
        changed = False
        classes: dict[int, list[int]] = defaultdict(list)
        for x in range(n):
            classes[uf.find(x)].append(x)

        for block in list(classes.values()):
            for i, a in enumerate(block):
                for b in block[i + 1 :]:
                    for law in laws:
                        if uf.union(law[a], law[b]):
                            changed = True

    groups: dict[int, list[int]] = defaultdict(list)
    for x in range(n):
        groups[uf.find(x)].append(x)
    return tuple(sorted((tuple(v) for v in groups.values()), key=lambda c: (c[0], len(c))))


def entropy_loss_uniform(partition: Sequence[Sequence[int]], n: int | None = None) -> float:
    """H(X | quotient(X)) for a uniform finite state space."""
    if n is None:
        n = sum(len(block) for block in partition)
    if n <= 0:
        raise ValueError("n must be positive")
    total = 0.0
    for block in partition:
        k = len(block)
        if k:
            total += (k / n) * log2(k)
    return total


def law_genesis_cost_uniform(laws: Sequence[Transformation]) -> float:
    partition = least_common_law_congruence(laws)
    return entropy_loss_uniform(partition)


def compose(left: Transformation, right: Transformation) -> tuple[int, ...]:
    """Return left o right."""
    if len(left) != len(right):
        raise ValueError("transformations must have equal size")
    return tuple(left[right[x]] for x in range(len(left)))


def apply_word(law: Transformation, interventions: Mapping[str, Transformation], word: str) -> tuple[int, ...]:
    """Apply an intervention word left-to-right after a microscopic law.

    For word 'PQ', return Q o P o law.
    """
    result = tuple(law)
    for symbol in word:
        if symbol not in interventions:
            raise KeyError(f"unknown intervention symbol: {symbol}")
        result = compose(interventions[symbol], result)
    return result


def protocol_cost_uniform(
    laws: Sequence[Transformation],
    interventions: Mapping[str, Transformation],
    word: str,
) -> float:
    transformed = [apply_word(law, interventions, word) for law in laws]
    return law_genesis_cost_uniform(transformed)


def raw_disagreement_count(laws: Sequence[Transformation]) -> int:
    return len(disagreement_pairs(laws))


def class_sizes(partition: Sequence[Sequence[int]]) -> tuple[int, ...]:
    return tuple(sorted((len(block) for block in partition), reverse=True))


def seed_closure(
    laws: Sequence[Transformation],
    seed_pairs: Iterable[Pair],
) -> tuple[tuple[int, ...], ...]:
    """Least congruence compatible with all laws and containing seed pairs."""
    n = _validate_transformations(laws)
    uf = UnionFind(n)
    for a, b in seed_pairs:
        uf.union(a, b)
    changed = True
    while changed:
        changed = False
        classes: dict[int, list[int]] = defaultdict(list)
        for x in range(n):
            classes[uf.find(x)].append(x)
        for block in list(classes.values()):
            for i, a in enumerate(block):
                for b in block[i + 1 :]:
                    for law in laws:
                        if uf.union(law[a], law[b]):
                            changed = True
    groups: dict[int, list[int]] = defaultdict(list)
    for x in range(n):
        groups[uf.find(x)].append(x)
    return tuple(sorted((tuple(v) for v in groups.values()), key=lambda c: (c[0], len(c))))


def forced_abstraction_uniform(laws: Sequence[Transformation], seed_pairs: Iterable[Pair]) -> float:
    """Extra uniform entropy loss caused by law-compatible closure beyond seed merging."""
    n = _validate_transformations(laws)
    seed = list(seed_pairs)
    direct = partition_from_pairs(n, seed)
    closed = seed_closure(laws, seed)
    return entropy_loss_uniform(closed, n) - entropy_loss_uniform(direct, n)
