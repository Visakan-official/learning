# SPRINT PLAN — 4 WEEKS (26 working days + 2 buffer) · **Sep 14 → Oct 11, 2026**

**Agreed pace:** 8–10 hrs/day, ~59 hrs/week — **6 full days + 1 light Sunday** (5 hrs) per week.
**Target:** interview-ready for a 1–2 yr DevOps role (Chennai market) on **Sat 10 Oct 2026**, with buffer days Oct 10–11.
**Compression:** this is the v2.0 Pareto curriculum (ROADMAP.md) executed in **26 days**. It works because
① phases run in parallel (Stages A–E overlap), ② non-interview topics are ⚪ awareness-level, ③ drills start on
Day 3 instead of at the end. It does **not** work if you skip Anki, skip labs, or skip the drills.

---

## The rules of this sprint (non-negotiable)

1. **Daily Anki (Phase 0) — 30 min before anything new.** At this speed, spaced repetition is the only thing standing between you and a leaky memory. Skip it and Week 3 collapses.
2. **No day counts without proof.** Every day ends with: quiz/score, lab output, 5+ cards, journal entry, dashboard + commit pushed. That's the definition of a finished day.
3. **Drills run in parallel from Day 3.** Each day includes 45–90 min on `INTERVIEW-DRILLS.md` for that theme. Phase 7 is practice all along, not revision at the end.
4. **Sundays are light (5 hrs):** Anki + drill sweep + project work only. Sleep is part of the plan; 60 hrs/week of new material without a light day ends in burnout, not offers.
5. **Slip protocol (Rule 3):** miss 2 consecutive daily targets → we re-plan explicitly and stretch the sprint. We never silently skip a 🔴 topic.
6. **Cost discipline:** destroy lab resources at each session close. Only `Hermes-v4` (production `t3.small`) stays.
7. **Teaching order:** I teach before I test. You owe me raw output, not summaries.

**Daily rhythm (~9 hrs):**

| Block | Time | What |
|---|---|---|
| 1 | 60–75 min | **Phase 0 Anki** + yesterday's drill questions answered cold |
| 2 | 150 min | Teach + first hands-on (new module) |
| 3 | 150 min | Continue lab / build the project piece |
| 4 | 90 min | **Prove:** quiz on the day's module + `INTERVIEW-DRILLS` theme |
| 5 | 45 min | **Recall + close:** 5+ Anki cards, Obsidian note, journal, dashboard, commit, destroy |

---

## Week 1 — Interview floor (Sep 14–20) · *exit: Linux, networking, Git, Docker basics done; P1 shipped*

| Day | Date | Modules | Interview theme (EOD) | Proof of done |
|---|---|---|---|---|
| **D1** | Mon 14 Sep | Finish M0.1 permissions (**drill T1–T4 owed**) + logs & services (`journalctl`, `systemctl`) + processes (`ps/top/kill/ss/lsof`) | Linux A1–A5 | Drill T1–T4 output + services/processes lab |
| **D2** | Tue 15 Sep | M0.1 troubleshooting drills (disk full · svc down · port in use · perms · unreachable) + text tools (`grep/sed/awk`) + package mgmt & timers + bash essentials + **Lab 0.1** backup script | Linux A6–A15 | **Quiz 0.1 ≥80% + Defend** · cards 🗂️ `mira::0-foundations/linux` |
| **D3** | Wed 16 Sep | M0.2 networking (compressed) + **Lab 0.2** broken-box diagnosis | Networking B16–B25 | **Quiz 0.2 ≥80%** · cards 🗂️ `mira::0-foundations/networking` |
| **D4** | Thu 17 Sep | M0.3 Git + **Lab 0.3** repo restructure via branch+PR → then M1.1 IAM | Git + AWS C26–C27 | **Quiz 0.3 ≥80%** · cards 🗂️ `mira::0-foundations/git` · PR merged |
| **D5** | Fri 18 Sep | M1.1 IAM + M1.2 EC2/EBS (console **and** CLI) | AWS C28–C34 | **Quiz 1.1 + 1.2 ≥80%** · EC2 built & destroyed |
| **D6** | Sat 19 Sep | M2.1 Docker fundamentals + M2.2 volumes/networks/Compose | Docker D51–D62 | **Quiz 2.1 + 2.2 ≥80%** · multi-container app up |
| **D7** | **Sun 20 Sep** | **LIGHT (5h)** — Anki + drill sweep A/B + start **P1** (S3 static site + bucket policy) | — | P1 repo scaffolded |

