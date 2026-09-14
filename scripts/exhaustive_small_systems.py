"""Exhaustive enumeration of tiny deterministic Law-Genesis systems.

The default n=3, two-law run is small enough for CI and is used as a
falsification/regression search.  It groups systems by Law Genesis Cost and
critical seed rank, showing that Gamma does not determine beta even on three
states.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import product
from pathlib import Path

from law_genesis.core import law_genesis_cost_uniform
from law_genesis.metrics import critical_seed_rank


def transformations(n: int):
    yield from product(range(n), repeat=n)


def enumerate_two_law_systems(n: int = 3):
    maps = list(transformations(n))
    counts: Counter[tuple[float, int]] = Counter()
    examples: dict[tuple[float, int], tuple[tuple[int, ...], tuple[int, ...]]] = {}

    # Treat {f,g} as an unordered microscopic-law family, including f=g.
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


def main() -> None:
    rows = enumerate_two_law_systems(3)
    out = Path("results")
    out.mkdir(exist_ok=True)
    payload = {
        "state_count": 3,
        "law_count": 2,
        "unordered_law_families": 378,
        "groups": rows,
        "claim": "Gamma does not determine critical seed rank beta on three-state deterministic systems.",
    }
    path = out / "exhaustive_n3_two_law.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(path)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
