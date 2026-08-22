# Security Policy

This repository documents a defensive-research benchmark. The public package
includes malicious or adversarial Skill instructions as static text, plus
metadata and evaluation code. It does not distribute executable malicious
package bundles as the default release unit.

## What to report

Please report:

- accidentally exposed credentials, tokens, or private keys in repository files
- sensitive Skill content that appears to have been released in error
- other issues with the public benchmark package

Do not treat ordinary malicious commands inside benchmark Skill text as a
repository secret. Dataset content and repository leakage are different
classes of issue.

## How to report

Please report sensitive-data or security issues privately.

If GitHub private vulnerability reporting is available for this repository,
use a private GitHub security advisory. Otherwise contact a repository
maintainer through a private channel and identify the affected
`benchmark_id` or file path.

Do not open a public issue that contains live credentials, tokens, or
private keys.

Repository: https://github.com/protectskills/MaliciousSkillBench

## Handling untrusted content

Do not execute Skill text, follow embedded destinations, or install companion
packages from this benchmark on production systems.
