# AWS + DevOps Bootcamp — ROADMAP **v2.0 (PARETO / INTERVIEW-FIRST)**

**Target role:** DevOps Engineer, **1–2 years experienced**, Chennai / South-India market
**Goal:** clear *any* interview loop for that band, in the **shortest defensible time**.
**Method (unchanged):** Learn → Do → Prove → Defend → **Recall**
**Tiers:** 🔴 CORE (deep, quiz ≥80% + defend + 5 cards + note) · 🟡 WORKING (usable + explainable, short quiz) · ⚪ AWARENESS (2-sentence answer + 2–3 cards, no lab)
**Anki legend:** 🗂️ = deck tag `mira::<phase>/<module>` — every 🔴 module ends with **5+ cards created**.

---

## 0. The Pareto decision — what actually gets asked

| Interview theme | Share of loop time | Tier | Why |
|---|---|---|---|
| Linux + shell + **troubleshooting** | ~25% | 🔴 | Gates the interview. "Disk full, service down, port in use" scenarios |
| Docker + **Kubernetes** | ~25% | 🔴 | The single most-demanded skill; K8s troubleshooting > K8s theory |
| AWS core (EC2/VPC/S3/IAM/ALB/ASG/RDS/CloudWatch/R53) | ~20% | 🔴 | Eight services cover ~90% of questions |
| CI/CD — **Jenkins + GitHub Actions** | ~10% | 🔴 | Chennai enterprises still interview Jenkins; startups interview Actions |
| Terraform | ~10% | 🔴 | Standard IaC answer. State/lock/import are the real questions |
| Prometheus/Grafana + logging concepts | ~5% | 🟡 | Asked as "how do you know it broke?" |
| Project deep-dive + behaviourals | ~5% of questions, **~100% of the decision** | 🔴 | "Walk me through your project, then tell me what broke" |
| Ansible · CloudFormation · ArgoCD · service mesh · tracing · ECS/EKS deep · ELK · Vault · Chef/Puppet | remainder | ⚪ | Namedrops must land; labs are not worth the hours |

**Rule v2.0:** we do not go deep where interviewers don't. Every 🔴 module is justified by a question that *will* be asked.

---

## 1. Timeline (pick your hours — this is the whole plan)

| Your pace | Duration | Finish if we start today |
|---|---|---|
| 30+ hrs/week (aggressive) | **~5.5 weeks** | ~20 Oct 2026 |
| **25–30 hrs/week (recommended)** | **~7 weeks** | ~1 Nov 2026 |
| 20 hrs/week | ~9 weeks | ~15 Nov 2026 |
| 10–12 hrs/week (original plan) | ~16 weeks | ~Jan 2027 |

Daily shape at 25–30 hrs/wk: **~2.5 h hands-on lab + 1 h teach/quiz + 30 min Anki (Phase 0) + 15 min journal/closure.** Weekends: one project block. **Anki is non-negotiable daily — it's 30 min that saves a week.**

---

## 2. Execution stages (the real order — phases below are the *taxonomy*)

| Stage | Weeks | Content | Exit proof |
|---|---|---|---|
| **A — Interview floor** | 1 | Linux interview-core (M0.1), networking trim (M0.2), Git (M0.3), Docker fundamentals (M2.1) | You can get around a box, explain DNS/HTTP/LB, branch/merge/PR, build+run a container |
| **B — Cloud + containers** | 2–4 | AWS core M1.1–M1.6 (parallel with Docker M2.1–M2.3), Terraform core M3.1 | **P1 shipped**, **P2 shipped**, VPC designed on paper + built |
| **C — Orchestration + pipelines** | 4–6 | K8s M2.4–M2.5, Helm M2.6, CI/CD M4.1–M4.3 | Pod deployed to K3s, Jenkinsfile + GH Actions pipeline green |
| **D — IaC depth + flagship** | 6–7 | Terraform state M3.2, ⚪ M3.3–M3.4, GitOps ⚪ M4.4 | **P3 shipped** (Terraform + K3s + monitoring) |
| **E — Ops polish + interview bootcamp** | 7–8 | Observability M5.1–M5.3, Security/cost M6.2–M6.4, **expanded Phase 7** | 100 interview questions drilled, 3 project stories, 2 mock interviews passed |

Cost discipline still applies every single session (Phase 6 = destroy). Lab ceiling: stay in free tier + ~$5 for a short EKS/K3s experiment.

---

## PHASE 0 — Foundations · **compressed to the interview-critical subset**

