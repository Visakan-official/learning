# PROGRESS — status table + session log

| Module | Score | Date | Anki cards | Obsidian note | Status |
|--------|-------|------|-----------|---------------|--------|
| M0.1 Linux Fundamentals | — | — | — | — | 🔴 not-started |
| Day 0 (setup) | n/a | 2026-08-11 | 7 (mira::0-foundations/day0) | ✅ Day 0 note | ✅ complete |
| Host migration (Windows → Omarchy/Arch) | n/a | 2026-09-13 | 7 (unchanged, all due) | ✅ vault verified | ✅ complete |

## Session log

| Date | Session | What happened | Next action |
|------|---------|---------------|-------------|
| 2026-08-11 | Day 0 | RULES accepted; WSL2+Ubuntu (user jeeni); IAM admin+Admins group+MFA+keys; AWS CLI; billing alarm chain (SNS+CloudWatch, test email ✓); gh auth (Visakan-official); 7 Anki cards; Obsidian note; constraint: t3.small = PRODUCTION, never touch | M0.1 Linux Fundamentals: filesystem + navigation + file ops |
| 2026-09-13 | Maintenance — host migration | Windows → **Omarchy 4.0.2 (Arch)**: repo copied to `~/Ai-assisted-learning` (NTFS `A:` original kept as fallback); vault → `~/Documents/Obsidian/Mira Bootcamp` (byte-identical); AWS CLI v2 installed to `~/.local` (no sudo) + creds migrated → `sts get-caller-identity` ✓ visakan-admin/139316821068; AnkiConnect :8765 ✓ + Anki MCP :3141 ✓ (**7 cards due, not yet reviewed**); dashboard script v1.4.0 (portable + stdlib-only) rebuilt ✓; live docs de-Windowsified (RULES/README/RESOURCES/ROADMAP → v1.4.0) | `gh auth login` → Phase 0 Anki review → M0.1 Linux Fundamentals |

