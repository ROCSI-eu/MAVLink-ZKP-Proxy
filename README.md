# MAVLink ZKP Proxy

> **Status: architecture and discovery.** This repository currently contains design documentation only. It does not yet contain a working proxy, proof circuit, Midnight contract, dashboard, or deployment.

MAVLink ZKP Proxy is a proposed gateway for turning selected MAVLink telemetry into privacy-preserving claims. Instead of publishing precise telemetry to every consumer, the gateway is intended to prove narrowly defined statements—such as “the vehicle is inside an approved area” or “speed is below a limit”—and anchor auditable proof metadata through a Midnight integration.

The project is not an autopilot, flight controller, collision-avoidance system, or replacement for a ground-control station. Flight-critical decisions must remain in systems designed and certified for that purpose.

## The problem

Raw vehicle telemetry can expose location, vehicle identity, and mission details. Operators may nevertheless need to demonstrate compliance to another party. The proposed system separates:

- **private inputs**, such as exact position and vehicle identity;
- **public claims**, such as a policy identifier, time window, and pass/fail result; and
- **audit evidence**, such as a proof digest and transaction reference.

Zero-knowledge proofs reduce disclosure; they do not establish that a sensor reading is truthful. Source authentication, key provisioning, replay protection, and trust in the vehicle or attestation device are separate requirements.

## Intended first release

The first end-to-end milestone is deliberately narrow:

1. ingest signed or explicitly marked-untrusted MAVLink 2 traffic from one simulated vehicle;
2. normalize `GLOBAL_POSITION_INT` and `VFR_HUD` data into a versioned internal record;
3. generate and locally verify a proof that horizontal speed is below a configured threshold;
4. submit only proof metadata through a mocked Midnight adapter;
5. display proof state without exposing exact position; and
6. replay the flow deterministically in CI from a recorded fixture.

Chain deployment, multi-vehicle consensus, arbitrary polygon proofs, autonomous command execution, production Kubernetes, and real-aircraft testing are outside this milestone.

## Proposed architecture

```text
PX4/ArduPilot SITL
       |
       | MAVLink 2 over UDP (development only)
       v
MAVLink bridge --> policy/proof worker --> verifier --> Midnight adapter
       |                  |                   |              |
       +------------ event/audit API --------+--------------+
                              |
                         operator UI
```

The bridge terminates MAVLink transport and produces a canonical record. The proof worker evaluates a versioned policy and creates a proof. Verification is a distinct trust boundary. The Midnight adapter must be replaceable with a deterministic mock so development and CI do not depend on a live network. The operator API exposes redacted views by default.

See the [system architecture and delivery plan](docs/system-plan.md) for trust boundaries, schemas, technology decisions, security assumptions, milestones, and acceptance gates.

## Repository layout

```text
.
├── README.md             # Product intent and contributor entry point
├── docs/
│   └── system-plan.md    # Architecture, scope, decisions, and delivery plan
└── LICENSE
```

The target source layout is documented rather than pre-created so that the first implementation pull request can establish workspace tooling and ownership deliberately.

## Current decisions and open questions

| Area | Current direction | Status |
| --- | --- | --- |
| Core services | Rust workspace | Proposed; validate with a vertical slice |
| Development telemetry | ArduPilot or PX4 SITL over UDP | Proposed |
| Service contracts | Protobuf/gRPC internally; HTTP/WebSocket at the UI boundary | Proposed |
| Proof system | Benchmark candidates before selecting a proving system | Open |
| Midnight integration | Adapter plus deterministic mock first | Proposed; SDK/contract details require validation |
| Persistence | PostgreSQL metadata; object storage only when retention requires it | Deferred until after the vertical slice |

Open design decisions must be resolved with short architecture decision records (ADRs), including measured evidence where performance or compatibility drives the choice.

## Definition of done for the documentation phase

Documentation is ready to hand to implementation teams when:

- every phase has measurable entry and exit criteria;
- the canonical schema and public/private proof inputs are versioned and reviewed;
- the threat model identifies owners and mitigations for high-risk threats;
- proof-system and Midnight compatibility spikes are recorded as ADRs;
- privacy, retention, and key-management owners are named; and
- CI commands and supported tool versions are pinned in the implementation scaffold.

## Contributing now

At this stage, useful contributions are design reviews, threat-model corrections, small compatibility experiments, schema proposals, and ADRs. Please avoid presenting proposed behavior as implemented behavior. A change that adds code should include tests, operational documentation, and an update to the relevant decision or milestone.

## Safety and licensing

Use simulation and controlled test environments until the safety and security gates in the system plan are met. Do not connect an experimental build to a flight-critical command path. The project is available under the [MIT License](LICENSE).
