# AWS + DevOps Bootcamp — ROADMAP (v1.3.0)

**Target role:** 1–2 year experienced DevOps Engineer (India market)
**Pacing assumption:** ~10–12 hrs/week → **~5–6 months total** (compressible if you grind)
**Status legend:** `[ ]` = not started · `[~]` = in progress · `[x]` = COMPLETE (quiz ≥80% + lab + defend + **Anki cards** + Obsidian note)
**Anki legend:** 🗂️ = deck tag for this module's flashcards (`mira::<phase>/<module>`). Every module ends with **Phase 5 — Recall: 5+ cards created.**

---

## PHASE 0 — Foundations (Weeks 1–3) · *no AWS yet, this is the base*

### M0.1 Linux Fundamentals — *the #1 skill interviewers probe*
- [ ] Filesystem layout, navigation, file ops (`ls`, `find`, `cp`, `mv`, `ln`)
- [ ] Permissions & ownership (chmod/chown, umask, setuid/setgid/sticky), users/groups
- [ ] Processes: ps, top/htop, kill, signals, jobs, nohup, systemd (units, journalctl)
- [ ] Text tools: grep, sed, awk, sort, uniq, cut, wc, xargs, pipes & redirection
- [ ] Network tools: curl, wget, ss/netstat, ping, dig/nslookup, nc
- [ ] Package management (apt), cron & systemd timers, environment variables
- [ ] **Bash scripting:** variables, conditionals, loops, functions, exit codes, error handling
- [ ] **Lab 0.1:** Write a production-style backup script (log rotation + notify on failure), commit to journal
- [ ] **Lab 0.2:** Linux troubleshooting drill — you're handed a broken box, you diagnose it
- [ ] **Quiz 0.1 ≥80%** + Defend: 10 interview Qs
- [ ] **Recall:** 5+ Anki cards 🗂️ `mira::0-foundations/linux` · Obsidian note
- 🗂️ **Deck:** `mira::0-foundations/linux`

### M0.2 Networking Basics
- [ ] OSI model (focus 4/7), TCP vs UDP, ports, 3-way handshake
- [ ] IP addressing, subnets/CIDR basics, private vs public IPs, NAT concept
- [ ] DNS: resolution flow, record types (A, AAAA, CNAME, MX, TXT, NS), dig drills
- [ ] HTTP/HTTPS: methods, status codes (1xx–5xx), headers, cookies, TLS handshake
- [ ] Proxies, reverse proxies, load balancer concept (why LB? health checks?)
- [ ] **Quiz 0.2 ≥80%**
- [ ] **Recall:** 5+ Anki cards 🗂️ `mira::0-foundations/networking` · Obsidian note

### M0.3 Git & GitHub — *daily tool, embarrassing to be weak at*
- [ ] Repos, commits, staging, `.gitignore`, diff, log, blame
- [ ] Branching: create/merge/delete, merge vs rebase, conflict resolution
- [ ] undo: checkout, revert, reset (soft/mixed/hard), stash, cherry-pick
- [ ] Remotes: fetch/pull/push, tags, releases
- [ ] GitHub workflow: fork → branch → PR → review → merge; conventional commits
- [ ] **Lab 0.3:** Restructure THIS repo via a feature branch + PR (practice on real work)
- [ ] **Quiz 0.3 ≥80%**
- [ ] **Recall:** 5+ Anki cards 🗂️ `mira::0-foundations/git` · Obsidian note

✅ **Milestone 1 (end of Phase 0):** Mock interview #1 — Linux + Networking + Git (30 min, strict)

---

## PHASE 1 — AWS Core (Weeks 4–8)

