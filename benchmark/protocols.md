# Evaluation Protocols

MaliciousSkillBench releases four frozen protocols. Use the supplied manifests in [`metadata/splits/`](../metadata/splits/). Do not regenerate splits.

Each protocol CSV has one row per benchmark identity with columns `benchmark_id`, `label`, `source_id`, and `split`. Join to the primary table on `benchmark_id`. Hugging Face also publishes typed Parquet copies of the same frozen membership tables; those Parquet files are the official `load_dataset(..., "splits")` path.

## Protocol sizes

| Protocol | File | Train | Validation | Test | Other |
|---|---|---:|---:|---:|---|
| Random | `random.csv` | 6,818 | 974 | 1,948 | — |
| Source-Balanced Random | `source_balanced_random.csv` | 6,817 | 973 | 1,950 | — |
| Malicious-Structural-Disjoint | `m_structural_disjoint.csv` | 6,818 | 974 | 1,948 | — |
| Source-Disjoint | `source_disjoint.csv` | 7,513 | 835 | 1,384 | 8 `excluded` |

All four manifests contain 9,740 rows.

## What each protocol tests

**Random.** A conventional i.i.d.-style partition of the 9,740 identities. Near-duplicate Skills from the same structural family may appear in more than one split.

**Source-Balanced Random.** A random partition that balances source composition more evenly across splits. It remains a random partition rather than a disjointness protocol.

**Malicious-Structural-Disjoint.** Malicious structural families are not shared across train/validation/test. This reduces evaluation leakage from near-duplicate malicious Skills. It is not a claim that all possible structural reuse has been removed.

**Source-Disjoint.** Training sources and evaluation sources are disjoint. Held-out sources are `SRC009`, `SRC011`, and `SRC012`. The test set contains 839 malicious and 545 benign identities. Results from this protocol describe **source-conditioned shift**. They should not be reported as universal unseen-source or out-of-distribution generalization.

The 8 Source-Disjoint `excluded` identities are retained for exact protocol accounting and are outside train/validation/test.

The frozen benchmark retains 4,588 structural-family identifiers. After conservative cross-label exclusion, 4,575 of these identifiers are represented by at least one final primary malicious identity; 13 retained family IDs have no final primary member.

## Recommended reporting

Report detection metrics separately for each protocol. Headline learned-detector results in the paper and project page use Macro-F1, malicious recall, and benign false-positive rate. See [`../evaluation/metrics.py`](../evaluation/metrics.py).
