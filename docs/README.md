# Documentation guide

| Metadata | Value |
| --- | --- |
| Status | Current documentation governance; system content remains Proposed/Open/Deferred as marked |
| Audience | All contributors and reviewers |
| Accountable role | Architecture lead |
| Review trigger | Any document addition, status change, or ownership-model change |

## Purpose

This index is the navigation and authority map for a documentation-led project that also permits isolated, disposable sandbox artifacts. It separates topics whose audiences, owners, and change cadences differ; the former [system plan](system-plan.md) is Superseded and is not an alternative baseline. Sandbox artifacts are not supported implementation and remain governed by the authorization and promotion rules below.

The [current work authorization](current-work-authorization.md) owns the activity boundary for solo-concept work and transitions into higher-consequence uses. The [delivery plan](delivery-plan.md#exploration-boundary) owns exploration categories, mandatory markings, isolation rules, and separate promotion gates. It also permits bounded recruitment outreach under its stated privacy controls. Supporting readiness and management records do not satisfy a gate.

## Status and authority

Every substantive document declares its purpose, audience, status, accountable role, review trigger, authority, related documents, validation method, and open decisions.

- **Current** — demonstrably true of this repository or an active documentation rule.
- **Proposed** — intended but unimplemented or unaccepted.
- **Open** — an unresolved hypothesis, question, or decision. `Open` does not stop unrelated work; the applicable promotion decision fails closed until it is resolved.
- **Deferred** — outside the current phase.
- **Superseded** — traceability only; no longer authoritative.

`MUST`, `MUST NOT`, and **Required** identify normative constraints for the proposed MVP. Examples, text diagrams, candidate technologies, and proposed layouts are illustrative unless explicitly marked normative. An accepted ADR supersedes a conflicting proposal; scope changes also require product approval and synchronized document updates.

Roles identify required accountability until named people are assigned. A role label, placeholder, sole-maintainer acknowledgement, or AI-assisted review does not satisfy an artifact-promotion requirement for a real accountable person, independent reviewer, or relying-party decision owner. Review triggers are used instead of arbitrary review dates. Evidence should be linked from an ADR or milestone record when those artifacts exist.

### Orthogonal artifact labels

Document state describes prose and decisions, not artifact maturity. Every governed artifact or milestone record MUST state each label below; the values are independent and MUST NOT be collapsed into one maturity word.

| Dimension | Allowed labels | What the label answers |
| --- | --- | --- |
| **Artifact implementation state** | `Concept only`, `Experimental`, `Supported prototype`, `MVP component`, `Pilot component`, `Production component`, `Superseded` | What has actually been implemented and supported? `Experimental` is disposable and never means validated. |
| **Evidence source** | `No execution evidence`, `Synthetic evidence`, `SITL evidence`, `Participant evidence`, `Real-source test evidence`, `Operational evidence` | What kind of observation supports the scoped statement? List multiple sources rather than implying substitution. |
| **Review independence** | `Unreviewed`, `Maintainer-reviewed`, `Peer-reviewed`, `Independently reviewed` | Who reviewed it, and were they independent of its production? Named scope and conflicts are required for the last two labels. |
| **Data class** | `Public documentation`, `Synthetic data`, `Participant research data`, `Restricted/customer data`, `Operational data` | What is the most sensitive data the artifact is authorized to handle? This is a ceiling, not evidence that data was used. |
| **Permitted environment** | `Documentation-only`, `Local-only`, `Isolated test environment`, `Approved research environment`, `Authorized pilot`, `Authorized production` | Where may this exact version run or be used? Higher-consequence environments require their specific gate. |
| **External claim level** | `No external assurance claim`, `Externally observed finding`, `Independently verified technical claim`, `Authorized pilot claim`, `Authorized production claim` | What may be said outside the project about this exact version and scope? |

Use a slash-separated profile when brevity helps, for example: **`Experimental / Synthetic evidence / Maintainer-reviewed / Synthetic data / Local-only / No external assurance claim`**. Omitting a dimension is not an upgrade. `Exploration permitted` is the activity status for reversible solo work within its stated boundary. **`Blocked` is reserved for a named promotion or deployment decision that cannot proceed**, such as `Blocked — Gate B participant evaluation`; it MUST NOT describe the repository, an entire track, or an unresolved hypothesis.

### Allowed external claims

| External claim level | Claims allowed | Minimum corresponding evidence |
| --- | --- | --- |
| `No external assurance claim` | Factual description of the concept, experiment, inputs, method, and observed synthetic result, with limitations and mandatory labels. | Truthful provenance only; no validation or readiness adjective is allowed. |
| `Externally observed finding` | The precise workflow, comprehension, integration, or commercial finding observed by the named external audience. | Approved governance and scoped participant/external evidence; this does not establish security, safety, interoperability, or readiness. |
| `Independently verified technical claim` | Only the technical property independently reproduced for the named version, configuration, corpus, and environment. | Relevant execution evidence plus competent independent review; interoperability additionally requires the release corpus and independent implementations specified by the delivery plan. |
| `Authorized pilot claim` | That the named scope is authorized for the recorded pilot, with limitations and stop conditions. | Passed applicable gates, governed data, named owners, independent risk review, and explicit pilot authorization. |
| `Authorized production claim` | That the named scope is authorized for the recorded production environment and supported operating envelope. | Gate E production evidence and explicit production authorization; claims remain limited to measured and reviewed properties. |

An `Experimental` artifact MUST NOT be described as **validated, secure, safe, interoperable, customer-backed, or production-ready**. Each term requires direct corresponding evidence: approved external evaluation for “validated” or “customer-backed”; scoped independent security or safety evidence for “secure” or “safe”; released cross-implementation evidence for “interoperable”; and explicit Gate E authorization plus operational evidence for “production-ready.” Evidence in one dimension never upgrades another.

## Reading paths

All root reading paths lead to the five [parallel exploration tracks](delivery-plan.md#operating-model). The delivery plan owns artifact dependencies and promotion gates; the [artifact register](management/validated-claim-contract-register.csv) records the six independent artifact labels plus activity and contract state without imposing milestone sequencing.

The Current state permits solo, synthetic, reversible exploration across tracks within the documented boundary. No artifact is recorded as externally validated or approved for deployment. External evidence and named reviewers are required only for the applicable promotion or claim, not for unrelated exploration.

| Reader | Recommended path |
| --- | --- |
| New contributor | Root [README](../README.md) → [current work authorization](current-work-authorization.md) → [product scope](product-scope.md) → [delivery plan](delivery-plan.md) |
| Prospective participant or future recruitment coordinator | [Current work authorization](current-work-authorization.md) → [pre-M1 participant readiness pack](pre-m1-participant-readiness.md) → [delivery plan](delivery-plan.md) |
| Product or safety | [Current work authorization](current-work-authorization.md) → [product scope](product-scope.md) → [security and privacy](security-and-privacy.md) → [delivery plan](delivery-plan.md) |
| Commercial/product strategy | [Product scope](product-scope.md) → [commercial model](commercial-model.md) → [architecture](architecture.md) → [delivery plan](delivery-plan.md) |
| Discovery researcher | [Current work authorization](current-work-authorization.md) → [discovery research plan](discovery-research-plan.md) → [product scope](product-scope.md) → [decisions](decisions.md) → [delivery plan](delivery-plan.md) |
| Engineering/platform | [Current work authorization](current-work-authorization.md) → [architecture](architecture.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) → [delivery plan](delivery-plan.md) |
| Cryptography | [Current work authorization](current-work-authorization.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [security and privacy](security-and-privacy.md) → [decisions](decisions.md) → [delivery plan](delivery-plan.md) |
| Security/privacy | [Current work authorization](current-work-authorization.md) → [security and privacy](security-and-privacy.md) → [data and proof model](data-and-proof-model.md) → [claim envelope](claim-envelope.md) → [testing and operations](testing-and-operations.md) → [delivery plan](delivery-plan.md) |
| Decision maker | [Current work authorization](current-work-authorization.md) → [decisions](decisions.md) → [delivery gates](delivery-plan.md) → [operational register](management/validated-claim-contract-register.csv) |

## Authority map

| Document | Owns | Primary accountable role |
| --- | --- | --- |
| [Current work authorization](current-work-authorization.md) | Work permitted during solo-concept exploration and transitions into higher-consequence uses | Repository maintainer for factual maintenance; later-work roles remain risk-triggered |
| [Product scope](product-scope.md) | Problem, actors, MVP, non-goals, success measures | Product owner |
| [Architecture](architecture.md) | Components, trust boundaries, flow, invariants, lifecycle | Architecture lead |
| [Data and proof model](data-and-proof-model.md) | Units, canonical encoding, witness/public inputs, circuit semantics | Cryptography lead |
| [Claim envelope](claim-envelope.md) | Public wire contract, disclosure rules, proof/receipt references, verifier outcomes | Cryptography lead |
| [Security and privacy](security-and-privacy.md) | Assets, trust assumptions, threats, controls, data handling, safety boundary | Security lead |
| [Delivery plan](delivery-plan.md) | Parallel tracks, artifact dependencies, promotion gates, and MVP declaration | Delivery lead |
| [Testing and operations](testing-and-operations.md) | Test layers, benchmarks, observability, deployment/readiness gates | Service owner/SRE |
| [Commercial model](commercial-model.md) | Open-core boundary, optional managed capabilities, and edition compatibility | Product owner |
| [Discovery research plan](discovery-research-plan.md) | Privacy-gated interview protocol, evidence handling, and evidence-to-decision rules | Product owner |
| [Decision register](decisions.md) | Decision state, ADR process, accountable deciders | Architecture lead |
| [Repository licensing policy](../LICENSING.md) | Effective license record and proposed path classification | Repository maintainer |
| [Dependency licensing policy](dependency-licensing-policy.md) | Dependency review and release-attribution gate | Architecture lead |

The current work authorization cannot amend, satisfy, or bypass a delivery-plan promotion requirement. It controls only the narrower activity boundary. The pre-M1 participant readiness pack is Proposed supporting material, not an authority or participation record. The review records under `docs/reviews/` are evidence or traceability artifacts, not substitutes for the owning documents above. Their status must be read before relying on them.

## Maintenance rules

- Update the owning document and cross-link; do not copy its detailed requirements elsewhere.
- Use the component names and lifecycle states defined by architecture and the trust terms and units defined by the data model.
- Record a genuinely resolved, consequential choice as an ADR. Do not manufacture ADRs for open questions.
- A pull request changing a normative requirement identifies its owner, validation evidence, affected gates, and decision status.
- Any expansion of authorized work must update the current work authorization and must not relax a delivery-plan gate without the required evidence and approval.
- Recruitment criteria and acknowledgement text remain Proposed. The outreach wording is usable only within the lightweight policy approved by the Current work authorization after its minimum privacy arrangement is approved; minimum recruitment information stays in the governed off-Git route, and any expanded contact or privacy handling requires separate approval.
- From a clean checkout, run `python3 scripts/check_docs.py` to validate repository-relative links, anchors, and fenced JSON. This is the authoritative documentation validation command.
- Licensing changes must update the root [licensing policy](../LICENSING.md), applicable ADR, decision register, README language, and mechanical mappings together. A Proposed mapping does not change the root `LICENSE`.

## Acceptance

This documentation system is acceptable when every authoritative topic is reachable from this page, no active page points to the superseded plan as authority, relative links resolve, and status language does not imply an implementation or authorization that does not exist.