**Week 1 exit test:** you can explain what happens on a URL request, triage a broken service, and run a container — cold, without notes.

---

## Week 2 — AWS core + containers (Sep 21–27) · *exit: P1 + P2 shipped, VPC designed and coded*

| Day | Date | Modules | Theme | Proof of done |
|---|---|---|---|---|
| **D8** | Mon 21 Sep | M1.3 VPC (design drill + build) + finish **P1** (ACM + CloudFront + Route 53 + GH Actions deploy) | AWS C26 | **Quiz 1.3 ≥80% + Defend** · **P1 LIVE on a real domain** |
| **D9** | Tue 22 Sep | M1.4 S3 deep + M1.5 ELB/ASG/Route 53 | AWS C35–C48 | **Quiz 1.4 + 1.5 ≥80%** · ALB+ASG running then destroyed |
| **D10** | Wed 23 Sep | M1.6 RDS/DynamoDB⚪/CloudWatch + M1.7 serverless⚪ | AWS C41–C50 | **Quiz 1.6 ≥80%** · alarm → SNS verified |
| **D11** | Thu 24 Sep | M3.1 Terraform core → **rebuild the VPC in code**, then destroy | Terraform F83–F92 | **Quiz 3.1 ≥80%** · VPC from `terraform apply` |
| **D12** | Fri 25 Sep | M2.3 registries/ECR + M2.4 K8s core part 1 (arch, pods, deployments, services, ingress) | K8s E63–E73 | ECR push via CLI · **Quiz 2.3 ≥80%** |
| **D13** | Sat 26 Sep | M2.4 K8s core part 2 + **troubleshooting drills** (CrashLoop, ImagePull, Pending, OOM, no endpoints, DNS) + install K3s | K8s E64–E69 | **Quiz 2.4 ≥80% + Defend** · pod running on K3s |
| **D14** | **Sun 27 Sep** | **LIGHT (5h)** — Anki + drill sweep C/D/E + start **P2** (dockerize the 3-tier app + Compose) | — | App runs in Compose with volumes+healthchecks |

---

## Week 3 — Orchestration, pipelines, IaC depth (Sep 28–Oct 4) · *exit: P2 in K8s via Helm, Jenkins pipeline green, TF state on S3*

| Day | Date | Modules | Theme | Proof of done |
|---|---|---|---|---|
| **D15** | Mon 28 Sep | M2.5 K8s intermediate (PV/PVC/StorageClass, StatefulSet, affinity/taints, HPA, RBAC, probe strategy) | K8s E70–E82 | **Quiz 2.5 ≥80%** · HPA scaling on load |
| **D16** | Tue 29 Sep | M2.6 Helm + deploy the app via a chart; **finish P2** incl. Jenkinsfile | K8s E82 · CI G93–G104 | **Quiz 2.6 ≥80%** · **P2 shipped + `Jenkinsfile` green** |
| **D17** | Wed 30 Sep | M4.1 CI/CD concepts (incl. **deployment strategies**) + M4.2 GH Actions deep incl. **OIDC keyless AWS auth** | CI G93 · G95 | **Quiz 4.1 + 4.2 ≥80%** · pipeline builds→pushes→deploys→smoke-tests |
| **D18** | Thu 1 Oct | M4.3 Jenkins (controller/agent, declarative pipeline, credentials) + M4.4 ArgoCD ⚪ | CI G98–G104 | **Quiz 4.3 ≥80%** · cards 🗂️ `mira::4-cicd/jenkins` |
| **D19** | Fri 2 Oct | M3.2 Terraform state (S3 + DynamoDB lock), modules, `import`/`state mv`, drift | Terraform F83–F92 | **Quiz 3.2 ≥80% + Defend** · remote backend demonstrated |
| **D20** | Sat 3 Oct | M5.1 Prometheus + Grafana + node_exporter + alert rules → wire into P3 | Observability H105–H112 | **Quiz 5.1 ≥80%** · alert fires on a real condition |
| **D21** | **Sun 4 Oct** | **LIGHT (5h)** — M5.2 logging + M6.2 security/secrets + drill sweep F/G/H | Obs/Security | Security drill: rotate + evaluate secrets path |

