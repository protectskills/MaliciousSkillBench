# Benchmark Schema

This GitHub package documents the public schema. Hugging Face is the primary data host; the typed field contract is `schema.json` in this directory, copied from the Hugging Face staging package.

The GitHub metadata table `metadata/benchmark_manifest.csv` has one row per benchmark identity and does **not** include full Skill text. Load `skill_text` and, when needed, `public_skill_text` from Hugging Face `primary.parquet`.

Top-level `fields` in `schema.json` is a **union across configs**, including taxonomy-only `mapping_provenance`. It is not a second primary schema. Use `configs.<name>.fields` for the contract of each Parquet file.

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
| `normalized_hash` | string | never | Frozen normalized identity hash of the original artifact. |
| `exact_hash` | string | never | Frozen exact Skill-text hash of the original artifact. |
| `release_status` | string | never | Public text-release decision: `FULL_TEXT` or `REDACTED_TEXT`. |
| `source_pointer` | string | allowed | Public source or project URL, never a local path. |
| `redaction_reason` | string | allowed | `sensitive_credential_material` for the five sanitized records; empty/null otherwise. |
| `original_text_withheld` | boolean | never | True only for the five records whose exact original text remains withheld. |

## Text fields (Hugging Face `primary` only)

| Field | Type | Null | Meaning |
|---|---|---|---|
| `skill_text` | string | five redacted rows | Exact frozen Skill text when publicly available. Null only when the original text is withheld. |
| `public_skill_text` | string | all exact-text rows | Sanitized public representation provided only for the five sensitive records. Null for the other 9,735 records. |
| `text_available` | boolean | never | Whether exact frozen `skill_text` is present. |
| `text_redacted` | boolean | never | True for sanitized records and for packaging-level credential redaction in some public texts. |
| `text_origin_source_id` | string | allowed | Source ID for the public text origin when available. |
| `public_text_sha256` | string | exact-text rows | SHA-256 of `public_skill_text` for sanitized records. Does not replace benchmark hashes. |

Recommended public-readable text: `row["skill_text"] or row["public_skill_text"]`.

For redacted records, `normalized_hash` and `exact_hash` identify the frozen original artifact, not the sanitized public representation. The five sanitized texts are not bit-for-bit identical to the frozen experimental inputs.

## Taxonomy fields

| Field | Type | Empty | Meaning |
|---|---|---|---|
| `attack_categories` | list[string] | `[]` | Harmonized attack display names. Covers 4,983 of 7,505 malicious identities. |
| `attack_category_codes` | list[string] | `[]` | Stable attack codes corresponding to `attack_categories`. |
| `impact_categories` | list[string] | `[]` | Derived harmonized impact display names. Covers 2,128 of 7,505 malicious identities. |
| `impact_category_codes` | list[string] | `[]` | Stable derived impact codes. |

Unmapped taxonomy fields use empty lists, not null. GitHub CSV serializes lists as semicolon-delimited strings; Hugging Face Parquet uses `list[string]`.

## Null policy

- `skill_text` is null only for the five `REDACTED_TEXT` records.
- `public_skill_text` is non-null only for those five records.
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
| `splits` | `splits/*.parquet` | 9,740 per protocol |

CSV copies of the split manifests remain as convenience files. Join split manifests to the primary table on `benchmark_id`.
