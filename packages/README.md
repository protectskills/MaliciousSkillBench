# Skill Packages

This directory contains source-level malicious Agent Skill artifacts
corresponding to the 7,505 malicious identities in MaliciousSkillBench.

Artifacts are grouped by source. `package_manifest.csv` maps each frozen
malicious benchmark identity to its source archive and package-relative path.

Some source artifacts are naturally multi-file Skill packages, while others
are source-native single files. Sensitive credential values are replaced with
sanitized placeholders where necessary; such cases are marked in the
manifest.

The SRC002 archive preserves 157 accepted source artifacts: 153 primary
benchmark identities, three cross-source duplicates, and one
cross-label-excluded source artifact. The global package manifest contains the
153 SRC002 identities that belong to the frozen malicious benchmark.

Do not execute untrusted Skill package contents.