### M1.1 IAM — *security foundation, huge in interviews*
- [ ] Users, groups, roles, policies (JSON), policy evaluation logic
- [ ] Least privilege, MFA, access keys best practices, trust policies
- [ ] **Lab:** Create admin user, MFA, billing alarm, AWS CLI + credentials, s3 bucket policy
- [ ] **Quiz 1.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/iam`

### M1.2 EC2 + EBS — *bread and butter*
- [ ] AMIs, instance types & families, pricing models (on-demand, reserved, spot)
- [ ] Key pairs, security groups (stateful, default rules), user-data scripts
- [ ] EBS: volumes, snapshots, AMI creation, instance store vs EBS, gp3/io1
- [ ] **Lab:** Launch hardened web server via user-data, snapshot + restore drill
- [ ] **Quiz 1.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/ec2-ebs`

### M1.3 VPC — *the #1 AWS interview killer, master it*
- [ ] CIDR design, subnets (public/private), route tables, IGW, NAT gateway/instance
- [ ] Security groups vs NACLs (stateless vs stateful — exam favourite), VPC peering, endpoints, bastion hosts
- [ ] **Lab:** Build a full VPC: 2 AZs, public+private subnets, NAT, ALB in public, app in private, RDS in db subnet — ALL from console first, then documented
- [ ] **Quiz 1.3 ≥80%** + Defend · **Recall:** 5+ cards 🗂️ `mira::1-aws/vpc`

### M1.4 S3 — *most-used service, cheapest interview points*
- [ ] Buckets, objects, keys, storage classes, lifecycle policies, versioning
- [ ] Static website hosting, CORS, presigned URLs, S3 vs EBS vs EFS
- [ ] Security: bucket policies, ACLs vs policies, encryption (SSE-S3/KMS), MFA delete
- [ ] **Lab:** Static site on S3 + versioning + lifecycle + presigned URL script
- [ ] **Quiz 1.4 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/s3`

### M1.5 ELB + ASG + Route 53
- [ ] ALB vs NLB vs CLB, target groups, listeners, health checks, stickiness
- [ ] ASG: launch templates, scaling policies, cooldowns, lifecycle hooks
- [ ] Route 53: hosted zones, routing policies (simple, weighted, latency, failover), alias vs CNAME
- [ ] **Lab:** ALB + ASG serving a stress-testable app; simulate AZ failure, watch it recover
- [ ] **Quiz 1.5 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/elb-asg-r53`

### M1.6 RDS + DynamoDB + CloudWatch
- [ ] RDS: engines, Multi-AZ, read replicas, backups, parameter groups, aurora mention
- [ ] DynamoDB: tables, partition keys, RCU/WCU vs on-demand, indexes (GSI/LSI), DAX mention
- [ ] CloudWatch: metrics, alarms, logs, log groups, agent, unified agent
- [ ] **Lab:** RDS + app connecting via SG rules; CloudWatch alarm that pages you
- [ ] **Quiz 1.6 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/rds-ddb-cw`

### M1.7 Serverless Foundations
- [ ] Lambda: runtime, triggers, layers, env vars, timeout/memory, cold starts, IAM role
- [ ] API Gateway: REST vs HTTP, stages, throttling
- [ ] EventBridge, SQS/SNS basics
- [ ] **Lab:** "Image resize on upload" — S3 → Lambda → S3, plus EventBridge cron Lambda
- [ ] **Quiz 1.7 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::1-aws/serverless`

✅ **Milestone 2 (end of Phase 1):** Mock interview #2 — AWS deep-dive (45 min, strict) + **Project P1**

### 📦 PROJECT P1 (resume piece #1): Static site on S3 + CloudFront + Route 53 + CI/CD
Static portfolio site, custom domain, HTTPS, GitHub Actions deploy on push, versioned S3.

---

## PHASE 2 — Containers: Docker + Kubernetes (Weeks 8–13) *the heart of modern DevOps*

