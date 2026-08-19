#!/usr/bin/env python3
"""Validate MaliciousSkillBench GitHub metadata against frozen protocol sizes.

This script reads CSV metadata only. It does not execute Skill text and does
not require Hugging Face Parquet.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


csv.field_size_limit(sys.maxsize)

EXPECTED = {
    "total": 9740,
    "malicious": 7505,
    "benign": 2235,
    "structural_families": 4588,
    "protocols": {
        "random": {"train": 6818, "validation": 974, "test": 1948},
        "source_balanced_random": {"train": 6817, "validation": 973, "test": 1950},
        "m_structural_disjoint": {"train": 6818, "validation": 974, "test": 1948},
        "source_disjoint": {"train": 7513, "validation": 835, "test": 1384, "excluded": 8},
    },
    "source_disjoint_held_out": {"SRC009", "SRC011", "SRC012"},
    "source_disjoint_test": {"malicious": 839, "benign": 545},
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate frozen MaliciousSkillBench GitHub metadata counts and split manifests."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=repo_root(),
        help="GitHub staging root (default: parent of this script).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.repo_root.resolve()
    manifest_path = root / "metadata" / "benchmark_manifest.csv"
    family_path = root / "metadata" / "structural_families.csv"
    failures: list[str] = []

    rows = read_csv(manifest_path)
    labels = Counter(row["label"] for row in rows)
    ids = [row["benchmark_id"] for row in rows]
    if len(rows) != EXPECTED["total"]:
        failures.append(f"manifest rows {len(rows)} != {EXPECTED['total']}")
    if len(set(ids)) != EXPECTED["total"]:
        failures.append("benchmark_id values are not unique")
    if labels.get("1", 0) != EXPECTED["malicious"]:
        failures.append(f"malicious {labels.get('1', 0)} != {EXPECTED['malicious']}")
    if labels.get("0", 0) != EXPECTED["benign"]:
        failures.append(f"benign {labels.get('0', 0)} != {EXPECTED['benign']}")
    if "skill_text" in (rows[0] or {}):
        failures.append("GitHub manifest unexpectedly contains skill_text")

    families = read_csv(family_path)
    if len(families) != EXPECTED["structural_families"]:
        failures.append(f"structural families {len(families)} != {EXPECTED['structural_families']}")

    for protocol, expected in EXPECTED["protocols"].items():
        split_rows = read_csv(root / "metadata" / "splits" / f"{protocol}.csv")
        counts = Counter(row["split"] for row in split_rows)
        if len(split_rows) != EXPECTED["total"]:
            failures.append(f"{protocol} rows {len(split_rows)} != {EXPECTED['total']}")
        for part, value in expected.items():
            if counts.get(part, 0) != value:
                failures.append(f"{protocol}/{part} {counts.get(part, 0)} != {value}")

    source_disjoint = read_csv(root / "metadata" / "splits" / "source_disjoint.csv")
    test = [row for row in source_disjoint if row["split"] == "test"]
    test_sources = {row["source_id"] for row in test}
    if test_sources != EXPECTED["source_disjoint_held_out"]:
        failures.append(f"source-disjoint test sources {sorted(test_sources)}")
    mal = sum(row["label"] == "1" for row in test)
    ben = sum(row["label"] == "0" for row in test)
    if mal != EXPECTED["source_disjoint_test"]["malicious"] or ben != EXPECTED["source_disjoint_test"]["benign"]:
        failures.append(f"source-disjoint test counts malicious={mal} benign={ben}")

    if failures:
        print("FAIL")
        for item in failures:
            print("-", item)
        return 1
    print(
        "PASS",
        EXPECTED["total"],
        "identities;",
        EXPECTED["malicious"],
        "malicious;",
        EXPECTED["benign"],
        "benign;",
        "four frozen protocols",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
