# Responsible Use

MaliciousSkillBench is intended for defensive security research and detection evaluation.

- The benchmark contains malicious or adversarial Skill instructions.
- Use the data in isolated, non-production analysis environments.
- Do not execute untrusted Skills, follow embedded URLs, or install companion packages from benchmark artifacts.
- The public release emphasizes static Skill instruction representation.
- Some content is intentionally withheld when it is sensitive or when a public snapshot cannot be redistributed.
- Sensitive credentials identified during release QA are withheld or redacted rather than published as full text.
- Executable malicious package bundles are not the default public release unit.

All 9,740 benchmark identities remain in the public dataset records. Public Skill text is available for 9,549 identities; 5 records are sensitive-withheld and 186 are snapshot-withheld. Withheld rows retain identifiers, labels, provenance, hashes, and frozen split membership.

See `SECURITY.md` for reporting accidentally exposed credentials or other release issues.