### M2.1 Docker Fundamentals
- [ ] Images vs containers vs layers; Dockerfile (FROM, RUN, COPY, CMD, ENTRYPOINT, EXPOSE)
- [ ] Image build cache, multi-stage builds, .dockerignore
- [ ] run/exec/ps/logs/rm/rmi, port publishing, env vars, healthchecks
- [ ] **Lab:** Containerize a real app (node or python) with multi-stage build, run it, inspect it
- [ ] **Quiz 2.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/docker`

### M2.2 Volumes, Networks, Compose
- [ ] Named volumes vs bind mounts, tmpfs
- [ ] Bridge vs host vs none networks, container-to-container DNS
- [ ] Docker Compose: services, networks, volumes, depends_on, env files, profiles
- [ ] **Lab:** Full-stack compose: app + postgres + redis + nginx reverse proxy, all wired
- [ ] **Quiz 2.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/compose`

### M2.3 Registries & Image Security
- [ ] Docker Hub, ECR (AWS), tagging, `docker login`, pull policies
- [ ] Image scanning (Trivy), distroless/scratch, least-privilege users in images
- [ ] **Lab:** Push to ECR from local, scan images, fix high-CVEs
- [ ] **Quiz 2.3 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/registries`

### M2.4 Kubernetes Core — *the biggest interview topic of all*
- [ ] Architecture: control plane (API server, etcd, scheduler, controller manager) vs nodes (kubelet, kube-proxy, container runtime)
- [ ] Pods, ReplicaSets, Deployments (rolling updates, rollbacks, strategy types)
- [ ] Services (ClusterIP, NodePort, LoadBalancer), Endpoints, DNS
- [ ] ConfigMaps & Secrets, namespaces, labels & selectors
- [ ] **Lab:** Deploy app on minikube/K3s: Deployment + Service + ConfigMap + Secret, scale it, roll it back
- [ ] **Quiz 2.4 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/k8s-core`

### M2.5 K8s Intermediate
- [ ] Ingress & Ingress controllers (nginx), TLS
- [ ] Storage: PV/PVC, storage classes
- [ ] Probes: liveness/readiness/startup; resource requests/limits; HPA
- [ ] kubectl power: get/describe/logs/exec/port-forward/apply vs create, `-o yaml`, `--dry-run`
- [ ] Troubleshooting drill: crashloop, image pull backoff, pending pods, node not ready
- [ ] **Lab:** nginx-ingress + cert, HPA under load (hey/wrk), survive a node drain
- [ ] **Quiz 2.5 ≥80%** + Defend · **Recall:** 5+ cards 🗂️ `mira::2-containers/k8s-intermediate`

### M2.6 Helm
- [ ] Charts, values, templates, release lifecycle (upgrade/rollback), repo add/install
- [ ] **Lab:** Deploy app via Helm chart, override values, rollback
- [ ] **Quiz 2.6 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::2-containers/helm`

✅ **Milestone 3 (end of Phase 2):** Mock interview #3 — Docker+K8s (45 min, strict) + **Project P2**

### 📦 PROJECT P2 (resume piece #2): Dockerized full-stack app + compose + ECR pipeline
Complete local compose stack → CI build + scan → push ECR.

---

## PHASE 3 — Infrastructure as Code (Weeks 13–16)

### M3.1 Terraform Core
- [ ] HCL syntax, providers, resources, data sources, variables, outputs, locals
- [ ] `init / plan / apply / destroy` lifecycle, state file & state locking
- [ ] **Lab:** Rebuild your Phase-1 VPC with Terraform (this is the skill interviewers demand)
- [ ] **Quiz 3.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::3-iac/terraform-core`

### M3.2 Terraform State & Remote Backends
- [ ] Why remote state, S3 backend + DynamoDB locking, state commands, `terraform import`
- [ ] Workspaces, modules (input/output), functions, `for_each` vs `count`
- [ ] **Lab:** Remote state with locking, extract a reusable VPC module, destroy everything cleanly
- [ ] **Quiz 3.2 ≥80%** + Defend · **Recall:** 5+ cards 🗂️ `mira::3-iac/terraform-state`

