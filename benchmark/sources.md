# Sources

MaliciousSkillBench registers **13 public sources**. **11** of those sources are Core-contributing; the remaining two are auxiliary public sources retained for provenance and attribution.

Core-contributing is a construction-role label. It is not a quality ranking and does not mean that auxiliary sources are excluded from the public registry.

The public registry is [`metadata/source_registry.csv`](../metadata/source_registry.csv). It contains public names, roles, paper/project pointers, and provenance summaries. It does not contain private local paths or author-archive filenames.

## Registered sources

| ID | Name | Role | Core-contributing |
|---|---|---|---|
| SRC001 | MalSkillBench | Core and auxiliary | yes |
| SRC002 | MaliciousAgentSkillsBench | Core and auxiliary | yes |
| SRC003 | Skill-Inject | Auxiliary | no |
| SRC004 | SkillLeakBench | Core and auxiliary | yes |
| SRC005 | Agent Skill Malware | Core and auxiliary | yes |
| SRC006 | AgentTrap | Core and auxiliary | yes |
| SRC007 | ClawHub Security Signals | Auxiliary | no |
| SRC008 | SkillTrojan | Core and auxiliary | yes |
| SRC009 | SkillHarm | Core | yes |
| SRC010 | SkillTrustBench | Core and auxiliary | yes |
| SRC011 | ATR Skill Security Benchmark | Core and auxiliary | yes |
| SRC012 | SkillFortifyBench | Core and auxiliary | yes |
| SRC013 | SkillSafetyBench | Core and auxiliary | yes |

Source-Disjoint evaluation holds out `SRC009`, `SRC011`, and `SRC012`.

Use `source_id` / `source_ids` on each identity for provenance. Some identities have more than one contributing source because of cross-source reuse; `source_ids` lists all contributors, while `source_id` is the primary source used for source-conditioned accounting.
