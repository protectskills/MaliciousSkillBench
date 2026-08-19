# Benchmark Schema

This GitHub package documents the public schema. Hugging Face is the primary data host; the typed field contract is `schema.json` in this directory, copied from the Hugging Face staging package.

The GitHub metadata table `metadata/benchmark_manifest.csv` has one row per benchmark identity and does **not** include full Skill text. Load `skill_text` from Hugging Face `primary.parquet`.

## Identity and labels

| Field | Type | Null | Meaning |
|---|---|---|---|
| `benchmark_id` | string | never | Stable primary identity. |
| `label` | string | never | Frozen label code: `1` malicious, `0` benign. |
| `source_id` | string | never | Primary contributing source. |
| `source_name` | string | never | Human-readable primary source name. |
| `source_ids` | list[string] (HF) / semicolon-delimited (GitHub CSV) | never | All contributing source IDs. |
| `provenance` | string | never | Frozen provenance category. |
| `evidence_type` | string | allowed | Frozen evidence type when available. |
| `structural_family_id` | string | benign rows | Malicious structural-family ID. Null for benign rows rather than a fabricated family. |
| `normalized_hash` | string | never | Frozen normalized identity hash. |
| `exact_hash` | string | never | Frozen exact Skill-text hash. |
| `release_status` | string | never | Public text-release decision. |
| `source_pointer` | string | allowed | Public source or project URL, never a local path. |

## Text fields (Hugging Face `primary` only)

| Field | Type | Null | Meaning |
|---|---|---|---|
| `skill_text` | string | withheld rows only | Static Skill text. Null for `WITHHELD_SENSITIVE`, `WITHHELD_SNAPSHOT`, or `WITHHELD_TECHNICAL`. |
| `text_available` | boolean | never | Whether public static text is present. |
| `text_redacted` | boolean | never | Whether public text contains packaging-level redactions. |
| `text_origin_source_id` | string | allowed | Source ID for the public text origin when available. |

## Taxonomy fields

| Field | Type | Empty | Meaning |
|---|---|---|---|
| `attack_categories` | list[string] | `[]` | Harmonized attack display names. Covers 4,983 of 7,505 malicious identities. |
| `attack_category_codes` | list[string] | `[]` | Stable attack codes corresponding to `attack_categories`. |
| `impact_categories` | list[string] | `[]` | Derived harmonized impact display names. Covers 2,128 of 7,505 malicious identities. |
| `impact_category_codes` | list[string] | `[]` | Stable derived impact codes. |

Unmapped taxonomy fields use empty lists, not null. GitHub CSV serializes lists as semicolon-delimited strings; Hugging Face Parquet uses `list[string]`.

## Null policy

- `skill_text` is null only for intentionally withheld records.
- `structural_family_id` is null for benign rows.
- Taxonomy lists are `[]` when unmapped.
- Do not interpret empty taxonomy lists as “no threat.” They mean “not mapped.”

## Hugging Face configurations

The Dataset Card exposes five configurations. Only `primary` is the default.

| Config | File | Rows |
|---|---|---:|
| `primary` | `primary.parquet` | 9,740 |
| `metadata` | `metadata.parquet` | 9,740 |
| `attack_taxonomy` | `attack_taxonomy.parquet` | 4,983 |
| `impact_taxonomy` | `impact_taxonomy.parquet` | 2,128 |
| `splits` | `splits/*.csv` | 9,740 per protocol |

Join split manifests to the primary table on `benchmark_id`.
