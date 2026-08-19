# Evaluation

This directory contains small reproducibility helpers for the frozen protocols. It does not rerun the paper's learned-detector experiments.

## Validate metadata

From the repository root:

```bash
python evaluation/validate_dataset.py
```

The validator checks:

- 9,740 unique `benchmark_id` values
- 7,505 malicious and 2,235 benign labels
- four frozen split manifests and their train/validation/test sizes
- Source-Disjoint held-out sources `SRC009`, `SRC011`, and `SRC012`

It reads GitHub metadata only (`metadata/benchmark_manifest.csv` and `metadata/splits/`). It does not require Hugging Face Parquet and does not execute Skill text.

```bash
python evaluation/validate_dataset.py --help
```

## Metrics

`metrics.py` implements the paper-facing binary detection metrics:

- Macro-F1
- malicious recall
- benign false-positive rate
- accuracy

Labels are `1` for malicious and `0` for benign. Join predictions to split manifests on `benchmark_id`.
