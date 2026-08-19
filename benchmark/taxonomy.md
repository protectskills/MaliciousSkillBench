# Taxonomy

MaliciousSkillBench provides a **harmonized attack taxonomy** and a **derived harmonized impact taxonomy**. Both are partial. Neither is a claim of complete threat coverage.

## Attack taxonomy

Attack mapping coverage is **4,983 / 7,505** malicious identities (66.4%). The remaining malicious identities are unmapped rather than labeled as “no attack.” Mappings are multi-label.

There are **11** harmonized attack categories:

| Stable code | Display name |
|---|---|
| `execution_code_delivery` | Execution / Code Delivery |
| `instruction_goal_memory_manipulation` | Instruction / Goal / Memory Manipulation |
| `privilege_tool_authority_abuse` | Privilege / Tool / Authority Abuse |
| `data_exfiltration_disclosure` | Data Exfiltration / Disclosure |
| `resource_availability_abuse` | Resource / Availability Abuse |
| `credential_access` | Credential Access |
| `persistence_control` | Persistence / Control |
| `dependency_supply_chain` | Dependency / Supply-Chain Abuse |
| `integrity_output_manipulation` | Integrity / Output Manipulation |
| `defense_evasion_obfuscation` | Defense Evasion / Obfuscation |
| `discovery_reconnaissance` | Discovery / Reconnaissance |

Public tables expose both display names (`attack_categories`) and stable codes (`attack_category_codes`). Hugging Face `attack_taxonomy.parquet` contains only the 4,983 mapped malicious identities.

## Derived impact taxonomy

Derived-impact mapping coverage is **2,128 / 7,505** malicious identities (28.4%). The attack × impact intersection is **1,888 / 7,505** (25.2%).

These are **derived harmonized impacts**. They are not source-provided annotations and must not be treated as ground truth.

Stable derived-impact codes used in the public schema:

- `unauthorized_code_execution_system_control`
- `sensitive_data_disclosure`
- `credential_compromise`
- `agent_control_instruction_compromise`
- `privilege_control_manipulation`
- `resource_service_abuse`
- `persistence_sustained_control`
- `availability_destructive_impact`
- `integrity_output_manipulation`

Hugging Face `impact_taxonomy.parquet` contains only the 2,128 mapped identities.

## Figure notes

Figure 1 includes a schematic source × attack miniature. Figure 2 is the quantitative threat landscape: attack distribution (N = 4,983), source × attack heatmap, and attack × impact heatmap (N = 1,888).
