# QUESTION BANK — spaced repetition queue

Every question Visakan misses goes here. Mira re-asks missed questions at the start of
every session (Phase 0, alongside Anki due cards) until answered correctly twice in a row.
Mirrored in Anki as the `mira::missed` deck — the Anki copy is the daily-driver; this file
is the git-tracked record.

## Format

- [ ] **Q:** question | **A:** answer | module: M0.1 | missed: 2026-08-10
- `[ ]` = still missed · `[x]` = answered correctly twice in a row

## Missed questions

- [ ] **Q:** Your resources run in ap-south-2. Where must a CloudWatch alarm on `EstimatedCharges` (billing) be created — and what statement about CloudWatch in other regions is FALSE? | **A:** **us-east-1 only** (the `AWS/Billing` metric exists nowhere else; console selector = N. Virginia). FALSE to say "CloudWatch can't be used in ap-south-2" — CloudWatch works in every region for other metrics; only the *billing* metric is us-east-1-exclusive. | module: M0.1 / Day-0 AWS | missed: 2026-09-13 (imprecise phrasing) | Anki: noteId 1789288649490
- [ ] **Q:** `t3.small` is not free-tier eligible (only t2.micro/t3.micro are). What does that mean for the t3.small already running in this account? | **A:** It is **not free tier** — it bills ~$30/mo on-demand against the credits. It runs the student's **production** Hermes/Telegram agent → never stop/terminate/reboot/modify it; cost control happens by destroying *lab* resources each session instead. | module: M0.1 / Day-0 AWS | missed: 2026-09-13 (question half-answered) | Anki: noteId 1789288649491

