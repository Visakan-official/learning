# INTERVIEW DRILLS — the question bank that decides the offer

**How this works (Rule 4 — evidence over claims):** every question is answered **out loud, cold, timer running**. A question is `[x]` only when I've heard the answer twice, clean, on different days. `[~]` = answered once. Blank = not yet.

Target: [ ] 100+ answered · [ ] whole file twice · [ ] hardest 20 a third time, the week of an interview.

Chennai 1–2 yr DevOps loops lean **scenario**, not trivia. So most of these are "X is broken, go" and "why would you choose Y".

---

## A. Linux & troubleshooting (the gate — miss these and the loop ends)

- [ ] 1. Production server: disk is 100% full. Walk me through it, in order.
- [ ] 2. A service won't start. `systemctl status` shows `failed`. What are your next 3 commands?
- [ ] 3. Something is eating all the CPU. How do you find it, and what do you do before killing it?
- [ ] 4. Memory is exhausted and the OOM killer is firing. How do you confirm that's what happened?
- [ ] 5. "Port 8080 is already in use" when starting your app. Find the culprit and free it.
- [ ] 6. `Permission denied` on a file that is `644`. Give three possible causes.
- [ ] 7. What does `namei -l` show, and when would you reach for it?
- [ ] 8. Difference between a hard link and a symlink. What breaks when the target moves?
- [ ] 9. `df` says the disk is full but `du` doesn't add up. Why? What do you check?
- [ ] 10. How do you find and delete files older than 30 days in a directory tree?
- [ ] 11. Explain `journalctl -u nginx --since "10 min ago"` and two other flags you use.
- [ ] 12. What is `umask 027` and what modes does it produce for files and directories?
- [ ] 13. A cron job runs fine by hand but never from cron. Name the three usual causes.
- [ ] 14. Write a 6-line bash script that checks a service and writes an alert if it's down.
- [ ] 15. What does `set -euo pipefail` do and why do you put it at the top of scripts?

## B. Networking

- [ ] 16. What happens, end to end, when you type `https://app.example.com` and press Enter?
- [ ] 17. TCP vs UDP — one real example of each, and why you'd pick it.
- [ ] 18. Explain the TLS handshake in 60 seconds. Where does the certificate come in?
- [ ] 19. What's the difference between a load balancer and a reverse proxy? L4 vs L7?
- [ ] 20. Split `10.0.4.130/26` — network, broadcast, usable range. Do it in your head.
- [ ] 21. Private vs public IPs. How does a private-subnet instance reach the internet?
- [ ] 22. DNS: A vs CNAME vs alias. Why does a CNAME at the apex fail?
- [ ] 23. A host is unreachable. Order of commands you run to bisect it.
- [ ] 24. What's a 502 from an ALB telling you? And a 504?
- [ ] 25. How do health checks work, and what's the difference between a liveness and a readiness probe (same idea, different layer)?

## C. AWS core

- [ ] 26. Design a 3-tier VPC. Justify every route table and security-group rule.
- [ ] 27. Security groups vs NACLs — stateful vs stateless, and where each applies.
- [ ] 28. Instance in a private subnet can't reach the internet. Diagnose it.
- [ ] 29. Difference between IAM user, group, role, and policy. When do you use a role?
- [ ] 30. Write (or explain) a least-privilege policy allowing read of one S3 prefix.
- [ ] 31. Why are root access keys banned, and what do you do instead?
- [ ] 32. EC2 won't boot / can't SSH. Triage it.
- [ ] 33. gp2 vs gp3 vs io2 — when does each make sense?
- [ ] 34. Snapshot vs AMI vs backup plan. How do you restore a volume from a snapshot?
- [ ] 35. ALB vs NLB vs Classic — pick one for a WebSocket service and defend it.
- [ ] 36. ASG: how does scaling actually work, and what's a cooldown for?
- [ ] 37. Traffic spikes every day at 9 AM. How do you make the ASG react before users notice?
- [ ] 38. S3 bucket policy vs ACL vs block-public-access — what wins?
- [ ] 39. How do you give a third party 24-hour access to one file in a private bucket?
- [ ] 40. Versioning + lifecycle: reduce S3 cost for logs while keeping 1 year of archives.
- [ ] 41. RDS Multi-AZ vs read replica — which solves which problem?
- [ ] 42. Your DB is at 90% CPU with read-heavy traffic. What do you do?
- [ ] 43. Point-in-time recovery: what is it, and what does it depend on?
- [ ] 44. CloudWatch metrics vs logs vs alarms — and how do you alert a human?
- [ ] 45. Billing metrics live in exactly one region. Which, and why does that matter?
- [ ] 46. Route 53 weighted vs failover vs latency routing — one use case each.
- [ ] 47. How do you serve a static site with a custom domain over HTTPS, cheapest sane way?
- [ ] 48. What's IMDSv2 and why enforce it?
- [ ] 49. When would you *not* use Lambda?
- [ ] 50. Something in prod broke at 2 AM. How do you find out, and what's your first move?

## D. Docker

- [ ] 51. Container vs VM — what's actually shared, what's isolated?
- [ ] 52. Explain image layers and why build order matters for cache hits.
- [ ] 53. Your image is 1.4 GB. Get it under 150 MB without breaking it.
- [ ] 54. Entrypoint vs CMD vs RUN. Which one runs at container start?
- [ ] 55. A container exits immediately with code 0. Why? How do you debug it?
- [ ] 56. Named volume vs bind mount — where does data live on the host, and what survives `docker rm`?
- [ ] 57. Two containers must talk to each other. How do they resolve each other's names?
- [ ] 58. How do you pass secrets into a container without baking them into the image?
- [ ] 59. What does `docker system prune -a` delete, and why is it dangerous on a shared host?
- [ ] 60. Container can't reach the internet but the host can. Diagnose.
- [ ] 61. Explain Compose `depends_on` vs `healthcheck` — why isn't depends_on enough?
- [ ] 62. Multi-stage build: what problem does it solve, and show the skeleton.

