# Full Skill Package Release

MaliciousSkillBench distributes two complementary layers.

1. **Static benchmark / index (Hugging Face).** The directly loadable public dataset provides frozen Skill text (or sanitized public text), labels, provenance, taxonomy, structural metadata, split membership, and hashes. Load it with `datasets.load_dataset("ProtectSkills/MaliciousSkillBench", "primary")`.
2. **Full Skill packages (GitHub Releases).** Reviewed source-package archives are distributed separately through GitHub Releases when the source artifacts exist and redistribution is authorized. These archives are **not** committed into the Git source tree.

The frozen benchmark remains **9,740** identities (7,505 malicious, 2,235 benign, 4,588 structural families). Adding package distribution does not create a new benchmark version.

## Current full-package scope: SRC002 only

The first full-package release covers **SRC002 — MaliciousAgentSkillsBench** only.

Other source package artifacts are **not** publicly downloadable yet. Do not treat this release as a complete 9,740-package dump.

| Item | Count |
|---|---:|
| Accepted SRC002 source artifacts | 157 |
| Exact to the preserved historical snapshot | 152 |
| Sanitized (not bit-identical) | 5 |
| Direct SRC002 primary benchmark rows | 153 |
| Cross-source deduplicated artifacts mapped to existing frozen identities | 3 |
| Cross-label-excluded source-release-only artifact | 1 |
| Missing | 0 |
| Ambiguous | 0 |

Release page: [https://github.com/protectskills/MaliciousSkillBench/releases/tag/src002-full-packages](https://github.com/protectskills/MaliciousSkillBench/releases/tag/src002-full-packages)

Primary archive: `SRC002_packages.tar.gz`

SHA256:

```
bf2532cb0e7fd3a76a2cf1bbb53cff1cd77fe67b3f152f802c084ef196860ed5
```

Five packages are released as `SANITIZED_NOT_BIT_IDENTICAL` because sensitive credential material was removed: `rest_422:legacy_v1`, `smp_1710:web-build`, `smp_1881:nanobanana-base`, `smp_2362:terra-data`, and `smp_3764:analytics`. They retain package structure and non-sensitive research content. Do not treat them as bit-identical to the preserved snapshot.

`smp_3604:dexter` is included in the 157-artifact source release but is not one of the 9,740 primary benchmark identities, because of a conservative cross-label conflict exclusion.

## How to verify the archive

Download `SRC002_packages.tar.gz` from the GitHub Release, then:

```bash
shasum -a 256 SRC002_packages.tar.gz
```

The digest must equal `bf2532cb0e7fd3a76a2cf1bbb53cff1cd77fe67b3f152f802c084ef196860ed5`.

Release-facing checksums with asset filenames are in [`metadata/packages/src002/RELEASE_SHA256SUMS.txt`](../metadata/packages/src002/RELEASE_SHA256SUMS.txt). The audited checksum file with original review-bundle paths is [`metadata/packages/src002/SHA256SUMS.txt`](../metadata/packages/src002/SHA256SUMS.txt); its contents were not rewritten.

## How `package_manifest` maps archive paths to benchmark identities

Public manifests:

- [`metadata/packages/src002/package_manifest.csv`](../metadata/packages/src002/package_manifest.csv)
- [`metadata/packages/src002/package_manifest.parquet`](../metadata/packages/src002/package_manifest.parquet)
- [`metadata/packages/src002/package_file_manifest.parquet`](../metadata/packages/src002/package_file_manifest.parquet)
- [`metadata/packages/src002/src002_release_closure.csv`](../metadata/packages/src002/src002_release_closure.csv)

Each `package_manifest` row identifies one accepted SRC002 source artifact. Use `package_relative_path` to locate the package root inside the archive. Use `benchmark_id` / `canonical_id` when the artifact maps onto a frozen benchmark identity. `release_fidelity` records whether the released tree is `EXACT_TO_PRESERVED_SNAPSHOT` or `SANITIZED_NOT_BIT_IDENTICAL`. `source_release_membership` and `benchmark_primary_membership` distinguish source-release inclusion from primary-benchmark membership.

The same reviewed manifests are also published on Hugging Face under `package_release/src002/` as an index layer. Hugging Face does not host `SRC002_packages.tar.gz`.

## Attribution and terms

SRC002 package bytes retain their recorded upstream terms (MIT, attribution required) for the 157 accepted author-provided historical snapshot packages. They are not relicensed under Apache-2.0 or CC BY 4.0.

- Upstream paper: https://arxiv.org/abs/2602.06547
- Upstream dataset: https://huggingface.co/datasets/ProtectSkills/MaliciousAgentSkillsBench

See [`THIRD_PARTY_NOTICE.md`](../THIRD_PARTY_NOTICE.md).

## Safety

These artifacts may contain malicious or adversarial Agent Skill logic. Do not execute untrusted Skills, shell scripts, Python, JavaScript, binaries, installers, or other package contents. Do not follow embedded URLs or install companion packages on production systems. Use isolated, non-production analysis environments.