---

## Week 4 — Ops polish + interview bootcamp (Oct 5–11) · *exit: P3 shipped, 122 drills answered, 2 mocks passed*

| Day | Date | Modules | Theme | Proof of done |
|---|---|---|---|---|
| **D22** | Mon 5 Oct | M6.3 Well-Architected + cost optimisation (Cost Explorer/Budgets lab) + M6.1 ECS/EKS ⚪→🟡 | Cost H/C | **Quiz 6.1 + 6.3 ≥80% + Defend** · written cost recommendation |
| **D23** | Tue 6 Oct | M6.4 systems design + whiteboard drills ×3 · finish **P3** (blue-green or canary demo + README + diagram) | Project I113–I116 | **Quiz 6.4 ≥80%** · **P3 shipped** |
| **D24** | Wed 7 Oct | **Phase 7:** 3-min project stories ×3 (recorded/rehearsed) · resume + LinkedIn + GitHub profile polish mapped to a real Chennai JD | Behavioural I117–I122 | Resume reviewed line-by-line · stories timed |
| **D25** | Thu 8 Oct | **Phase 7:** mock loop #1 (screen → technical → scenario, graded) + repair every gap found · drill bank sweep 1 | Full bank | Mock #1 score + gap list closed |
| **D26** | Fri 9 Oct | **Phase 7:** mock loop #2 · break/fix mocks ×2 · salary/notice/on-call answers · **apply to 15 vetted Chennai JDs** | Full bank | Mock #2 passed · 15 applications sent with tailored resume |
| **B1** | Sat 10 Oct | **BUFFER:** repair anything failed; second clean pass on the hardest 20 drills; polish READMEs | — | All 🔴 modules ≥80% with zero open misses |
| **B2** | Sun 11 Oct | **BUFFER:** third pass on hardest drills · light Anki · rest | — | **Interview-ready** |

---

## Milestones (what "on track" means)

| Milestone | Date | Binary check |
|---|---|---|
| M0.1/M0.2/M0.3 passed | Sep 17 | 3 quizzes ≥80% + 3 labs in `journal/` |
| AWS core 🔴 complete | Sep 24 | Quizzes 1.1–1.6 ≥80%, VPC built in TF and destroyed |
| **P1 + P2 shipped** | Sep 29 | Public URLs/repos + READMEs + runbooks |
| K8s 🔴 complete | Sep 29 | Pods/Helm on K3s + all 6 troubleshooting drills answered |
| CI/CD + TF state 🔴 complete | Oct 2 | 2 pipelines + remote backend demo |
| **P3 shipped** | Oct 6 | Terraform + K3s + monitoring + blue-green evidence |
| 122 drills answered twice | Oct 9 | `INTERVIEW-DRILLS.md` checkboxes `[x]` |
| 2 mock loops passed | Oct 9 | My graded scorecards |

## Retention mitigation (the real risk at this speed)

1. **Anki daily, no exceptions** — 20–30 new cards/day generated by the modules; the queue grows to ~300 cards by Week 3. That's expected and correct.
2. **Interleaving:** each day's Block 1 re-tests 2–3 items from *previous* days, not just Anki.
3. **Drills twice** — never once. The 122-question bank gets a full second pass in D25–B1.
4. **After the sprint: maintenance mode.** While interviewing, 60–90 min/day: Anki queue + 5 random drills + 1 break/fix mock weekly. Interview performance decays without this — plan for it, don't "see how it goes".

## What this sprint does NOT make you

- **Not** a Kubernetes expert (that's the job, over years) — you'll be *interview-correct* on core + troubleshooting.
- **Not** fluent in Ansible/ArgoCD/service mesh/Deep ELK — you'll answer their concept questions and say so honestly.
- **Not** experienced. Three shipped projects + defensible answers is what a 1–2 yr band tests for; don't invent years you don't have. Say "lab + project proof" and let the work speak.

---

*Agreed 2026-09-13. Supersedes the pace table in ROADMAP §1 (25–30 hrs/wk → 7 weeks) for this sprint only;
ROADMAP content is unchanged — only the schedule is compressed. Re-plan trigger: 2 consecutive missed days.*
