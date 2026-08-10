# 🚀 Mira's DevOps Bootcamp — v1.3.0

A strict, evidence-only, AI-taught AWS + DevOps bootcamp. One student (Visakan), one teacher (Mira — a Hermes Agent profile), one goal: **interview-ready for 1–2 year experienced DevOps Engineer roles.**

> Built on the Learn → Do → Prove → Defend → **Recall** method, powered by Anki spaced repetition, an Obsidian knowledge vault, a NotebookLM study notebook, and a live GitHub Pages progress dashboard.

## The system (v1.3.0)

| Component | What it does | Where |
|---|---|---|
| 📋 **ROADMAP.md** | The full curriculum — 8 phases, checkbox-per-topic. Current module = first unchecked box | `ROADMAP.md` |
| ⚖️ **RULES.md** | The contract between Mira and Visakan. Read it. Accept it. | `RULES.md` |
| 🧭 **STATUS.txt** | Live resume pointer — current module, next action. Updated after every topic | `STATUS.txt` |
| 📊 **PROGRESS.md** | Session log + status table (scores, dates) | `PROGRESS.md` |
| 🃏 **question-bank.md** | Missed-question queue (spaced repetition — mirrored in Anki) | `question-bank.md` |
| 📓 **journal/** | Daily evidence log — every session must end here or it didn't count | `journal/YYYY-MM-DD.md` |
| 🗂️ **Anki** | Flashcard SRS: Phase 0 = daily due-card review; Phase 5 = cards created for every completed topic | Anki desktop (AnkiConnect + Anki MCP add-on) |
| 🧠 **Obsidian vault** | Revision notes per topic, wikilinked hub. No note = topic incomplete | `A:\Obsidian\Mira Bootcamp` |
| 🤖 **NotebookLM** | AI study partner — ask it the "why" questions, feed it RESOURCES + notes | notebooklm.google.com |
| 📈 **Dashboard** | Auto-built progress page (modules, %, Anki stats) → GitHub Pages | `docs/` → https://visakan-official.github.io/learning/ |
| 🔧 **scripts/build_dashboard.py** | Builds the dashboard; run at the end of EVERY session (Rule 14) | `scripts/` |

## Session flow (mandatory)

1. **Phase 0 — Anki review:** due cards first. No new material until they're done.
2. **Resume:** Mira reads `STATUS.txt` — the files are the memory, never the chat.
3. **Learn → Do → Prove → Defend** (current module = first unchecked box in ROADMAP).
4. **Phase 5 — Recall:** pass the topic → create 5+ Anki flashcards + Obsidian note.
5. **Phase 6 — Destroy:** terminate ALL lab resources. Billing alarm is Day-0-mandatory.
6. **Close:** journal entry + run the dashboard script + git commit + push (Rule 14).

## The 4 portfolio projects

| # | Project | Tech | When |
|---|---|---|---|
| P1 | Static site: S3 + CloudFront + Route53 + CI/CD | AWS, GH Actions | End Phase 1 |
| P2 | Full-stack app dockerized + ECR pipeline | Docker, Compose, ECR | End Phase 2 |
| P3 | 3-tier app on AWS, 100% Terraform | Terraform, AWS | End Phase 3 |
| P4 | Full CI/CD + GitOps (OIDC → ECR → ArgoCD) | GH Actions, ArgoCD, EKS/ECS | End Phase 4 |

---

*Curriculum structure adapted from a friend's bootcamp kit (v1.2.0), upgraded to v1.3.0 with Anki SRS, Obsidian↔Anki bridge, NotebookLM, and the live dashboard.*