### M3.3 Ansible (config management awareness)
- [ ] Inventory, playbooks, modules, handlers, roles; ad-hoc commands
- [ ] **Lab:** Configure EC2 instances with Ansible (nginx + app deploy), idempotency proof
- [ ] **Quiz 3.3 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::3-iac/ansible`

### M3.4 CloudFormation (awareness, interview mentions)
- [ ] Template anatomy, stack lifecycle; Terraform vs CloudFormation comparison (interview classic)
- [ ] **Quiz 3.4 ≥80%** (short) · **Recall:** 3+ cards 🗂️ `mira::3-iac/cloudformation`

✅ **Milestone 4:** Mock interview #4 — IaC (30 min) + **Project P3**

### 📦 PROJECT P3 (resume piece #3): 3-tier app on AWS, 100% Terraform
VPC (2 AZ) + ALB + ASG + RDS + S3 + secrets, modules, remote state. This is the project that lands interviews.

---

## PHASE 4 — CI/CD (Weeks 16–19)

### M4.1 CI/CD Concepts
- [ ] CI vs CD vs CDE; pipeline stages; artifacts; environments (dev/stage/prod); gating
- [ ] **Quiz 4.1 ≥80%** (short, conceptual) · **Recall:** 3+ cards 🗂️ `mira::4-cicd/concepts`

### M4.2 GitHub Actions — *deep, this is your primary tool*
- [ ] Workflows: events, jobs, steps, runners, matrix, caching, artifacts, environments
- [ ] Secrets & variables, OIDC to AWS (no long-lived keys!), concurrency, reusable workflows
- [ ] **Lab:** CI (lint→test→build→scan→push ECR) + CD (deploy to EC2/ECS) with OIDC
- [ ] **Quiz 4.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::4-cicd/gh-actions`

### M4.3 Jenkins (legacy awareness — still in 60% of job ads)
- [ ] Pipeline as code (declarative), agents, stages, plugins, credentials
- [ ] **Lab:** Same pipeline in Jenkins against a local agent
- [ ] **Quiz 4.3 ≥80%** (awareness level) · **Recall:** 3+ cards 🗂️ `mira::4-cicd/jenkins`

### M4.4 GitOps with ArgoCD
- [ ] GitOps principles, ArgoCD app of apps, sync policies, drift detection
- [ ] **Lab:** ArgoCD on minikube: app deploys from Git, revert = git revert
- [ ] **Quiz 4.4 ≥80%** + Defend · **Recall:** 5+ cards 🗂️ `mira::4-cicd/gitops`

✅ **Milestone 5:** Mock interview #5 — CI/CD + GitOps (40 min, strict) + **Project P4**

### 📦 PROJECT P4 (resume piece #4): Full CI/CD + GitOps pipeline
GitHub Actions (OIDC) → ECR → ArgoCD/ECS deploy, blue/green or canary, rollback drill.

---

## PHASE 5 — Observability (Weeks 19–21)

### M5.1 Prometheus + Grafana
- [ ] Metrics model, exporters, service discovery, PromQL basics, alerting (Alertmanager)
- [ ] Grafana dashboards, data sources, annotations
- [ ] **Lab:** Monitor the Phase-2 cluster: node/app metrics, custom dashboard, alert fires
- [ ] **Quiz 5.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::5-observability/prometheus`

### M5.2 Logging
- [ ] Log aggregation concepts; ELK/OpenSearch (ingest, index, search) or Loki; EFK on k8s
- [ ] AWS: CloudWatch Logs, Log Insights, S3 log archival
- [ ] **Lab:** Centralize app logs, search them, alert on error pattern
- [ ] **Quiz 5.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::5-observability/logging`

### M5.3 Tracing & SLOs (awareness)
- [ ] Distributed tracing (Jaeger/Tempo), OpenTelemetry, golden signals, SLI/SLO/SLA
- [ ] **Quiz 5.3 ≥80%** (short) · **Recall:** 3+ cards 🗂️ `mira::5-observability/tracing`

