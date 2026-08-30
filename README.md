# MAVLink ZKP Proxy

> **Current maturity: documentation only.** This repository contains no working proxy, proof circuit, Midnight contract, dashboard, or deployment.

MAVLink ZKP Proxy is a proposed observational gateway that turns selected MAVLink telemetry into narrowly defined, privacy-preserving claims. The initial claim is that a simulated vehicle's horizontal speed is at or below a policy limit, without disclosing exact position.

Zero-knowledge proofs can limit disclosure; they do not prove that telemetry reflects physical reality. Chain inclusion does not authenticate an off-chain sensor reading. Source authentication, replay controls, trustworthy time, and vehicle integrity remain separate concerns.

## Product positioning

MAVLink ZKP Proxy is positioned as a **privacy-preserving telemetry attestation gateway**: it accepts eligible telemetry, preserves and evaluates its declared trust context, and produces narrowly scoped evidence that a private telemetry value satisfies a public policy without publishing the underlying sensitive data. MAVLink is the first telemetry adapter, not the product boundary, and bounded speed is the first claim type, not a commitment to a single-purpose proof system.

A ledger, when used, is an optional publication or timestamp boundary for approved proof metadata. It is not the source of truth for telemetry, vehicle state, or proof validity; verification and the explicitly modeled source-trust boundary remain authoritative for those questions.

The product is **not**:

- a MAVLink router or general protocol-forwarding service;
- a telemetry archive, flight-log store, or historical analytics platform;
- a flight controller or other navigation and vehicle-control component;
- a command-authority system or a mechanism for approving, issuing, or relaying commands;
- an anonymous tracking service for vehicles, operators, or missions; or
- a general-purpose blockchain bridge for arbitrary messages, assets, or cross-chain activity.

The repository and product names are branding decisions separate from this positioning. Any rename requires an explicit branding decision and coordinated migration; terminology must not be silently changed as though a rename were part of the product scope.

## Proposed MVP target

The deterministic, single-vehicle SITL vertical slice below is the eventual proposed MVP target after the [**Validated claim and verifier contract**](docs/delivery-plan.md#next-milestone--validated-claim-and-verifier-contract) milestone passes its stop/go review; it is not presently authorized implementation work.

Until that review passes, current work is limited to documentation reconciliation, governed discovery, conspicuously labelled non-cryptographic UX research, and disposable proof-system-neutral format/vector spikes. Telemetry parsing, a circuit, real proof verification, and publication are not presently authorized.

1. ingest MAVLink 2 traffic over local UDP and preserve its trust state;
2. normalize the required `GLOBAL_POSITION_INT` and `VFR_HUD` fields;
3. create and independently verify one bounded-speed proof;
4. record approved proof metadata through a deterministic mock chain adapter;
5. show redacted lifecycle state; and
6. replay the scenario in CI from synthetic fixtures.

This MVP is observational. It has no vehicle command path and makes no flight-control, collision-avoidance, safety-critical, scalability, availability, or real-time claim.

## Proposed architecture

```text
single SITL vehicle -> MAVLink bridge -> proof worker -> verifier
                            |                              |
                            +------ redacted status ------+-> mock chain adapter
```

Components are proposed boundaries, not deployed services. Development begins with a modular process or small workspace; external SDKs remain behind adapters. Technology candidates require evidence and an accepted architecture decision record (ADR) before becoming settled choices.

## Start here

The [documentation index](docs/README.md) provides audience-specific reading paths and explains document authority. The named next milestone is [**Validated claim and verifier contract**](docs/delivery-plan.md#next-milestone--validated-claim-and-verifier-contract). `docs/delivery-plan.md` owns that milestone's entry conditions, workstream, required evidence, and exit rules. This is a planning milestone in a documentation-only repository; it does not imply that a prototype has been implemented.

Choose the shortest path for your reason for visiting:

| Audience | Start with | Then read |
| --- | --- | --- |
| First-time visitor or contributor | [Product scope](docs/product-scope.md) | [Architecture](docs/architecture.md) and [delivery plan](docs/delivery-plan.md) |
| Potential customer, partner, or other third party | [Product scope](docs/product-scope.md) | [Commercial model](docs/commercial-model.md), [claim envelope](docs/claim-envelope.md), and [security and privacy](docs/security-and-privacy.md) |
| Manager or decision maker | [Delivery plan](docs/delivery-plan.md) | [Management coordination](docs/management/README.md) and [decision register](docs/decisions.md) |
| Engineer or technical reviewer | [Architecture](docs/architecture.md) | [Data and proof model](docs/data-and-proof-model.md), [claim envelope](docs/claim-envelope.md), and [testing and operations](docs/testing-and-operations.md) |
| Product or discovery researcher | [Discovery research plan](docs/discovery-research-plan.md) | [Product scope](docs/product-scope.md), [commercial model](docs/commercial-model.md), and [decision register](docs/decisions.md) |

### Document directory

- [product scope](docs/product-scope.md) — MVP, deferred work, non-goals, and success measures;
- [architecture](docs/architecture.md) — boundaries, responsibilities, data flow, and failure behavior;
- [data and proof model](docs/data-and-proof-model.md) — telemetry units, encoding, and proof semantics;
- [claim envelope](docs/claim-envelope.md) — public wire contract, disclosure rules, and verifier outcomes;
- [security and privacy](docs/security-and-privacy.md) — trust assumptions, threats, controls, and safety boundary;
- [delivery plan](docs/delivery-plan.md) — the next milestone, phases, evidence, owners, and stop/go rules;
- [testing and operations](docs/testing-and-operations.md) — validation layers and readiness gates; and
- [commercial model](docs/commercial-model.md) — open capabilities, optional services, and anti-lock-in rules;
- [discovery research plan](docs/discovery-research-plan.md) — research protocol, privacy gate, and evidence rules;
- [decision register](docs/decisions.md) — proposed, open, deferred, and accepted decisions; and
- [management coordination](docs/management/README.md) — operational work-item status and external-tool mapping.

## Contributing during discovery

Useful contributions are reviews, synthetic fixtures, compatibility experiments, schema proposals, threat-model corrections, and evidence-backed ADRs. Do not describe proposed behavior as implemented. Code changes should update the relevant requirements, tests, and decision evidence.

## Safety and license

Use simulation and controlled test environments only. Do not connect an experimental build to a flight-critical command path. Hardware work requires the gates in the [delivery plan](docs/delivery-plan.md). This project uses the [MIT License](LICENSE).