### M0.1 Linux Fundamentals 🔴 — *the #1 skill interviewers probe*
- [ ] FHS + storage layers in practice (`lsblk`, `findmnt`, subvolumes, `man 7 hier`)
- [ ] **Permissions from zero**: uid/gid/groups → 3 triads → r/w/x on files **vs directories** → octal → `chmod` (both syntaxes) → `chown`/`chgrp` → `umask` → setuid/setgid/sticky → `stat`/`namei`
- [ ] Navigation + file ops under time pressure (`ls/find/du/df/stat`), symlinks vs hardlinks
- [ ] **Logs & services**: `journalctl -u`, `systemctl status/restart/enable`, `/var/log`, log rotation
- [ ] **Processes**: `ps/top/htop`, `kill` & signals, `nohup`/`&`/`jobs`, `lsof`, `ss -tulpn`
- [ ] **Troubleshooting drills (interview format)**: disk full · high CPU/mem · service won't start · port already in use · permission denied · can't reach a host
- [ ] Text tools: `grep/sed/awk/cut/sort/uniq/wc/xargs`, pipes + redirection
- [ ] Package management (**pacman/AUR**; apt/yum conceptually), cron + systemd timers, env vars
- [ ] **Bash scripting 🟡**: variables, conditionals, loops, functions, exit codes, `set -euo pipefail`
- [ ] **Lab 0.1:** production-style backup script (log rotation + failure alert) → `journal/`
- [ ] **Lab 0.2:** broken-box diagnosis — I break it, you find it, in <15 min
- [ ] **Quiz 0.1 ≥80% + Defend** · **Recall:** 5+ cards 🗂️ `mira::0-foundations/linux`

### M0.2 Networking Basics 🔴 — *trimmed to what's tested*
- [ ] OSI in 60 s + TCP vs UDP, ports, 3-way handshake, TLS handshake outline
- [ ] IP/CIDR, public vs private, NAT, **subnet math you can do in your head** (VPC prep)
- [ ] DNS end-to-end: resolution flow, A/AAAA/CNAME/MX/TXT/NS, TTL, `dig`/`nslookup`
- [ ] HTTP/S: methods, status codes, headers, cookies
- [ ] Reverse proxy vs load balancer, L4 vs L7, health checks
- [ ] 🔴 **"What happens when I type a URL and press Enter?"** — the classic opener, answer in 90 s
- [ ] **Quiz 0.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::0-foundations/networking`

### M0.3 Git & GitHub 🔴 — *daily tool, embarrassing to be weak at*
- [ ] Repos, staging, commits, `.gitignore`, `diff`, `log`, `blame`, conventional commits
- [ ] Branch/merge/rebase, conflict resolution, `stash`, `cherry-pick`, tags + releases
- [ ] Undo: `checkout`, `restore`, `revert` vs `reset --soft/--mixed/--hard` (what each does to history)
- [ ] Remotes, `fetch` vs `pull`, PR workflow (branch → PR → review → merge)
- [ ] **Lab 0.3:** restructure THIS repo through a feature branch + PR
- [ ] **Quiz 0.3 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::0-foundations/git`

---

## PHASE 1 — AWS Core (the 8 services that carry the interview)

### M1.1 IAM 🔴 — *always the first security question*
- [ ] Users/groups/roles/policies; **groups for permissions, users for identity**
- [ ] Policy JSON: Effect/Action/Resource/Condition; managed vs inline; least privilege
- [ ] Roles vs access keys; instance profiles; **why root keys are banned**
- [ ] MFA, password policy, credential reports, Access Analyzer
- [ ] **Quiz 1.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/iam`

### M1.2 EC2 + EBS 🔴 — *bread and butter*
- [ ] Instances, types (t/burstable vs m/c/r families), AMIs, key pairs, user data
- [ ] EBS types (gp3/io2/st1), snapshots, AMI from snapshot, encryption
- [ ] Security groups vs NACLs (stateful vs stateless — guaranteed question)
- [ ] Spot/reserved/savings plans; **instance metadata & IMDSv2**
- [ ] SSH access patterns, bastion vs SSM Session Manager
- [ ] **Quiz 1.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/ec2-ebs`

### M1.3 VPC 🔴 — *the #1 AWS interview killer*
- [ ] VPC, subnets (public/private), IGW, NAT GW, route tables, NACLs
- [ ] CIDR planning by hand; AZs; VPC peering + endpoints (gateway/interface)
- [ ] **Design drill:** 3-tier VPC on paper → defend every route and SG rule
- [ ] Build it live (Terraform in Stage B), then destroy (Phase 6)
- [ ] **Quiz 1.3 ≥80% + Defend** · **Recall:** 5+ cards 🗂️ `mira::1-aws/vpc`

