# Learned baselines

Public headline baselines for MaliciousSkillBench:

1. Word TF-IDF + logistic regression
2. Word TF-IDF + linear SVM (Word-SVM; paper headline)
3. Char TF-IDF + linear SVM

These models use inert public Skill text only. Source IDs, provenance, hashes, taxonomy labels, and structural family IDs are excluded from features.

Frozen headline Word-SVM Macro-F1: Random 0.932, Malicious-Structural-Disjoint 0.916, Source-Disjoint 0.665.

## Run

The script expects Hugging Face `primary` text plus the frozen split CSVs. After the dataset is published:

```bash
python baselines/run_baselines.py --help
python baselines/run_baselines.py --protocol random --model word_tfidf_linear_svm --seed 42
```

Before Hub publication, pass local files:

```bash
python baselines/run_baselines.py \
  --primary-parquet /path/to/primary.parquet \
  --splits-dir /path/to/splits \
  --protocol source_disjoint \
  --model word_tfidf_linear_svm \
  --seed 42
```

The default dataset id is `ProtectSkills/MaliciousSkillBench`.

Default seed is 42. Full paper tables used seeds 42/43/44; this public CLI defaults to a single seed so that a reproduction run is deterministic and inspectable.

This directory does not include MiniLM, robustness sweeps, or other internal experimental variants as headline baselines.
