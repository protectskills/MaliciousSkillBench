#!/usr/bin/env python3
"""Run the three public MaliciousSkillBench learned baselines.

Models:
  word_tfidf_logreg
  word_tfidf_linear_svm
  char_tfidf_linear_svm

The script reads Skill text as inert data. It never executes Skill content
and does not use source, provenance, taxonomy, or family fields as features.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from evaluation.metrics import detection_metrics  # noqa: E402


MODELS = ("word_tfidf_logreg", "word_tfidf_linear_svm", "char_tfidf_linear_svm")
PROTOCOLS = ("random", "source_balanced_random", "m_structural_disjoint", "source_disjoint")
DEFAULT_DATASET_ID = "ORG/MaliciousSkillBench"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fit a public TF-IDF baseline on a frozen MaliciousSkillBench protocol."
    )
    parser.add_argument("--model", choices=MODELS, default="word_tfidf_linear_svm")
    parser.add_argument("--protocol", choices=PROTOCOLS, default="random")
    parser.add_argument("--seed", type=int, default=42, help="Default 42, matching the public frozen seed.")
    parser.add_argument(
        "--dataset-id",
        default=DEFAULT_DATASET_ID,
        help="Hugging Face dataset id. ORG/MaliciousSkillBench is a staging placeholder.",
    )
    parser.add_argument("--primary-parquet", type=Path, help="Local primary.parquet (preferred before Hub publication).")
    parser.add_argument("--splits-dir", type=Path, default=ROOT / "metadata" / "splits")
    parser.add_argument("--max-train", type=int, default=0, help="Optional cap for smoke tests; 0 uses the full split.")
    return parser.parse_args()


def model_spec(name: str, seed: int) -> Pipeline:
    if name == "word_tfidf_logreg":
        return Pipeline([
            ("vectorizer", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.995, max_features=120000, sublinear_tf=True, strip_accents="unicode", dtype=np.float32)),
            ("classifier", LogisticRegression(C=1.0, class_weight="balanced", random_state=seed, solver="liblinear", max_iter=1500)),
        ])
    if name == "word_tfidf_linear_svm":
        return Pipeline([
            ("vectorizer", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.995, max_features=120000, sublinear_tf=True, strip_accents="unicode", dtype=np.float32)),
            ("classifier", LinearSVC(C=1.0, class_weight="balanced", random_state=seed, max_iter=6000)),
        ])
    if name == "char_tfidf_linear_svm":
        return Pipeline([
            ("vectorizer", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=2, max_features=160000, sublinear_tf=True, dtype=np.float32)),
            ("classifier", LinearSVC(C=1.0, class_weight="balanced", random_state=seed, max_iter=6000)),
        ])
    raise ValueError(name)


def load_splits(path: Path) -> dict[str, list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    parts: dict[str, list[dict[str, str]]] = {"train": [], "validation": [], "test": []}
    for row in rows:
        if row["split"] in parts:
            parts[row["split"]].append(row)
    return parts


def load_text_map(args: argparse.Namespace) -> dict[str, str]:
    if args.primary_parquet is not None:
        import pandas as pd

        frame = pd.read_parquet(args.primary_parquet, columns=["benchmark_id", "skill_text", "text_available"])
        return {
            str(row.benchmark_id): ("" if row.skill_text is None else str(row.skill_text))
            for row in frame.itertuples()
            if bool(row.text_available)
        }
    from datasets import load_dataset

    if args.dataset_id == DEFAULT_DATASET_ID:
        raise SystemExit(
            "ORG/MaliciousSkillBench is a staging placeholder. Pass --primary-parquet for local files."
        )
    data = load_dataset(args.dataset_id, split="train")
    return {
        row["benchmark_id"]: (row.get("skill_text") or "")
        for row in data
        if row.get("text_available")
    }


def main() -> int:
    args = parse_args()
    parts = load_splits(args.splits_dir / f"{args.protocol}.csv")
    texts = load_text_map(args)
    train = [row for row in parts["train"] if row["benchmark_id"] in texts]
    test = [row for row in parts["test"] if row["benchmark_id"] in texts]
    if args.max_train:
        train = train[: args.max_train]
        test = test[: max(1, args.max_train // 4)]
    if not train or not test:
        raise SystemExit("no overlapping text rows for the requested split")
    estimator = model_spec(args.model, args.seed)
    x_train = [texts[row["benchmark_id"]] for row in train]
    y_train = np.array([int(row["label"]) for row in train])
    x_test = [texts[row["benchmark_id"]] for row in test]
    y_test = np.array([int(row["label"]) for row in test])
    estimator.fit(x_train, y_train)
    pred = estimator.predict(x_test)
    metrics = detection_metrics(y_test, pred)
    print(
        f"{args.model} {args.protocol} seed={args.seed} "
        f"train={len(train)} test={len(test)} "
        f"macro_f1={metrics['macro_f1']:.3f} "
        f"malicious_recall={metrics['malicious_recall']:.3f} "
        f"benign_fpr={metrics['benign_fpr']:.3f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