### M1.4 S3 🔴 — *most-asked service, cheapest points*
- [ ] Buckets, objects, keys, storage classes, versioning, lifecycle, replication
- [ ] Policies vs ACLs vs block-public-access; presigned URLs; static hosting
- [ ] Encryption (SSE-S3/KMS/SSE-C), Object Lock basics; CloudFront in front
- [ ] **Quiz 1.4 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/s3`

### M1.5 ELB + ASG + Route 53 🔴
- [ ] ALB vs NLB vs GWLB; target groups, listeners, health checks, sticky sessions
- [ ] Launch templates + ASG: min/max/desired, scaling policies, cooldown, lifecycle hooks
- [ ] Route 53: hosted zones, A/CNAME/alias, routing policies (weighted, latency, failover), TTLs
- [ ] **Quiz 1.5 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/elb-asg-r53`

### M1.6 RDS + DynamoDB ⚪ + CloudWatch 🔴
- [ ] RDS: engines, Multi-AZ vs read replicas (the classic distinction), backups/PITR, snapshots
- [ ] CloudWatch: **metrics vs logs vs alarms**, Log Insights queries, dashboards, alarm → SNS
- [ ] SNS vs SQS, EventBridge outline; **billing metrics live only in us-east-1**
- [ ] ⚪ DynamoDB: PK/SK, on-demand vs provisioned, when NoSQL vs RDS
- [ ] **Quiz 1.6 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/rds-ddb-cw`

### M1.7 Serverless ⚪ — *awareness only*
- [ ] Lambda (handler, timeout, cold starts, IAM role), API Gateway, when NOT to use serverless
- [ ] **Recall:** 3 cards 🗂️ `mira::1-aws/serverless`

### 📦 PROJECT P1 (Shipped end of Stage B): Static site → S3 + CloudFront + Route 53 + GitHub Actions
**Interview value:** DNS + CDN + IAM least privilege + a real CI/CD pipeline + cost story (free tier).

---

## PHASE 2 — Containers: Docker + Kubernetes 🔴 *(the heart of the loop)*

### M2.1 Docker Fundamentals 🔴
- [ ] Why containers vs VMs; images/layers/union-FS; registry pull flow
- [ ] `build/run/exec/logs/inspect/ps/rm/rmi`, port mapping, env vars, entrypoint vs cmd
- [ ] **Dockerfile craft**: layer caching order, multi-stage builds, `.dockerignore`, slim/distroless
- [ ] Debugging: container exits instantly, exec into a broken container, log-less failures
- [ ] **Quiz 2.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/docker`

### M2.2 Volumes, Networks, Compose 🔴
- [ ] Named volumes vs bind mounts vs tmpfs; **data loss on `docker rm`** drill
- [ ] Bridge/host/none/overlay; container DNS by service name; published ports vs internal
- [ ] Compose: services, depends_on/healthcheck, env files, profiles, `up -d`/`logs`/`down -v`
- [ ] **Quiz 2.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/compose`

### M2.3 Registries & Image Security 🟡
- [ ] ECR: repos, auth, tags vs digests, lifecycle policies, scanning
- [ ] Image hygiene: minimal base, non-root user, no secrets in layers, SBOM/Trivy outline
- [ ] **Quiz 2.3 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/registries`

### M2.4 Kubernetes Core 🔴 — *the biggest interview topic of all*
- [ ] Architecture: control plane (API server, etcd, scheduler, controller-manager) vs kubelet/kube-proxy/CRI
- [ ] Pods, ReplicaSets, Deployments, rollout/rollback, DaemonSet/StatefulSet/Job outline
- [ ] Services (ClusterIP/NodePort/LB) + **Ingress**, ConfigMap/Secret, Namespaces, resource requests/limits
- [ ] Probes (liveness/readiness/startup) — why readiness ≠ liveness
- [ ] **Troubleshooting drills 🔴**: CrashLoopBackOff · ImagePullBackOff · Pending (resources/taints) · OOMKilled · Service has no endpoints · DNS inside the cluster
- [ ] **Quiz 2.4 ≥80% + Defend** · **Recall:** 5+ cards 🗂️ `mira::2-containers/k8s-core`

