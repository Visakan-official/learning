# RESOURCES — curated per module (v1.3.0)

Rule: **docs first, courses second, videos last.** Real engineers read docs.
Videos are for concepts you can't grok from text. Don't binge — learn, then DO.

**v1.3.0 additions:** 🃏 Anki study resources · 🤖 NotebookLM feeding (upload these per phase)

---

## PHASE 0 — Foundations

### M0.1 Linux
- 📖 [Linux Journey](https://linuxjourney.com/) — free, perfect structured start
- 🎮 [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) — wargame; the best CLI practice on earth
- 📖 [The Linux Command Line (free PDF)](https://linuxcommand.org/tlcl.php) — the reference book
- 📖 [Bash Guide](https://mywiki.wooledge.org/BashGuide) — scripting done right
- 🎬 [TechWorld with Nana — Linux for DevOps](https://www.youtube.com/watch?v=Wgi0oygIOd0) (YouTube, free) — only if text bores you

### M0.2 Networking
- 📖 [Cloudflare Learning Center — Networking](https://www.cloudflare.com/learning/network-layer/what-is-the-osi-model/)
- 📖 [How DNS works](https://howdns.works/) — playful but correct
- 🎬 [freeCodeCamp — Computer Networking Course](https://www.youtube.com/watch?v=qiQR5rTSshw)

### M0.3 Git
- 📖 [Pro Git book (free)](https://git-scm.com/book/en/v2) — read ch 1–3, 5, 7
- 🎮 [Learn Git Branching](https://learngitbranching.js.org/) — interactive, do ALL of it
- 📖 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

---

## PHASE 1 — AWS Core
- 📖 **AWS docs per service** (IAM → EC2 → VPC → S3 → ELB/ASG → Route53 → RDS → Lambda). Search "[service] user guide".
- 🎬 [Adrian Cantrill — AWS Certified Solutions Architect](https://cantrill.io/) — paid, but the deepest AWS course that exists. Worth it for interview depth.
- 🎬 [freeCodeCamp — AWS Certified Solutions Architect full course](https://www.youtube.com/watch?v=Ia-UEYYR44s) (free fallback)
- 🎮 [AWS free tier](https://aws.amazon.com/free/) — YOUR lab. Use it. Destroy after use.
- 📖 [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — read the 6 pillars once in Phase 1, again in Phase 6.

### VPC deep-dives (interview killer — invest here)
- 📖 [AWS VPC user guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- 🎬 [freeCodeCamp — AWS Networking (VPC deep dive)](https://www.youtube.com/watch?v=HnN_eZgpCqI)

---

## PHASE 2 — Docker & Kubernetes

### Docker
- 📖 [Docker curriculum](https://docker-curriculum.com/) — the classic free path
- 📖 [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- 🎬 [TechWorld with Nana — Docker tutorial](https://www.youtube.com/watch?v=3c-iBn73dDE)

### Kubernetes
- 📖 [Kubernetes docs — concepts](https://kubernetes.io/docs/concepts/) (read: Architecture, Workloads, Services/Networking, Storage, Configuration)
- 📖 [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) — do the interactive ones
- 🎬 [TechWorld with Nana — Kubernetes course](https://www.youtube.com/watch?v=X48VuDVv0do) (free, excellent)
- 🎓 [KodeKloud — CKA course](https://kodekloud.com/) — paid; THE gold standard. Get it if you can; CKA syllabus ≈ interview syllabus.
- 🎮 [killer.sh](https://killer.sh/) — CKA exam simulators (paid, worth it near interview time)

### Helm
- 📖 [Helm docs — getting started](https://helm.sh/docs/)

---

## PHASE 3 — IaC
- 📖 [Terraform learn tutorials](https://developer.hashicorp.com/terraform/tutorials) — do ALL of the AWS ones
- 📖 [Terraform docs — language](https://developer.hashicorp.com/terraform/language)
- 🎬 [freeCodeCamp — Terraform course](https://www.youtube.com/watch?v=SLB_c_ayRMo)
- 📖 [Ansible docs — getting started](https://docs.ansible.com/ansible/latest/getting_started/index.html)
- 📖 [CloudFormation basics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) — awareness level only

---

## PHASE 4 — CI/CD
- 📖 [GitHub Actions docs](https://docs.github.com/en/actions) — workflows, environments, OIDC
- 📖 [OIDC to AWS in GH Actions](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
- 📖 [Jenkins — Pipeline getting started](https://www.jenkins.io/doc/book/pipeline/)
- 📖 [ArgoCD docs](https://argo-cd.readthedocs.io/en/stable/) — concepts + getting started

---

## PHASE 5 — Observability
- 📖 [Prometheus docs — getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)
- 📖 [PromQL basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- 📖 [Grafana docs](https://grafana.com/docs/)
- 📖 [OpenSearch docs](https://opensearch.org/docs/latest/) or [Loki docs](https://grafana.com/docs/loki/latest/)

---

## PHASE 6 — Advanced AWS + Security
- 📖 [ECS docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html), [EKS docs](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- 📖 [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- 📖 [OWASP Top 10](https://owasp.org/www-project-top-ten/) + [Trivy](https://aquasecurity.github.io/trivy/) + [Semgrep](https://semgrep.dev/)
- 📖 [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

---

## PHASE 7 — Interview Prep
- 📖 **Our own `question-bank.md`** — the primary weapon
- 🃏 **Your Anki collection** — `mira::*` decks are the daily-driver version of the question bank
- 📖 [roadmap.sh/devops](https://roadmap.sh/devops) — sanity-check your coverage
- 📖 [DevOps interview questions (KodeKloud blog)](https://kodekloud.com/blog/devops-interview-questions/) — extra drilling
- 📖 [STAR method](https://www.themuse.com/advice/star-interview-method) for behavioral answers

---

## 🃏 Anki & Spaced Repetition (v1.3.0)
- 📖 [How Anki works (spaced repetition explained)](https://docs.ankiweb.net/studying.html) — why Phase 0 exists
- 📖 [20 rules of formulating knowledge](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge) — how to write GOOD cards (Mira grades your cards against this)
- Card rule: **one fact per card, front = question, back = answer with the WHY.** No lazy cards.

## 🤖 NotebookLM (v1.3.0)
- Upload per phase: `RESOURCES.md`, your Obsidian notes for the phase, official AWS PDFs.
- Use the **Study Guide** mode + ask it "why" questions between sessions (Rule 13).
- One good Q+A per module comes back into the journal → becomes an Anki card.

---

## Tools you'll install (timeline)
| Week | Tool | Why |
|---|---|---|
| Day 0 | WSL2 + Ubuntu | Your Linux lab on Windows |
| Day 0 | AWS account + CLI | The cloud lab |
| Day 0 | VS Code + WSL ext | Editor |
| Day 0 | Anki + AnkiConnect + Anki MCP add-on | SRS (already done ✅) |
| Day 0 | Obsidian + AnkiSync+ plugin | Vault + card bridge |
| Phase 2 | Docker Desktop (WSL2 backend) | Containers |
| Phase 2 | minikube or K3s (in WSL2) | K8s lab |
| Phase 3 | Terraform, Ansible | IaC |
| Phase 4 | Jenkins (local), ArgoCD (in cluster) | CI/CD |
| Phase 5 | Prometheus, Grafana, Loki/OpenSearch | Observability |
