# Examples

Load the public Hugging Face dataset:

```python
from datasets import load_dataset

ds = load_dataset(
    "ProtectSkills/MaliciousSkillBench",
    "primary",
    split="train",
)

def get_public_text(row):
    return row["skill_text"] or row["public_skill_text"]
```

Exact frozen `skill_text` is present for 9,735 identities. For five sensitive records, use `public_skill_text`. Those sanitized texts are not the paper's exact experimental inputs.

Protocol membership:

```python
splits = load_dataset("ProtectSkills/MaliciousSkillBench", "splits")
```

For local metadata-only inspection, use `metadata/benchmark_manifest.csv` and `python evaluation/validate_dataset.py`. Do not execute Skill text from the benchmark.