### M2.5 K8s Intermediate 🟡
- [ ] Storage: PV/PVC/StorageClass, emptyDir vs PVC, StatefulSet + headless service
- [ ] Scheduling: nodeSelector/affinity/taints+tolerations, HPA + metrics-server
- [ ] RBAC + ServiceAccounts, NetworkPolicy, Jobs/CronJobs, RollingUpdate vs Recreate strategy
- [ ] **Quiz 2.5 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/k8s-intermediate`

### M2.6 Helm 🟡
- [ ] Chart anatomy (Chart.yaml/values/templates), `helm install/upgrade/rollback/history`, values override order
- [ ] Templating essentials (`{{ }}`, `--set`, `.Values`, `_helpers.tpl` outline)
- [ ] ⚪ Operator/CRD concept in 2 sentences
- [ ] **Quiz 2.6 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/helm`

### 📦 PROJECT P2 (Shipped end of Stage B/C): Dockerized 3-tier app → ECR → EC2 + Compose → Jenkins pipeline
**Interview value:** multi-container Compose, volumes, healthchecks, image registry pipeline, deployment script, rollback.

---

## PHASE 3 — Infrastructure as Code

### M3.1 Terraform Core 🔴
- [ ] HCL: providers, resources, variables, outputs, locals, data sources, `plan/apply/destroy`
- [ ] `for_each` vs `count`, depends_on, implicit vs explicit dependency graph
- [ ] **Lab:** build the M1.3 VPC 100% in code, then destroy
- [ ] **Quiz 3.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::3-iac/terraform-core`

### M3.2 Terraform State & Remote Backends 🔴
- [ ] Why state exists, what's in it, why it must not be committed or shared loose
- [ ] S3 + DynamoDB locking backend; workspaces; `import`, `state mv/rm`, drift + refresh
- [ ] Modules: inputs/outputs, when a module earns its keep; `terraform fmt/validate/tflint` outline
- [ ] **Quiz 3.2 ≥80% + Defend** · **Recall:** 5+ cards 🗂️ `mira::3-iac/terraform-state`

### M3.3 Ansible ⚪ — *be able to talk about it*
- [ ] Agentless model, inventory, playbook/role structure, idempotency; **Ansible vs Terraform** in one answer
- [ ] One tiny playbook run against localhost (no big lab)
- [ ] **Recall:** 3 cards 🗂️ `mira::3-iac/ansible`

### M3.4 CloudFormation / CDK ⚪
- [ ] Stacks, templates, drift, why AWS shops still use it; TF vs CFN trade-off answer
- [ ] **Recall:** 3 cards 🗂️ `mira::3-iac/cloudformation`

### 📦 PROJECT P3 (flagship, shipped end of Stage D): 3-tier app on AWS, 100% Terraform + K3s + monitoring
**Interview value:** VPC/SG/ALB/EC2/RDS provisioned as code, K8s workload deployed, Prometheus + Grafana, blue-green or canary cutover, cost teardown story.

---

## PHASE 4 — CI/CD 🔴

### M4.1 CI/CD Concepts 🔴
- [ ] CI vs CD vs CD(deploy); build→test→scan→push→deploy; artifacts vs images; environments
- [ ] **Deployment strategies 🔴**: rolling, blue-green, canary, recreate — trade-offs (guaranteed question)
- [ ] Rollback thinking; feature flags; trunk-based vs gitflow (opinion + why)
- [ ] **Quiz 4.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::4-cicd/concepts`

### M4.2 GitHub Actions 🔴
- [ ] Workflow anatomy: on/jobs/steps/runners, matrix builds, caching, artifacts, environments + approvals
- [ ] Secrets/OIDC **keyless AWS auth** (no long-lived keys in CI), reusable workflows outline
- [ ] **Lab:** full pipeline — lint → test → build → push to ECR → deploy → smoke test
- [ ] **Quiz 4.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::4-cicd/gh-actions`

### M4.3 Jenkins 🟡 (still in ~60% of Chennai JDs)
- [ ] Architecture: controller vs agents, executors, plugins, credentials store
- [ ] Freestyle vs **declarative Pipeline**; `Jenkinsfile` stages/steps/agent/post; parameters
- [ ] Shared libraries + multibranch concept (⚪); `Jenkinsfile` vs GH Actions comparison answer
- [ ] **Lab:** same P2 pipeline expressed as a `Jenkinsfile`
- [ ] **Quiz 4.3 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::4-cicd/jenkins`

