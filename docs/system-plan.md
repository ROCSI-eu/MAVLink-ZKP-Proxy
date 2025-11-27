# System Architecture and Integration Plan

## Components and Primary Stacks
- **MAVLink client/bridge**: Rust with `mavlink` crate for robust parsing and asynchronous telemetry; Python fallback via `pymavlink` for rapid prototyping and SITL tooling.
- **ZKP prover/verifier service**: Rust using `arkworks` ecosystem (e.g., `ark-groth16`, `ark-ed-on-bls12-381`) for performance and no-std options; circuit authoring assisted by `circom` for quick iterations where Rust DSL is insufficient.
- **Midnight connector**: Rust (matching Midnight SDK) exposing bindings to submit proofs/transactions and subscribe to consensus events.
- **Operator dashboard**: TypeScript/React with Vite, consuming WebSocket streams for live telemetry and REST/gRPC for control/status.

## Data Schemas
- **Canonical MAVLink payload for proofs (JSON for transport)**:
  ```json
  {
    "msg_id": 30,
    "frame": {
      "lat": 513456789,    // 1e-7 deg
      "lon": -113456789,   // 1e-7 deg
      "alt": 54500,        // millimeters
      "vx": 120,           // cm/s
      "vy": -35,
      "vz": 5,
      "timestamp_ms": 1712345678
    },
    "airframe_id": "uav-23",
    "mission_hash": "0xabc123..."
  }
  ```
- **Fields covered by ZKP**: kinematic tuple `(lat, lon, alt, vx, vy, vz, timestamp_ms)` committed in a Merkle leaf; `mission_hash` binds telemetry to the active plan.
- **Anonymized/hashed fields**: `airframe_id` stored as Poseidon hash; optional operator ID and geofence ID salted+hashed; location bucketed to 100 m grid for dashboard display while proof attests to fine-grained bounds.
- **Proof statements (examples)**:
  - Position lies within authorized geofence polygon.
  - Velocity below safety envelope.
  - Telemetry attested within last Δt (recency proof using timestamp commitment).

## Libraries and SDK Choices
- **MAVLink**:
  - *Rust `mavlink` crate*: strong typing, async streams; requires generated message set from XML.
  - *Python `pymavlink`*: broad tool support (SITL, log replay); slower and GIL-bound.
  - *Interface*: bridge publishes normalized JSON over WebSocket/gRPC to prover service.
- **ZKP**:
  - *Arkworks*: performant Rust circuits and Groth16/Plonkish backends; steeper learning curve.
  - *Circom + snarkjs*: fast prototyping and auditor familiarity; introduces Node dependency and Rust↔FFI boundary.
  - *Interface*: prover REST/gRPC endpoints `POST /proofs/geofence`, `POST /proofs/velocity` returning proof bytes + public signals; verifier library embedded in Midnight connector.
- **Midnight**:
  - *Midnight Rust SDK*: first-class chain integration, proof submission, and event subscriptions; early-stage APIs may change.
  - *Alternative*: gRPC/REST gateway to node for language-agnostic use; adds latency and extra ops surface.

## Inter-Service Interfaces
- **Telemetry ingress**: WebSocket (binary MAVLink) from GCS/UAV → Rust bridge; bridge also exposes gRPC `StreamTelemetry` returning normalized frames.
- **Proof generation**: gRPC with unary RPCs for batch proofs and server-streaming for progress; REST mirror for simple clients.
- **Consensus submission**: Midnight connector offers gRPC `SubmitProof` and `WatchTx` streams; publishes events to message bus (NATS) for dashboard updates.
- **Dashboard APIs**: REST for historical queries, WebSocket for live telemetry/proof status; JWT-based auth with short-lived tokens.

## Persistence and Logging
- **Persistence**: PostgreSQL for telemetry summaries and proof metadata; object storage (S3-compatible) for raw logs and proof artifacts; Redis for pub/sub and caching recent frames.
- **Logging/Tracing**: OpenTelemetry (otlp) with structured fields: `uav_id`, `mission_hash`, `msg_id`, `proof_type`, `tx_hash`.
- **Audit trail**: Append-only proof submission log (JSON Lines) rotated daily; chain transaction IDs mirrored into database for correlation.

## Deployment Outline
- **Development**:
  - Run SITL (e.g., ArduPilot `sim_vehicle.py` or PX4 `px4_sitl`) feeding UDP to MAVLink bridge.
  - Docker Compose with services: mavlink-bridge (Rust), prover (Rust), dashboard (Vite dev server), Midnight connector (mock if chain unavailable), Postgres, Redis, NATS.
  - Hot-reload for Rust via `cargo watch` and React via Vite.
- **Production**:
  - Container images per service (Distroless/Alpine for Rust, minimal Node runtime for dashboard build artifacts served by Nginx).
  - Kubernetes deployment with Helm charts; secrets in KMS-managed store; horizontal pod autoscaling on telemetry/Proof queue depth.
  - Observability stack (Prometheus, Loki/Tempo, Grafana) wired through OpenTelemetry exporters.
  - Midnight connectivity via managed node or in-cluster validator depending on SLA.

## Simulation and Testing Strategy
- **SITL** for functional flows (geofence breach, velocity envelope); recorded `.tlog` replay for regressions.
- **Property tests** on circuit constraints (Rust `proptest`); deterministic fixtures for proof verification.
- **Contract tests** for gRPC/REST schemas using Buf + Postman collections.
- **Load testing** with Locust/k6 on telemetry ingestion and proof generation queues.

## Containerization Baseline
- Base images: `rust:1.79-slim` for builders, scratch/distroless for release; `node:20-alpine` for dashboard build stage.
- Multi-stage Dockerfiles output minimal runtime layers; non-root user, read-only filesystem, seccomp/AppArmor profiles.
- Shared `.env.example` capturing ports, secrets, and chain endpoints; use `docker-compose.override.yml` for local tweaks.
