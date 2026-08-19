# Off-the-shelf scanner evaluation

This directory documents the frozen public scanner comparison. It does not include scanner environments, Skill execution harnesses, or bulk Skill inputs.

Evaluated methods and exact public names:

- **Cisco-local-behavioral**
- **SkillFortify-offline**
- **SkillSpector-static**

These are operational comparisons on frozen protocols. They are not a claim that any scanner was reproduced in every vendor configuration.

## Source-Disjoint headline

| Method | Macro-F1 | Malicious recall | Benign FPR |
|---|---:|---:|---:|
| Cisco-local-behavioral | 0.308 | 2.5% | 1.1% |
| SkillFortify-offline | 0.349 | 25.3% | 49.9% |
| SkillSpector-static | 0.281 | 0.0% | 0.55% |

Different methods occupy different false-positive / false-negative operating regimes. No evaluated method jointly achieves high malicious recall and low benign false-positive rates under source shift.

Do not summarize this table as “all scanners overflag benign.” Cisco-local-behavioral and SkillSpector-static have low FPR largely alongside very low recall.

## Method caveats

**SkillSpector-static** is a static / no-LLM configuration. It is not the LLM-backed SkillSpector configuration used in some external work.

**Cisco-local-behavioral** was run in a local compatibility environment. Environment internals are intentionally not the focus of the public README; treat this as a reproducibility limitation of the local setup rather than a modified scanner rule set.

## ColluSkill is a different task

ColluSkill evaluates adversarial attack-evasion success rate (ASR). This experiment evaluates binary malicious/benign detection with Macro-F1, malicious recall, and benign FPR. Do not compare ColluSkill ASR with these detection metrics as if they were the same quantity.

## Frozen numbers

See [`source_disjoint_results.csv`](source_disjoint_results.csv). These values are copied from the frozen public evaluation; they are not recomputed here.
