# Responsible Use

MaliciousSkillBench is intended for defensive security research and detection evaluation.

- The benchmark contains malicious or adversarial Skill instructions.
- Use the data in isolated, non-production analysis environments.
- Do not execute untrusted Skills, follow embedded URLs, or install companion packages from benchmark artifacts.
- The public release emphasizes static Skill instruction representation.
- Some exact original text is withheld when it contains sensitive credential material.
- For those five records, a sanitized public representation is provided; the exact frozen original remains withheld.
- Historical author-provided snapshots are no longer a withholding reason; their exact frozen text is public.
- Package-level archives under `packages/`, where present, are untrusted research samples and must not be executed.

All 9,740 benchmark identities remain in the public dataset records. Exact frozen Skill text is available for 9,735 identities. Five malicious records withhold the exact original text and provide a sanitized representation instead. Withheld originals retain identifiers, labels, provenance, hashes, and frozen split membership.

See `SECURITY.md` for reporting accidentally exposed credentials or other release issues.