## E. Kubernetes

- [ ] 63. Walk me through what happens from `kubectl apply -f deploy.yaml` to a running pod.
- [ ] 64. Pod is in `CrashLoopBackOff`. Go.
- [ ] 65. Pod is in `ImagePullBackOff`. Go.
- [ ] 66. Pod is stuck `Pending`. Give five reasons.
- [ ] 67. A pod gets `OOMKilled`. How do you confirm, and what are your two fixes?
- [ ] 68. Service exists but requests hang — no endpoints. Why?
- [ ] 69. Pods can't resolve `db.default.svc.cluster.local`. Debug it.
- [ ] 70. Deployment rollout is stuck at 1/3. How do you find out why?
- [ ] 71. Liveness vs readiness vs startup probe — give an example where mixing them up causes an outage.
- [ ] 72. Difference between ClusterIP, NodePort, LoadBalancer. When is Ingress the better answer?
- [ ] 73. ConfigMap vs Secret: is a Secret actually secret? What do you do instead for real secrets?
- [ ] 74. Requests vs limits: what happens when a container exceeds each?
- [ ] 75. HPA isn't scaling. What do you check?
- [ ] 76. Explain PV, PVC and StorageClass with a database example. Why StatefulSet?
- [ ] 77. How do you do a zero-downtime deploy in K8s? What does `maxSurge`/`maxUnavailable` control?
- [ ] 78. Rollback a bad deploy — command, and what happens to the old ReplicaSet.
- [ ] 79. Taints/tolerations vs node affinity — which problem does each solve?
- [ ] 80. What's in the control plane, and what happens if etcd dies?
- [ ] 81. A ServiceAccount can't list pods. How do you fix it with RBAC?
- [ ] 82. What does `helm rollback` do, and where does Helm store release state?

## F. Terraform / IaC

- [ ] 83. Why does Terraform need state? What's in it?
- [ ] 84. Two engineers apply at once. What happens and how do you prevent it?
- [ ] 85. Someone deleted a resource in the console. How do you reconcile?
- [ ] 86. `terraform import` — when, and what does it *not* do?
- [ ] 87. `count` vs `for_each`: which breaks when you remove the middle element?
- [ ] 88. How do you keep secrets out of Terraform code and state?
- [ ] 89. What's a module, and when does creating one become a bad idea?
- [ ] 90. Explain the dependency graph: implicit vs `depends_on`.
- [ ] 91. Terraform vs CloudFormation vs Ansible — one line each, then when you'd mix them.
- [ ] 92. Your plan wants to destroy the prod database. What do you do in the next 30 seconds?

## G. CI/CD

- [ ] 93. CI vs CD vs continuous deployment — drawn as a pipeline.
- [ ] 94. Design a pipeline: lint → test → build → push → deploy → smoke test, with a rollback gate.
- [ ] 95. How does CI authenticate to AWS without storing access keys? (OIDC)
- [ ] 96. Rolling vs blue-green vs canary — trade-offs, and which you'd pick for a payments API.
- [ ] 97. How do you roll back a bad deploy in 60 seconds? (each strategy)
- [ ] 98. Jenkins controller/agent architecture. Why not build on the controller?
- [ ] 99. Declarative vs scripted pipeline. What's in a `Jenkinsfile` `post` block?
- [ ] 100. Jenkins vs GitHub Actions — when would you choose either?
- [ ] 101. A pipeline is green but the app is broken in prod. How is that possible, and what do you add?
- [ ] 102. How do you handle DB migrations in a pipeline with zero downtime?
- [ ] 103. How do you keep CI secrets out of logs?
- [ ] 104. GitOps: what does ArgoCD actually do, and how is it different from a push pipeline?

## H. Observability & reliability

- [ ] 105. How do you know your service is healthy right now? (metrics → logs → traces)
- [ ] 106. Prometheus pull model vs push. Why exporters?
- [ ] 107. Write (or explain) a PromQL alert for error rate > 5% over 5 minutes.
- [ ] 108. What would you put on a service dashboard? (USE/RED)
- [ ] 109. Logs are costing more than the service. What do you do?
- [ ] 110. Define SLI, SLO, error budget — and what you do when the budget is exhausted.
- [ ] 111. Postmortem blameless structure in 30 seconds.
- [ ] 112. Alert fatigue: how do you fix too many alerts?

## I. Project deep-dive + behavioural (decides the offer)

- [ ] 113. Walk me through P1/P2/P3 in 3 minutes each — problem, design, build, breakage, fix, result.
- [ ] 114. What was the hardest bug in your project, and how did you find it?
- [ ] 115. What would you improve if you rebuilt it? (must be specific, not "more tests")
- [ ] 116. How much does your project cost per month, and how would you halve it?
- [ ] 117. You've never worked in a team — how do you know you can? (STAR: collab story)
- [ ] 118. Tell me about a time you broke something and owned it.
- [ ] 119. Prod is down, manager and customer are pinging you — what do you say and do?
- [ ] 120. Why should we hire you over someone with 2 years of experience?
- [ ] 121. Where do you want to be in 2 years, and what are you learning now?
- [ ] 122. You're handed a service you've never seen and on-call for it tonight. What do you do in the first hour?

---

**Scoring a drill answer (how I grade it):**
- **Correct + complete + <90 s** → `[x]` candidate (needs a second clean pass on another day)
- **Correct but rambling / missed a consequence** → `[~]`, goes to `question-bank.md`
- **Wrong, or "chmod 777 fixed it" style** → miss. Logged, re-asked until twice clean.
