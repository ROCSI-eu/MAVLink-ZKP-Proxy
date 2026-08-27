# MAVLink ZKP Proxy

> **Current maturity: documentation only.** This repository contains no working proxy, proof circuit, Midnight contract, dashboard, or deployment.

MAVLink ZKP Proxy is a proposed observational gateway that turns selected MAVLink telemetry into narrowly defined, privacy-preserving claims. The initial claim is that a simulated vehicle's horizontal speed is at or below a policy limit, without disclosing exact position.

Zero-knowledge proofs can limit disclosure; they do not prove that telemetry reflects physical reality. Chain inclusion does not authenticate an off-chain sensor reading. Source authentication, replay controls, trustworthy time, and vehicle integrity remain separate concerns.

## Proposed first release

The first implementation target is one deterministic, single-vehicle SITL vertical slice:

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

The [documentation index](docs/README.md) provides audience-specific reading paths and explains document authority. Key references are:

- [product scope](docs/product-scope.md) — MVP, deferred work, non-goals, and success measures;
- [architecture](docs/architecture.md) — boundaries, responsibilities, data flow, and failure behavior;
- [data and proof model](docs/data-and-proof-model.md) — telemetry units, encoding, and proof semantics;
- [security and privacy](docs/security-and-privacy.md) — trust assumptions, threats, controls, and safety boundary;
- [delivery plan](docs/delivery-plan.md) — phases, evidence, owners, and the next implementation step;
- [testing and operations](docs/testing-and-operations.md) — validation layers and readiness gates; and
- [decision register](docs/decisions.md) — proposed, open, deferred, and accepted decisions.

## Contributing during discovery

Useful contributions are reviews, synthetic fixtures, compatibility experiments, schema proposals, threat-model corrections, and evidence-backed ADRs. Do not describe proposed behavior as implemented. Code changes should update the relevant requirements, tests, and decision evidence.

## Safety and license

Use simulation and controlled test environments only. Do not connect an experimental build to a flight-critical command path. Hardware work requires the gates in the [delivery plan](docs/delivery-plan.md). This project uses the [MIT License](LICENSE).