### M4.4 GitOps / ArgoCD ⚪
- [ ] Git as source of truth, pull vs push deployment, sync/drift/self-heal, ArgoCD vs Flux in a sentence
- [ ] **Recall:** 3 cards 🗂️ `mira::4-cicd/gitops`

---

## PHASE 5 — Observability 🟡

### M5.1 Prometheus + Grafana 🔴 *(asked as "how do you know it broke?")*
- [ ] Pull model, exporters (node_exporter), scrape configs, PromQL basics (rate/increase/sum by), alert rules → Alertmanager
- [ ] Grafana: data sources, dashboards, **USE/RED method** for what to chart
- [ ] **Quiz 5.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::5-observability/prometheus`

### M5.2 Logging 🟡
- [ ] `journald` + Docker/K8s log flow, structured (JSON) logging, log levels, retention/cost
- [ ] ⚪ ELK/Loki architecture in 2 sentences; CloudWatch Logs + metric filters
- [ ] **Quiz 5.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::5-observability/logging`

### M5.3 SLI/SLO + incident response ⚪→🟡
- [ ] SLI/SLO/error budget in one answer; MTTR mindset; on-call runbook + postmortem structure
- [ ] **Recall:** 3 cards 🗂️ `mira::5-observability/tracing`

---

## PHASE 6 — Advanced AWS + Security + Cost

### M6.1 ECS & EKS ⚪→🟡
- [ ] ECS: task definitions, services, Fargate vs EC2 launch type — comparison-ready
- [ ] EKS: what AWS manages vs what you do, node groups, IRSA outline; **K3s is our lab** (cost), EKS optional short lab
- [ ] **Quiz 6.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/ecs-eks`

### M6.2 Secrets & Security 🔴
- [ ] Secrets Manager vs SSM Parameter Store vs env vars; rotation; never-in-git discipline
- [ ] Least-privilege IAM review, S3 bucket hardening, SG hygiene, GuardDuty/CloudTrail outline
- [ ] SSH key hygiene (0600), TLS certs (ACM), VPC endpoints for private access
- [ ] **Quiz 6.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/security`

### M6.3 Well-Architected + Cost 🔴
- [ ] The 6 pillars in one line each; cost levers: right-sizing, graviton, spot, S3 lifecycle, scheduling, free tier traps
- [ ] **Lab:** Cost Explorer + Budgets + alarm review → one written cost-optimisation recommendation
- [ ] **Quiz 6.3 ≥80% + Defend** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/cost`

### M6.4 Systems Design & Migration 🔴
- [ ] Design a scalable 3-tier app on AWS (VPC, multi-AZ, ASG, ALB, RDS, cache, CDN) — whiteboard + defend
- [ ] Design a multi-region/DR answer (RTO/RPO), lift-shift vs re-platform vs re-architect
- [ ] Containerise-and-deploy an existing app: the migration story interviewers love
- [ ] **Quiz 6.4 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/design`

---

## PHASE 7 — INTERVIEW BOOTCAMP 🔴 *(expanded — this is where the offer is won)*

- [ ] **Rapid-fire bank:** 100+ scenario questions from `INTERVIEW-DRILLS.md`, gap-free, twice through
- [ ] **Project storytelling:** each of P1/P2/P3 told in 3 min (problem → design → build → breakage → fix → result) + 4 pre-loaded follow-up answers
- [ ] **Break/fix mocks:** I break an EC2/K8s/CI pipeline live; you diagnose under time pressure (5 rounds)
- [ ] **Whiteboard drills:** 3-tier VPC · CI/CD flow · K8s request path · blue-green vs canary (4 rounds)
- [ ] **Behaviourals:** "tell me about a failure", "conflict in a team", "tight deadline" — 3 STAR stories rehearsed
- [ ] **Resume + LinkedIn + GitHub polish:** outcome-first bullets, quantified, mapped to the JD
- [ ] **Full mock loop ×2:** screen → technical → scenario → manager round, graded by me
- [ ] **Salary + negotiation script** for the Chennai band; notice/bond questions answered professionally
- [ ] **Defend:** "why should we hire you over someone with 2 years?" — 60 s, no filler

---

## 3. What we CUT and DEMOTED (explicit — no silent drops, Rule 3)

