# 🚀 Mira's DevOps Bootcamp — v2.0 (Pareto / Interview-First)

A strict, evidence-only, AI-taught AWS + DevOps bootcamp. One student (Visakan), one teacher (Mira — a Hermes Agent profile), one goal: **clear any interview loop for a 1–2 year experienced DevOps Engineer role in the Chennai market, in the shortest defensible time.**

> Built on Learn → Do → Prove → Defend → **Recall**, powered by Anki spaced repetition, an Obsidian vault, a NotebookLM study notebook, and a live GitHub Pages progress dashboard.
>
> **v2.0 principle:** we go deep only where interviewers actually go deep. Everything else is *awareness* — explainable in two sentences, no lab hours. See [What we cut and demoted](ROADMAP.md#3-what-we-cut-and-demoted-explicit--no-silent-drops-rule-3).
> **v2.0 pacing:** 25–30 hrs/week → **~7 weeks**. 30+ → ~5.5 weeks. 20 → ~9 weeks.

## The system (v2.0)

| Component | What it does | Where |
|---|---|---|
| 📋 **ROADMAP.md** | Curriculum v2.0 — 8 phases, 🔴/🟡/⚪ tiers, checkbox-per-topic. Current module = first unchecked box | `ROADMAP.md` |
| 🎤 **INTERVIEW-DRILLS.md** | **122 scenario questions** — the bank that decides the offer. Answered cold, out loud, twice | `INTERVIEW-DRILLS.md` |
| ⚖️ **RULES.md** | The contract between Mira and Visakan (14 rules) | `RULES.md` |
| 🧭 **STATUS.txt** | Live resume pointer — current module, next action. Updated after every topic | `STATUS.txt` |
| 📊 **PROGRESS.md** | Session log + status table (scores, dates) | `PROGRESS.md` |
| 🃏 **question-bank.md** | Missed-question queue (mirrored in Anki `mira::missed`) | `question-bank.md` |
| 📓 **journal/** | Daily evidence log — every session must end here or it didn't count | `journal/YYYY-MM-DD.md` |
| 🗂️ **Anki** | Phase 0 = daily due-card review · Phase 5 = 5+ cards per completed topic | Anki + AnkiConnect + Anki MCP |
| 🧠 **Obsidian vault** | Revision notes per topic, wikilinked hub. No note = topic incomplete | `~/Documents/Obsidian/Mira Bootcamp` |
| 🤖 **NotebookLM** | Study partner for "why" questions (study material, never evidence) | notebooklm.google.com |
| 📈 **Dashboard** | Auto-built progress page (modules, %, Anki stats) → GitHub Pages | `docs/` → https://visakan-official.github.io/learning/ |
| 🔧 **scripts/build_dashboard.py** | Builds the dashboard (stdlib-only, OS-portable); run every session (Rule 14) | `scripts/` |

**Lab host:** Omarchy 4.0.2 (Arch-based Linux), user `vizack`, home `/home/vizack`. Repo `~/Ai-assisted-learning`.
No WSL, no VM. Package manager `pacman` (+ `yay`). AWS CLI v2 at `~/.local/bin/aws`, creds in `~/.aws` (600).

## Execution stages (the real order)

| Stage | Weeks | Content | Exit proof |
|---|---|---|---|
| **A** Interview floor | 1 | Linux core · networking trim · Git · Docker fundamentals | Move around a box, explain DNS/HTTP/LB, branch+PR, build+run a container |
| **B** Cloud + containers | 2–4 | AWS core (IAM→CW) + Docker deep/Compose + Terraform core | **P1 + P2 shipped** |
| **C** Orchestration + pipelines | 4–6 | K8s core/intermediate, Helm, CI/CD (GH Actions + Jenkins) | Pod on K3s, both pipelines green |
| **D** IaC depth + flagship | 6–7 | Terraform state, ⚪ Ansible/CFN/GitOps | **P3 shipped** |
| **E** Ops polish + interview bootcamp | 7–8 | Observability, security/cost, expanded Phase 7 | 122 drills answered, 3 project stories, 2 mocks passed |

## Session flow (mandatory)

1. **Phase 0 — Anki review:** due cards first. No new material until they're done.
2. **Resume:** Mira reads `STATUS.txt` — the files are the memory, never the chat.
3. **Learn → Do → Prove → Defend** on the current module (teach *before* testing — always).
4. **Phase 5 — Recall:** pass → 5+ Anki cards + Obsidian note.
5. **Phase 6 — Destroy:** terminate ALL lab resources (except the production `t3.small`).
6. **Close:** journal entry + dashboard rebuild + commit + push (Rule 14).
7. **Interview spine (v2.0):** every module adds its questions to `INTERVIEW-DRILLS.md` practice; Phase 7 is drilled continuously, not saved for the end.

## The 3 portfolio projects

| # | Project | Stack | Ships | Interview value |
|---|---|---|---|---|
| P1 | Static site, prod-grade | S3 + CloudFront + Route 53 + ACM + GH Actions | End Stage B | DNS/CDN/IAM/OIDC + pipeline + cost story |
| P2 | Dockerized 3-tier app | Docker + Compose + ECR + EC2 + **Jenkins** | End Stage C | Multi-container, volumes, healthchecks, image pipeline, rollback |
| P3 | AWS infra as code + K8s + monitoring | **Terraform** + VPC/ALB/ASG/RDS + K3s + Helm + Prometheus/Grafana + blue-green | End Stage D | Everything a 1–2 yr JD lists, in one repo |

---

*Adapted from a friend's bootcamp kit (v1.2.0) → v1.3.0 (Anki SRS, Obsidian↔Anki, NotebookLM, dashboard) → v1.4.0 (host migrated Windows → Omarchy/Arch; dashboard script OS-portable + stdlib-only) → **v2.0 (2026-09-13): Pareto restructure for the Chennai 1–2 yr DevOps market** — serial phases parallelised, non-interview topics demoted to awareness, Phase 7 expanded, new `INTERVIEW-DRILLS.md` bank.*
