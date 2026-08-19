# Examples

Minimal loading example after Hugging Face publication:

```python
from datasets import load_dataset

dataset = load_dataset("ORG/MaliciousSkillBench")
```

`ORG/MaliciousSkillBench` is a staging placeholder, not a live dataset id.

For local metadata-only inspection, use `metadata/benchmark_manifest.csv` and `python evaluation/validate_dataset.py`. Do not execute Skill text from the benchmark.