| Item | v1.3.0 | v2.0 | Reasoning | Risk if asked |
|---|---|---|---|---|
| Ansible | full module | ⚪ awareness + tiny localhost playbook | Rarely probed beyond "what is it / vs Terraform" at 1–2 yr | Cover in one 20-min session before an interview that names it |
| CloudFormation | quiz + cards | ⚪ awareness | AWS-only shops ask it conceptually | 1-line comparison answer exists |
| ArgoCD/GitOps | module + lab | ⚪ awareness | Asked as a concept; lab hours buy little at this band | You can still explain pull-based deploy |
| ECS/EKS labs | module depth | ⚪→🟡 concepts, **K3s as the lab** | EKS control-plane cost + duplicates K8s learning | Same K8s questions; EKS specifics = 5 cards |
| Observability depth | 3 modules | 🟡 Prometheus/Grafana real, rest ⚪ | Alerts/dashboards are asked; tracing/SLO rarely | SLI/SLO answer rehearsed in Phase 7 |
| Serverless | module + lab | ⚪ | Out of scope for most JD-s in this band | 3 cards |
| DynamoDB depth | module | ⚪ | Rarely deep for DevOps | Comparison answer |
| Deep bash (arrays/traps) | partial | 🟡 only what scripts need | Interviews ask short scripts, not bash golf | Scripting drills in Phase 7 |
| BGP/VLAN/OSPF deep networking | partial | **cut** | Cloud-networking roles ask it; DevOps-in-Chennai doesn't | Say "routing beyond AWS I'm learning" honestly |
| Chef/Puppet/Vault/service mesh | mentioned | **cut** | Legacy/over-scoped for this band | One-line awareness |
| 4th project | 4 projects | **3 projects** | 3 deep stories beat 4 shallow ones | Coverage preserved via P3 |
| Deep Terraform module libraries | module | 🟡 modules + `state mv/import` | State questions are the real filter | Modules asked as "have you built one" — you will have |

**Sequencing change (the biggest time win):** v1.3.0 ran phases strictly serially (Weeks 1–28). v2.0 **parallelises**: AWS + Docker + Terraform move together in Stage B, and CI/CD is taught *through* projects, not as a theory block. Same coverage of 🔴 items, ~60% of the calendar.

---

## 4. The 3 Portfolio Projects (resume pieces)

| # | Project | Stack | Ships | Interview value |
|---|---|---|---|---|
| P1 | Static site, prod-grade | S3 + CloudFront + Route 53 + ACM + **GitHub Actions** | End Stage B | DNS/CDN/IAM/OIDC + pipeline + cost story |
| P2 | Dockerized 3-tier app | Docker + Compose + ECR + EC2 + **Jenkins** | End Stage C | Multi-container, volumes, healthchecks, image pipeline, rollback |
| P3 | AWS infra as code + K8s + monitoring | **Terraform** + VPC/ALB/ASG/RDS + **K3s** + Helm + Prometheus/Grafana + blue-green | End Stage D | The flagship: everything a 1–2 yr JD lists, in one repo |

Each project = code + README (architecture diagram, runbook, "what I'd improve") + a 3-min spoken story. **A project you can't explain does not exist.**

---

## 5. Chennai market layer (why the tiers look like this)

- **Who's hiring around you:** GCCs & product cos (Zoho, Freshworks, PayPal, Walmart, Ford, Comcast, Athenahealth, Amazon) + service cos (TCS, Infosys, Cognizant, HCL, Wipro, LTIMindtree) + product startups. GCC/product loops probe **K8s + Terraform + Linux troubleshooting**; service cos probe **Jenkins + AWS + shell scripting** + communication. v2.0 targets the union.
- **Typical loop:** screening → 1–2 technical rounds (heavy scenario + "explain your project") → sometimes a live break/fix or a small script → managerial round (attitude, shifts/on-call, notice period) → HR.
- **Recurring Chennai-specific questions:** disk-full triage · "pod is in CrashLoopBackOff, go" · write a shell script to check a service and alert · Jenkins pipeline vs Jenkinsfile · how do you deploy without downtime · VPC design for 3 tiers · IAM least privilege · what do you do when prod goes down at 2 AM.
- **Band:** roughly ₹4.5–9 LPA for 1–2 yrs (product GCCs at the top). Your leverage at this band is **demonstrable lab + project proof**, not years — which is exactly what this repo produces.
- **Truth to hold onto:** no course "clears any interview". What clears interviews is being able to answer *this* bank cold, defend your projects, and stay calm in break/fix. That's Phase 7, and it's why Phase 7 is now the largest phase in v2.0.

---

*ROADMAP v2.0 (2026-09-13) — Pareto restructure for the Chennai 1–2 yr DevOps market. Supersedes v1.3.0. Changes logged in `PROGRESS.md` + `journal/2026-09-13.md`.*
