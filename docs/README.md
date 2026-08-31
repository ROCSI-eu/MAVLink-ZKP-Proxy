# Documentation guide

| Metadata | Value |
| --- | --- |
| Status | Current documentation governance; system content remains Proposed/Open/Deferred as marked |
| Audience | All contributors and reviewers |
| Accountable role | Architecture lead |
| Review trigger | Any document addition, status change, or ownership-model change |

## Purpose

This index is the navigation and authority map for a documentation-only project. It separates topics whose audiences, owners, and change cadences differ; the former [system plan](system-plan.md) is Superseded and is not an alternative baseline.

The [current work authorization](current-work-authorization.md) owns the conservative activity boundary while `M1` entry remains unsatisfied. It permits bounded recruitment outreach through public professional channels under its lightweight policy only after the required minimum privacy arrangement is approved; the Proposed [pre-M1 participant readiness pack](pre-m1-participant-readiness.md) supplies the approved bounded message and stop conditions but does not satisfy a gate. For operational work-item status and external-tool mapping, see the non-normative [management coordination index](management/README.md). The [solo planning readiness record](reviews/validated-claim-contract/solo-planning-readiness-record.md) records the Current factual operating context and the resulting milestone hold.

## Status and authority

Every substantive document declares its purpose, audience, status, accountable role, review trigger, authority, related documents, validation method, and open decisions.

- **Current** — demonstrably true of this repository or an active documentation rule.
- **Proposed** — intended but unimplemented or unaccepted.
- **Open** — unresolved and blocking.
- **Deferred** — outside the current phase.
- **Superseded** — traceability only; no longer authoritative.

`MUST`, `MUST NOT`, and **Required** identify normative constraints for the proposed MVP. Examples, text diagrams, candidate technologies, and proposed layouts are illustrative unless explicitly marked normative. An accepted ADR supersedes a conflicting proposal; scope changes also require product approval and synchronized document updates.

Roles identify required accountability until named people are assigned. A role label, placeholder, sole-maintainer acknowledgement, or AI-assisted review does not satisfy a milestone requirement for a real accountable person, independent reviewer, or relying-party decision owner. Review triggers are used instead of arbitrary review dates. Evidence should be linked from an ADR or milestone record when those artifacts exist.

## Reading paths

All root reading paths lead to the named next milestone, [**Validated claim and verifier contract**](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract). The [delivery plan](delivery-plan.md) owns its entry conditions, workstream, required evidence, and exit rules; the [operational register](management/validated-claim-contract-register.csv) owns the Current coordination status.

The Current state is solo documentation planning with `M1` and `M2` blocked. The [current work authorization](current-work-authorization.md) defines what may be done before M1 entry, including lightweight public-channel outreach after approval of its minimum privacy arrangement, minimum recruitment information through the governed off-Git route, and an initial non-research suitability conversation; the [solo planning readiness record](reviews/validated-claim-contract/solo-planning-readiness-record.md) records why the broader boundary applies. Outreach stops before research interviews, workflow evidence, telemetry exchange, procurement claims, restricted data, or independent review and cannot be used as discovery, validation, or product evidence. No discovery execution, paper/non-cryptographic prototype research, format/vector spike, proof work, telemetry/SITL work, hardware work, publication, pilot, or production activity is authorized. Future phase permissions described in the delivery plan become available only after their accepted prerequisites and reviews are recorded.

| Reader | Recommended path |
| --- | --- |
| New contributor | Root [README](../README.md) → [current work authorization](current-work-authorization.md) → [product scope](product-scope.md) → [delivery plan](delivery-plan.md) |
| Prospective participant or future recruitment coordinator | [Current work authorization](current-work-authorization.md) → [pre-M1 participant readiness pack](pre-m1-participant-readiness.md) → [delivery plan](delivery-plan.md) |
| Product or safety | [Current work authorization](current-work-authorization.md) → [product scope](product-scope.md) → [security and privacy](security-and-privacy.md) → [delivery plan](delivery-plan.md) |
| Commercial/product strategy | [Product scope](product-scope.md) → [commercial model](commercial-model.md) → [architecture](architecture.md) → [next milestone](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) |
| Discovery researcher | [Current work authorization](current-work-authorization.md) → [discovery research plan](discovery-research-plan.md) → [product scope](product-scope.md) → [decisions](decisions.md) → [next milestone](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) |
| Engineering/platform | [Current work authorization](current-work-authorization.md) → [architecture](architecture.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) → [next milestone](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) |
| Cryptography | [Current work authorization](current-work-authorization.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [security and privacy](security-and-privacy.md) → [decisions](decisions.md) → [next milestone](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) |
| Security/privacy | [Current work authorization](current-work-authorization.md) → [security and privacy](security-and-privacy.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) → [next milestone](delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) |
| Decision maker | [Current work authorization](current-work-authorization.md) → [decisions](decisions.md) → [delivery gates](delivery-plan.md) → [operational register](management/validated-claim-contract-register.csv) |

## Authority map

| Document | Owns | Primary accountable role |
| --- | --- | --- |
| [Current work authorization](current-work-authorization.md) | Work permitted while M1 entry remains unsatisfied and the transition boundary into M1 | Repository maintainer for factual maintenance; milestone roles remain unassigned |
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
| [Repository licensing policy](../LICENSING.md) | Effective license record and proposed path classification | Repository maintainer |
| [Dependency licensing policy](dependency-licensing-policy.md) | Dependency review and release-attribution gate | Architecture lead |

The current work authorization cannot amend, satisfy, or bypass a delivery-plan prerequisite. It controls only the narrower pre-M1 activity boundary. The pre-M1 participant readiness pack is Proposed supporting material, not an authority or participation record. The review records under `docs/reviews/` are evidence or traceability artifacts, not substitutes for the owning documents above. Their status must be read before relying on them.

## Maintenance rules

- Update the owning document and cross-link; do not copy its detailed requirements elsewhere.
- Use the component names and lifecycle states defined by architecture and the trust terms and units defined by the data model.
- Record a genuinely resolved, consequential choice as an ADR. Do not manufacture ADRs for open questions.
- A pull request changing a normative requirement identifies its owner, validation evidence, affected gates, and decision status.
- Any expansion of pre-M1 work must update the current work authorization and must not relax a delivery-plan gate without the required evidence and approval.
- Recruitment criteria and acknowledgement text remain Proposed. The outreach wording is usable only within the lightweight policy approved by the Current work authorization after its minimum privacy arrangement is approved; minimum recruitment information stays in the governed off-Git route, and any expanded contact or privacy handling requires separate approval.
- From a clean checkout, run `python3 scripts/check_docs.py` to validate repository-relative links, anchors, and fenced JSON. This is the authoritative documentation validation command.
- Licensing changes must update the root [licensing policy](../LICENSING.md), applicable ADR, decision register, README language, and mechanical mappings together. A Proposed mapping does not change the root `LICENSE`.

## Acceptance

This documentation system is acceptable when every authoritative topic is reachable from this page, no active page points to the superseded plan as authority, relative links resolve, and status language does not imply an implementation or authorization that does not exist.
