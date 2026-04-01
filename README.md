<div align="center">

# Artyom Pryanishnikov

**Engineering Leader & Full-Stack Architect**

Leading engineering at two companies — a startup building communication platforms and an established enterprise.
Background in both software engineering and business operations gives me a systems-level view of products.

17 merged PRs in Svelte, SvelteKit, Biome, OXC (235k+ combined stars).
Two production backends: 41K lines Go (ECS + Event Sourcing) and a B2B SaaS scoring 27K+ tenders with AI.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/frankfmy/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/FrankFMY)
[![Website](https://img.shields.io/badge/frankfmy.com-000?style=for-the-badge&logo=safari&logoColor=white)](https://frankfmy.com)

</div>

---

## What I Build

### BizEngine `Go` `41K LOC` `private`

Server engine for creating digital twins of businesses. Entity-Component-System architecture with Event Sourcing — every business object is an Entity with typed JSONB Components, every mutation produces an Event in an append-only log.

- **14 business modules** — Catalog, Warehouse, Orders, HR, Finance (double-entry accounting), Logistics (GPS tracking), CRM, Documents, Import, Webhooks
- **Process engine** — YAML-defined state machines for order fulfillment, stock replenishment, delivery tracking
- **Arcana integration** — reactive sync engine with 32 graph definitions, JSON Patch diffs, Centrifugo real-time delivery
- **3D space validation** — AABB collision detection for spatial layouts
- Double-entry bookkeeping (int64 kopeks, РСБУ chart of accounts), Russian tax/EDO/labeling integration stubs

Stack: Go 1.24, Chi, PostgreSQL 16, Redis, Centrifugo v6, MinIO

### FrankFMY CRM [`crm.frankfmy.com`](https://crm.frankfmy.com) `TypeScript` `private`

B2B SaaS for Russian government procurement — sole engineer, production with paying customers.

- **27K+ tenders** parsed from zakupki.gov.ru, scoring engine with morphological stemming, OKPD2 matching, log-weighted keyword normalization
- **AI document analysis** — PDF/DOCX extraction, per-template keyword scoring in technical specifications
- **Real-time notifications** — SSE in-app + Web Push + Telegram bot + email digest
- **Security** — httpOnly cookie auth, CSP/HSTS, CSRF double-submit, bcrypt + session revocation

Stack: Bun + Elysia, SvelteKit + Svelte 5, PostgreSQL + Drizzle ORM, Redis, Caddy

---

## Open Source

| Project | Stars | Merged | What I worked on |
|---------|-------|--------|-----------------|
| **[Svelte](https://github.com/sveltejs/svelte)** | 86k+ | [7 PRs](https://github.com/sveltejs/svelte/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | Reactive store detection in block expressions, state preservation during invalidation |
| **[SvelteKit](https://github.com/sveltejs/kit)** | 20k+ | [5 PRs](https://github.com/sveltejs/kit/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | Remote function error handling, DX improvements |
| **[Bun](https://github.com/oven-sh/bun)** | 87k+ | [5 open](https://github.com/oven-sh/bun/pulls?q=is%3Apr+author%3AFrankFMY) | Fetch API error messages, S3 client fixes |
| **[Biome](https://github.com/biomejs/biome)** | 23k+ | [3 PRs](https://github.com/biomejs/biome/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | Async generator rules, formatter directives |
| **[OXC](https://github.com/oxc-project/oxc)** | 19k+ | [2 PRs](https://github.com/oxc-project/oxc/pulls?q=is%3Apr+author%3AFrankFMY+is%3Amerged) | Diagnostic message improvements |

---

## Other Projects

| Project | What it does | Stack |
|---------|-------------|-------|
| **[Arcana](https://github.com/FrankFMY/Arcana)** | Reactive graph sync engine — real-time PostgreSQL-to-frontend with WebSocket and framework adapters | Go, PostgreSQL |
| **[Burrow](https://github.com/FrankFMY/burrow)** | Self-hosted VPN — VLESS+Reality, CDN fronting, Hysteria2, auto-fallback, split tunneling | Go, Svelte, Tauri |
| **[AURA](https://github.com/FrankFMY/AURA)** | Censorship-resistant messenger on Nostr protocol | TypeScript, Svelte |

---

## Stack

**Languages**

![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/-PHP-777BB4?style=flat-square&logo=php&logoColor=white)

**Frontend**

![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Svelte](https://img.shields.io/badge/-Svelte-FF3E00?style=flat-square&logo=svelte&logoColor=white)
![SvelteKit](https://img.shields.io/badge/-SvelteKit-FF3E00?style=flat-square&logo=svelte&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/-TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

**Backend**

![Bun](https://img.shields.io/badge/-Bun-000000?style=flat-square&logo=bun&logoColor=white)
![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![NestJS](https://img.shields.io/badge/-NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white)
![ElysiaJS](https://img.shields.io/badge/-ElysiaJS-7C3AED?style=flat-square&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Laravel](https://img.shields.io/badge/-Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![Chi](https://img.shields.io/badge/-Chi-00ADD8?style=flat-square&logo=go&logoColor=white)
![Fiber](https://img.shields.io/badge/-Fiber-00ADD8?style=flat-square&logo=go&logoColor=white)

**Data & Infrastructure**

![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Caddy](https://img.shields.io/badge/-Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white)
![Tauri](https://img.shields.io/badge/-Tauri-FFC131?style=flat-square&logo=tauri&logoColor=black)
![MinIO](https://img.shields.io/badge/-MinIO-C72E49?style=flat-square&logo=minio&logoColor=white)

---

<div align="center">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs?username=FrankFMY&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=6&theme=dracula&hide_border=true&cache_seconds=86400" height="150" alt="languages graph" />
  &nbsp;
  <img src="https://github-readme-streak-stats-eight.vercel.app?user=FrankFMY&locale=en&mode=daily&theme=dracula&hide_border=true&border_radius=5" height="150" alt="streak graph" />
</div>

<br>

<div align="center">
  <img src="https://raw.githubusercontent.com/FrankFMY/FrankFMY/output/snake.svg" alt="Snake animation" />
</div>
