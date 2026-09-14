from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from examples.fragility_separation import evaluate as evaluate_fragility
from examples.nonlinear_depth_witness import SYSTEM_A, SYSTEM_B, summary
from scripts.exhaustive_small_systems import enumerate_two_law_systems

RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def write_depth_witness() -> None:
    data = {"A": summary(SYSTEM_A), "B": summary(SYSTEM_B)}

    with (RESULTS / "nonlinear_depth_witness.json").open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    with (RESULTS / "nonlinear_depth_witness.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["system", "depth", "word", "gamma_bits", "class_sizes", "raw_disagreement_pairs"])
        for system, rows in data.items():
            for row in rows:
                writer.writerow([
                    system,
                    row["depth"],
                    row["word"],
                    f"{row['gamma_bits']:.12f}",
                    " ".join(map(str, row["class_sizes"])),
                    row["raw_disagreement_pairs"],
                ])


def write_fragility_family() -> None:
    rows = [evaluate_fragility(n) for n in range(2, 9)]
    with (RESULTS / "fragility_separation.json").open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
        f.write("\n")
    with (RESULTS / "fragility_separation.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_exhaustive_n3() -> None:
    rows = enumerate_two_law_systems(3)
    payload = {
        "state_count": 3,
        "law_count": 2,
        "unordered_law_families": 378,
        "groups": rows,
        "claim": "Gamma does not determine critical seed rank beta on three-state deterministic systems.",
    }
    with (RESULTS / "exhaustive_n3_two_law.json").open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def main() -> None:
    write_depth_witness()
    write_fragility_family()
    write_exhaustive_n3()
    print("generated Law Genesis theorem and falsification results")


if __name__ == "__main__":
    main()
