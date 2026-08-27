# Decision register and ADR process

| Metadata | Value |
| --- | --- |
| Status | Current process and decision inventory |
| Audience | All decision owners, implementers, and reviewers |
| Accountable role | Architecture lead maintains the register; listed roles decide their domain |
| Review trigger | Decision state, evidence, owner, due gate, or ADR change |
| Authority | Normative decision process; candidate choices remain Proposed/Open/Deferred |

## Decision policy

No architectural decision is accepted merely because it appears in a diagram or candidate table. **Accepted** is recorded as `Current` with a linked ADR and evidence. This repository currently has no accepted implementation-technology ADRs.

Create an ADR when a choice is consequential, difficult to reverse, contested, security/privacy relevant, or required by a delivery gate. An ADR records: title/status; context; decision; considered options; consequences; accountable owner; decision date; evidence; validation/rollback; affected documents; and superseded ADRs. Review dates are not invented; review triggers are explicit.

Store the first accepted ADR under `docs/adr/NNNN-short-title.md` and add it to this register. Do not create the directory or an ADR solely to make the structure appear complete. Proposed and Open items remain here until evidence supports a decision.

## Register

| Topic | State | Due gate | Accountable owner | Required reviewers | Required evidence |
| --- | --- | --- | --- | --- | --- |
| Observational, single-vehicle SITL MVP with no command path | Proposed scope baseline | Phase 0 exit | Product owner | Safety owner | Scope and hazard-boundary review |
| Initial SITL/autopilot, dialect, message and signing profile | Open | Phase 1 entry | Telemetry lead | — | Executable compatibility matrix and fixture |
| Canonical schema, encoding, commitment fields and snapshot freshness | Open | Phase 1 exit / Phase 2 entry | Architecture lead | Cryptography and security leads | Reviewed specification and golden vectors |
| Trust-state claim eligibility | Open | Phase 1 exit | Security lead | — | Threat analysis and signed/unsigned/invalid tests |
| Proof system, circuit toolchain, setup and key lifecycle | Open | Phase 2 exit | Cryptography lead | Security lead | Benchmark/compatibility ADR and independent review |
| Clock authority, skew/window and replay policy | Open | Phase 2 exit | Security lead | — | Threat analysis, restart and negative tests |
| Internal/API contract technology | Open | Before public API implementation | Architecture lead | — | Compatibility/ergonomics spike and contract tests |
| Rust/Tokio and MAVLink library | Proposed candidate | Phase 0/1 | Engineering lead | Telemetry lead | Maintained-library review, signing compatibility, fuzz/benchmark result |
| UI technology and event transport | Proposed candidate | Phase 3 | Engineering lead | — | Auth/redaction/accessibility design evidence |
| Midnight SDK, network, contract language and verification route | Open | Phase 4 entry | Chain lead | — | Pinned executable spike, disclosure/cost/finality notes |
| Public chain metadata allowlist | Open | Phase 4 entry | Product/privacy owner | Security lead | Observer-focused privacy review |
| Metadata persistence technology | Deferred until lifecycle needs it | Phase 3 | Service owner | — | State/restart requirement and migration/backup design |
| Data purpose, jurisdiction and retention | Open | Phase 3 exit; before hardware | Product/privacy owner | — | Data inventory and approved retention/deletion schedule |
| Authentication and administrative authorization | Open | Phase 3 | Security lead | — | Threat model and authorization matrix |
| SLOs and production topology | Deferred until measurements | Phase 5 entry | Service owner | SRE | Load results, workload and capacity model |
| Hardware pilot safety case | Deferred | Before hardware connection | Safety owner | — | Hazard analysis and approved controlled test plan |
| Live-chain production, HA, Kubernetes, brokers, cache, object storage, multi-region | Deferred | Separate post-MVP decision | Architecture lead | Product, security, privacy, and operations leads | Demonstrated requirement and operational evidence |

## Current invariants versus decisions

The only `Current` claims concern repository reality and documentation governance: the repository is documentation-only, this register is the decision process, and no implementation ADR exists. MVP scope and architecture are Proposed constraints to guide the first implementation; they become accepted decisions only through accountable review. Open items block their stated gates. Deferred items are not implied future commitments.

## Validation and related documents

The architecture lead checks that every closed item links evidence and an ADR, every Open item has one owner and due gate, and superseded decisions update affected documents. See [documentation governance](README.md), [delivery gates](delivery-plan.md), and the owning topic documents indexed there.
