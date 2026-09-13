# PROGRESS — status table + session log

| Module | Score | Date | Anki cards | Obsidian note | Status |
|--------|-------|------|-----------|---------------|--------|
| M0.1 Linux Fundamentals | — | — | — | — | 🔴 not-started |
| Day 0 (setup) | n/a | 2026-08-11 | 7 (mira::0-foundations/day0) | ✅ Day 0 note | ✅ complete |
| Host migration (Windows → Omarchy/Arch) | n/a | 2026-09-13 | 7 (unchanged, all due) | ✅ vault verified | ✅ complete |
| **Curriculum restructure → v2.0 (Pareto)** | n/a | 2026-09-13 | 7 | ✅ vault verified | ✅ complete |
| M0.1 Linux Fundamentals 🔴 | — | in progress | — | — | 🟡 in-progress (permissions taught; drill T1–T4 owed) |

## Session log

| Date | Session | What happened | Next action |
|------|---------|---------------|-------------|
| 2026-08-11 | Day 0 | RULES accepted; WSL2+Ubuntu (user jeeni); IAM admin+Admins group+MFA+keys; AWS CLI; billing alarm chain (SNS+CloudWatch, test email ✓); gh auth (Visakan-official); 7 Anki cards; Obsidian note; constraint: t3.small = PRODUCTION, never touch | M0.1 Linux Fundamentals: filesystem + navigation + file ops |
| 2026-09-13 | **Restructure — ROADMAP v2.0 (Pareto/Interview-First)** | Student requested Pareto restructure for the Chennai 1–2 yr DevOps market. Actions: re-tiered every module 🔴/🟡/⚪; **demoted** Ansible · CloudFormation · ArgoCD · ECS/EKS depth · serverless · DynamoDB · deep ELK to awareness; **cut** BGP/VLAN-depth · Chef/Puppet/Vault/service-mesh · the 4th project; **expanded** K8s troubleshooting + Phase 7 interview bootcamp (now the largest phase); **parallelised** AWS+Docker+Terraform (Stage B) instead of serial phases → 25–30 hrs/wk ≈ 7 weeks (was 28 serial). Created `INTERVIEW-DRILLS.md` (122 scenario questions, A–I by theme). Also: taught the M0.1 permissions foundation from zero after the student correctly rejected a drill on untaught ground (btrfs subvolumes, sticky bit, rwx/chmod) — teaching-order ladder now written into the teacher skill | Finish M0.1 drill T1–T4 → remaining M0.1 boxes → Quiz 0.1 |
| 2026-09-13 | Maintenance — host migration | Windows → **Omarchy 4.0.2 (Arch)**: repo copied to `~/Ai-assisted-learning` (NTFS `A:` original kept as fallback); vault → `~/Documents/Obsidian/Mira Bootcamp` (byte-identical); AWS CLI v2 installed to `~/.local` (no sudo) + creds migrated → `sts get-caller-identity` ✓ visakan-admin/139316821068; AnkiConnect :8765 ✓ + Anki MCP :3141 ✓ (**7 cards due, not yet reviewed**); dashboard script v1.4.0 (portable + stdlib-only) rebuilt ✓; live docs de-Windowsified (RULES/README/RESOURCES/ROADMAP → v1.4.0) | `gh auth login` → Phase 0 Anki review → M0.1 Linux Fundamentals |

