"""Exhaustive enumeration of tiny deterministic Law-Genesis systems.

The search treats a two-law microscopic family {f,g} as unordered, including
f=g.  For each family it computes Law Genesis Cost and exact critical seed rank
and then groups systems by the pair (Gamma, beta).

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import product
from pathlib import Path

from law_genesis.core import law_genesis_cost_uniform
from law_genesis.metrics import critical_seed_rank


def transformations(n: int):
    yield from product(range(n), repeat=n)


def unordered_family_count(n: int) -> int:
    m = n**n
    return m * (m + 1) // 2


def enumerate_two_law_systems(n: int = 3):
    if n < 1:
        raise ValueError("n must be positive")
    maps = list(transformations(n))
    counts: Counter[tuple[float, int]] = Counter()
    examples: dict[tuple[float, int], tuple[tuple[int, ...], tuple[int, ...]]] = {}

    for i, f in enumerate(maps):
        for g in maps[i:]:
            laws = (f, g)
            gamma = round(law_genesis_cost_uniform(laws), 12)
            beta = critical_seed_rank(laws)
            key = (gamma, beta)
            counts[key] += 1
            examples.setdefault(key, (f, g))

    rows = []
    for (gamma, beta), count in sorted(counts.items()):
        f, g = examples[(gamma, beta)]
        rows.append(
            {
                "gamma": gamma,
                "beta": beta,
                "count": count,
                "example_f": list(f),
                "example_g": list(g),
            }
        )
    return rows


def payload(n: int) -> dict:
    return {
        "state_count": n,
        "law_count": 2,
        "unordered_law_families": unordered_family_count(n),
        "groups": enumerate_two_law_systems(n),
        "claim": f"Gamma does not determine critical seed rank beta on the enumerated {n}-state deterministic systems.",
    }


def write_payload(n: int, out: Path = Path("results")) -> Path:
    out.mkdir(exist_ok=True)
    path = out / f"exhaustive_n{n}_two_law.json"
    path.write_text(json.dumps(payload(n), indent=2) + "\n", encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3, choices=(2, 3, 4))
    args = parser.parse_args()
    path = write_payload(args.n)
    print(path)


if __name__ == "__main__":
    main()
