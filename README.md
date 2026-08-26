<div align="center">

# Artem Prianishnikov

**Senior Backend / Platform Engineer**

TypeScript · Node.js · Go · Python · PostgreSQL

Building reliable product and platform systems from ambiguous requirements to verified production.

[Website](https://frankfmy.com) · [LinkedIn](https://www.linkedin.com/in/frankfmy/) · [Telegram](https://t.me/FrankFMY) · [Email](mailto:pryanishnikovartem@gmail.com) · [X](https://x.com/FrankFMY)

</div>

---

## What I do

I design and ship backend-heavy product systems: data models, APIs, integrations, background workflows, authentication and authorization, testing, deployment, observability, and incident recovery. I can deliver the complete product vertical with React/Next.js or SvelteKit, while my strongest work is in backend architecture, data integrity, and production reliability.

Recent work spans multi-tenant B2B SaaS, procurement workflows, industrial telemetry, collaborative business software, secure messaging, developer tooling, and deterministic financial analytics.

I work evidence-first: explicit invariants, transaction and concurrency boundaries, test-driven changes, exact artifact identity, fresh-clone verification, and rollback-aware production delivery.

## Selected engineering work

| System | Scope | Engineering signal |
|---|---|---|
| [**AURA**](https://github.com/FrankFMY/AURA) | Privacy-first browser-based Nostr messenger with encrypted one-to-one messaging, signed invitations, Passkey/PRF identity custody, device linking, relay replay, and durable inbox/outbox persistence | Solo-built and released with explicit custody and delivery semantics, fail-closed boundaries, unit tests, and browser E2E coverage |
| [**TenderHQ**](https://tenderhq.ru) | Multi-tenant procurement product with ingestion, scoring, CRM, AI document workflows, background jobs, auth, and operations tooling | Reduced pending queue work by more than 90% by restoring a missing domain invariant; hardened tenant isolation across secondary lookups and document paths |
| **Industrial telemetry platform** | Read-only upper software/data contour around MQTT, PostgreSQL/TimescaleDB, alerts, APIs, and operational workflows | Batched persistence, WAL-based crash recovery, deduplication, bounded time-series queries, health checks, and exact-artifact delivery |
| **Collaborative business platform** | Backend and integration boundaries for versioned, synchronized business workflows | Integrated a canonical visual editor through explicit adapters and contract tests, migrated active consumers, and removed the legacy compatibility path after parity proof |

## Selected public code

| Repository | Engineering focus |
|---|---|
| [**AURA**](https://github.com/FrankFMY/AURA) | TypeScript, secure stateful workflows, WebAuthn custody, Nostr protocol integration, durable browser storage, Vitest, and Playwright |
| [**service-slo-watchdog**](https://github.com/FrankFMY/service-slo-watchdog) | Dependency-free Python SLO probes, bounded HTTP transport, atomic alert/recovery state, corruption recovery, and deduplicated transitions |
| [**exact-source-audit**](https://github.com/FrankFMY/exact-source-audit) | Exact Git-index secret scanning and deterministic CycloneDX SBOM generation without dereferencing worktree symlinks or printing secret values |
| [**git-activity-analysis-core**](https://github.com/FrankFMY/git-activity-analysis-core) | Privacy-aware local Git scanning, deterministic repository analytics, Conventional Commit classification, and resource-bounded clustering |
| [**order-risk-engine**](https://github.com/FrankFMY/order-risk-engine) | Decimal-only, exchange-neutral pre-trade sizing with explicit notional, risk, leverage, quantity-step, and portfolio limits |
| [**fifo-cost-basis**](https://github.com/FrankFMY/fifo-cost-basis) | Decimal FIFO lot matching, proportional fee allocation, realized PnL, open lots, partial coverage, and explicit quality flags |
| [**schema-evolution-planner**](https://github.com/FrankFMY/schema-evolution-planner) | Deterministic flat-schema evolution plans with injected type compatibility, stable fingerprints, and explicit migration resolutions |
| [**canvas-geometry**](https://github.com/FrankFMY/canvas-geometry) | Low-level 2D geometry, collision semantics, spatial indexing, Canvas rendering, and deterministic server animation backed by 1,627 behavior tests |
| [**modbus-edge-agent**](https://github.com/FrankFMY/modbus-edge-agent) | Python, read-only Modbus RTU, semantic register decoding, synthetic provenance, credential-free durable buffering, MQTT QoS 1, and hardened systemd packaging |
| [**deterministic-sphere-network**](https://github.com/FrankFMY/deterministic-sphere-network) | Seeded Fibonacci-sphere geometry, bounded-degree proximity graphs, strict numeric guards, and GPU-ready typed buffers |
| [**totp-recovery-kit**](https://github.com/FrankFMY/totp-recovery-kit) | RFC 6238 vectors, replay-step authority, identity-bound AES-256-GCM TOTP envelopes, and Argon2id hash-only recovery codes |
| [**connector-contracts**](https://github.com/FrankFMY/connector-contracts) | Strict versioned connector manifests, bounded event envelopes, prototype-safe payload validation, and domain-separated signature bytes |

Additional focused libraries: [canonical-json-fingerprint](https://github.com/FrankFMY/canonical-json-fingerprint), [typed-unit-system](https://github.com/FrankFMY/typed-unit-system), and [async-control](https://github.com/FrankFMY/async-control). Broader toolkits: [ru-procurement-toolkit](https://github.com/FrankFMY/ru-procurement-toolkit) and [fmy-stack](https://github.com/FrankFMY/fmy-stack).

The focused repositories use explicit licenses and security boundaries, hosted CI across supported runtimes, versioned release artifacts, and fresh-clone/package verification.

## Open source

**18 merged pull requests** across Svelte, SvelteKit, Biome, and OXC.

| Project | Merged work |
|---|---:|
| [Svelte](https://github.com/sveltejs/svelte/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | 7 PRs: compiler/runtime fixes, accessibility behavior, migration docs, and test maintenance |
| [SvelteKit](https://github.com/sveltejs/kit/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | 6 PRs: precompression, navigation types, history API compatibility, warning behavior, and docs |
| [Biome](https://github.com/biomejs/biome/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | 3 PRs: TypeScript-aware lint fixes, import cleanup correctness, and async-generator handling |
| [OXC](https://github.com/oxc-project/oxc/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | 2 PRs: actionable diagnostics and formatter-directive handling |

## Core stack

<p>
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white">
  <img alt="Go" src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="NestJS" src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white">
  <img alt="Express" src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white">
  <img alt="React" src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB">
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white">
  <img alt="Redis" src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">
</p>

## Work

Open to Senior Backend / Platform Engineer, Product Engineer, Tech Lead, and hands-on engineering leadership opportunities. Remote contract or full-time.