✅ **Milestone 6:** Mock interview #6 — Observability (30 min)

---

## PHASE 6 — Advanced AWS + Security + Cost (Weeks 21–24)

### M6.1 ECS & EKS on AWS
- [ ] ECS: task definitions, Fargate vs EC2, service autoscaling, ECS vs EKS decision
- [ ] EKS: managed control plane, node groups, IAM roles for pods, spot nodes
- [ ] **Lab:** Deploy containerized app to ECS Fargate with ALB; repeat on EKS (minikube skills transfer)
- [ ] **Quiz 6.1 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/ecs-eks`

### M6.2 Secrets & Security
- [ ] AWS Secrets Manager vs SSM Parameter Store, KMS (CMK vs AWS-managed)
- [ ] DevSecOps: SAST (Semgrep/SonarQube), dependency scan (OWASP), container scan (Trivy) in pipeline, SBOM
- [ ] **Quiz 6.2 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/security`

### M6.3 Well-Architected + Cost Optimization
- [ ] 6 pillars (operational excellence, security, reliability, performance, cost, sustainability)
- [ ] Cost: savings plans, spot, rightsizing, S3 lifecycle, billing alerts; FinOps basics
- [ ] **Quiz 6.3 ≥80%** + Defend · **Recall:** 5+ cards 🗂️ `mira::6-advanced/cost`

### M6.4 Systems Design & Migration (interview gold)
- [ ] Design a scalable app architecture on AWS (diagram + reasoning: VPC, multi-AZ, ASG, caching, CDN, DB tier)
- [ ] Migration patterns (lift-and-shift, re-platform, re-architect)
- [ ] **Quiz 6.4 ≥80%** · **Recall:** 5+ cards 🗂️ `mira::6-advanced/design`

✅ **Milestone 7:** Mock interview #7 — Full scenario design (45 min, whiteboard-style)

---

## PHASE 7 — Interview Bootcamp (Weeks 24–28)

- [ ] **Question bank:** 200+ questions across ALL modules — drilled via spaced repetition (Anki) until 90%+ hit rate
- [ ] **Mock interviews:** 5 full-length mocks (45 min each): Linux/git, Docker/K8s, AWS, CI/CD+IaC, mixed senior panel
- [ ] **Scenario rounds:** "Your app is slow / down / leaking secrets — what do you do?" diagnosis drills
- [ ] **Behavioral:** STAR answers, "tell me about a time you broke prod", ownership stories (use real journal/project incidents)
- [ ] **Resume + portfolio:** finalize 4 projects with READMEs, diagrams, and a live demo URL
- [ ] **Salary/negotiation prep:** local/remote market rates for 1–2 yr DevOps
- [ ] **Capstone review:** full walkthrough of every project, every decision defended

✅ **Graduation:** "I certify the student as interview-ready for 1–2 yr experienced DevOps roles."

---

## The 4 Portfolio Projects (resume pieces)

| # | Project | Tech | When |
|---|---|---|---|
| P1 | Static site: S3 + CloudFront + Route53 + CI/CD | AWS, GH Actions | End Phase 1 |
| P2 | Full-stack app dockerized + ECR pipeline | Docker, Compose, ECR | End Phase 2 |
| P3 | 3-tier app on AWS, 100% Terraform | Terraform, AWS | End Phase 3 |
| P4 | Full CI/CD + GitOps (OIDC → ECR → ArgoCD) | GH Actions, ArgoCD, EKS/ECS | End Phase 4 |

Every project gets: working code, README with architecture diagram, deployment runbook, and a "what I'd improve" section. That last part is what makes interviewers lean in.

---

*v1.3.0: added Anki Recall checkpoints (5+ cards/module), deck naming convention, and completion criteria alignment with the Recall phase.*
