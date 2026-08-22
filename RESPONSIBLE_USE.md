# Responsible Use

MaliciousSkillBench is intended for defensive security research and detection evaluation.

- The benchmark contains malicious or adversarial Skill instructions.
- Use the data in isolated, non-production analysis environments.
- Do not execute untrusted Skills, follow embedded URLs, or install companion packages from benchmark artifacts.
- Hugging Face hosts static public Skill representations and benchmark metadata.
- Reviewed full Skill package artifacts are additionally available for SRC002 through GitHub Releases; other source packages are not publicly downloadable yet.
- Do not execute untrusted package contents.
- Some exact original text is withheld when it contains sensitive credential material.
- For those five records, a sanitized public representation is provided; the exact frozen original remains withheld.
- Historical author-provided snapshots are no longer a withholding reason; their exact frozen text is public.

All 9,740 benchmark identities remain in the public dataset records. Exact frozen Skill text is available for 9,735 identities. Five malicious records withhold the exact original text and provide a sanitized representation instead. Withheld originals retain identifiers, labels, provenance, hashes, and frozen split membership.

See `SECURITY.md` for reporting accidentally exposed credentials or other release issues.
