from __future__ import annotations

import csv
import json
from pathlib import Path

from examples.nonlinear_depth_witness import SYSTEM_A, SYSTEM_B, summary

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def main() -> None:
    data = {"A": summary(SYSTEM_A), "B": summary(SYSTEM_B)}

    with (RESULTS / "nonlinear_depth_witness.json").open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

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

    print("generated nonlinear depth witness results")


if __name__ == "__main__":
    main()
