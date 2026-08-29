# Documentation guide

| Metadata | Value |
| --- | --- |
| Status | Current documentation governance; system content remains Proposed/Open/Deferred as marked |
| Audience | All contributors and reviewers |
| Accountable role | Architecture lead |
| Review trigger | Any document addition, status change, or ownership-model change |

## Purpose

This index is the navigation and authority map for a documentation-only project. It separates topics whose audiences, owners, and change cadences differ; the former [system plan](system-plan.md) is Superseded and is not an alternative baseline.

## Status and authority

Every substantive document declares its purpose, audience, status, accountable role, review trigger, authority, related documents, validation method, and open decisions.

- **Current** — demonstrably true of this repository or an active documentation rule.
- **Proposed** — intended design awaiting implementation evidence and, where material, an ADR.
- **Open** — requires evidence or accountable approval before implementation may rely on it.
- **Deferred** — intentionally postponed beyond the MVP.
- **Superseded** — retained for traceability but no longer authoritative.

`MUST`, `MUST NOT`, and **Required** identify normative constraints for the proposed MVP. Examples, text diagrams, candidate technologies, and proposed layouts are illustrative unless explicitly marked normative. An accepted ADR supersedes a conflicting proposal; scope changes also require product approval and synchronized document updates.

Roles identify accountability until named people are assigned. Review triggers are used instead of arbitrary review dates. Evidence should be linked from an ADR or milestone record when those artifacts exist.

## Reading paths

All root reading paths lead to the named next milestone, [**Validated claim and verifier contract**](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract). The [delivery plan](delivery-plan.md) is the owner of its entry conditions, workstream, required evidence, and exit rules. It permits bounded, disposable Phase 0 spikes while blocking broad Phase 1 production engineering until the milestone stop/go review passes; this remains planning for a documentation-only repository, not a claim that any prototype exists.

| Reader | Recommended path |
| --- | --- |
| New contributor | Root [README](../README.md) → [product scope](product-scope.md) → [delivery plan](delivery-plan.md) |
| Product or safety | [Product scope](product-scope.md) → [security and privacy](security-and-privacy.md) → [delivery plan](delivery-plan.md) |
| Commercial/product strategy | [Product scope](product-scope.md) → [commercial model](commercial-model.md) → [architecture](architecture.md) |
| Discovery researcher | [Discovery research plan](discovery-research-plan.md) → [product scope](product-scope.md) → [decisions](decisions.md) |
| Engineering/platform | [Architecture](architecture.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) |
| Cryptography | [Data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [security and privacy](security-and-privacy.md) → [decisions](decisions.md) |
| Security/privacy | [Security and privacy](security-and-privacy.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) |
| Decision maker | [Decisions](decisions.md) → [delivery gates](delivery-plan.md) |

## Authority map

| Document | Owns | Primary accountable role |
| --- | --- | --- |
| [Product scope](product-scope.md) | Problem, actors, MVP, non-goals, success measures | Product owner |
| [Architecture](architecture.md) | Components, trust boundaries, flow, invariants, lifecycle | Architecture lead |
| [Data and proof model](data-and-proof-model.md) | Units, canonical encoding, witness/public inputs, circuit semantics | Cryptography lead |
| [Claim envelope](claim-envelope.md) | Public wire contract, disclosure rules, proof/receipt references, verifier outcomes | Cryptography lead |
| [Security and privacy](security-and-privacy.md) | Assets, trust assumptions, threats, controls, data handling, safety boundary | Security lead |
| [Delivery plan](delivery-plan.md) | Next-milestone entry, workstream, evidence, and exit rules; phases, dependencies, acceptance, and definition of done | Delivery lead |
| [Testing and operations](testing-and-operations.md) | Test layers, benchmarks, observability, deployment/readiness gates | Service owner/SRE |
| [Commercial model](commercial-model.md) | Open-core boundary, optional managed capabilities, and edition compatibility | Product owner |
| [Discovery research plan](discovery-research-plan.md) | Privacy-gated interview protocol, evidence handling, and evidence-to-decision rules | Product owner |
| [Decision register](decisions.md) | Decision state, ADR process, accountable deciders | Architecture lead |

## Maintenance rules

- Update the owning document and cross-link; do not copy its detailed requirements elsewhere.
- Use the component names and lifecycle states defined by architecture and the trust terms and units defined by the data model.
- Record a genuinely resolved, consequential choice as an ADR. Do not manufacture ADRs for open questions.
- A pull request changing a normative requirement identifies its owner, validation evidence, affected gates, and decision status.
- Repository-relative links and fenced JSON must be validated with every documentation change.

## Acceptance

This documentation system is acceptable when every authoritative topic is reachable from this page, no active page points to the superseded plan as authority, relative links resolve, and status language does not imply an implementation exists.
