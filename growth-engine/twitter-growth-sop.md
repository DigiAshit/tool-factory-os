---
# CONTRACT (machine-readable). Human SOP follows.
id: growth-engine/twitter-growth-sop
version: 3
owner_role: Twitter Strategist
trigger:
  type: scheduled
  cadence: daily
  window: 08:00-10:00 local (primary post); replies throughout day
inputs:
  - name: product_state          # current product(s) in Scale phase + this week's metric deltas
    source: _shared scorecard
  - name: discovery_log          # verbatim user-frustration language
    source: opportunity-engine/discovery-log
  - name: recent_metrics         # MRR, WAU, API cost, churn deltas vs last week
    source: posthog + stripe
  - name: launch_assets          # optional, only on launch days
    source: growth-engine/launch-sop
state:
  reads:  artifacts/{product}/x/state.json    # account lists, last-posted, in-flight DMs, used hooks
  writes: artifacts/{product}/x/state.json
tools_allowed: [x_api_post, x_api_reply, x_api_dm, posthog_read, stripe_read, link_shortener, screenshot_grab]
outputs:
  - { name: thread_draft,   artifact: artifacts/{product}/x/thread-{date}.md }
  - { name: standalone,     artifact: artifacts/{product}/x/tweets-{date}.md }
  - { name: reply_log,      artifact: artifacts/{product}/x/replies-{date}.jsonl }
  - { name: dm_log,         artifact: artifacts/{product}/x/dms-{date}.jsonl }
  - { name: daily_report,   artifact: artifacts/{product}/x/report-{date}.json }   # appended to scorecard
guardrails:                       # canonical values: _shared/metrics.yaml#platform_guardrails
  warm_dms_per_day:   ref:_shared/metrics.yaml#platform_guardrails.x_warm_dms_per_day
  reply_min_spacing:  ref:_shared/metrics.yaml#platform_guardrails.reply_cadence_min_minutes_between
  hitl_gate: true                 # human approval REQUIRED before anything posts/DMs under founder identity
  pii: scraped engager lists must record source + consent basis; no DMs to non-engagers
  identity: never fabricate a metric; numbers come from scorecard/stripe/posthog only
eval:
  rubric: _shared/content-eval-rubric.yaml
  applies_to: [thread_draft, standalone, reply_log]
  block_publish_below: 0.80
depends_on:
  - _shared/metrics.yaml
  - _shared/content-eval-rubric.yaml
  - growth-engine/founder-authority-sop      # positioning rules (inherited, not restated)
  - growth-engine/distribution-sop           # canonical 15-min reply placement rule
  - growth-engine/product-promotion-sop      # canonical warm-DM templates
escalation:
  - if eval blocks 2x on same draft -> escalate to human with required_edits
  - if a reply/post is flagged or rate-limited -> pause channel, write incident to daily_report
done_when:
  - 1 thread_draft AND >=1 standalone pass eval (>=0.80) AND are human-approved
  - >=5 value-first replies logged within cadence + spacing guardrails
  - DMs sent <= daily cap; every DM + response appended to dm_log for Customer Researcher
  - daily_report written with the KPIs in section 9
---

# Growth Engine — Twitter (X) Growth SOP

## 1. Purpose & scope
Run daily by the **Twitter Strategist** to grow organic distribution for the
product(s) currently in the Scale phase, using a build-in-public motion. This skill
covers original threads, standalone tweets, reply-based distribution, and the handoff
of warm leads into DMs. Positioning rules are inherited from `founder-authority-sop`;
all hard numbers (caps, commitments, metric definitions) come from
`_shared/metrics.yaml`. Every draft is scored by `_shared/content-eval-rubric.yaml`
before a human approves the post.

## 2. Daily output target (the mix)
Produce per day, per active product:
- **1 original thread** (section 4) — the anchor asset.
- **1–2 standalone tweets** (section 5) — quick wins between threads.
- **5 value-first replies** (section 6) — borrowed-audience distribution.
- **≤ cap warm DMs** (section 7) — only to people who engaged today.

Maintain a rough **70/30 split**: 70% pure value/build-in-public, 30% product-adjacent.
Never two consecutive promotional posts.

## 3. Content pillars (rotate; don't repeat a pillar two days running)
1. **Revenue/usage updates** — real deltas, wins *and* losses ("MRR dipped $200, here's why").
2. **Build teardowns** — a screenshot of a UI iteration, a query, a cost optimization.
3. **Contrarian lesson** — a heuristic you changed your mind on, with the data that moved you.
4. **Demo moment** — a 15–30s clip of the core workflow producing an outcome in one click.
5. **Cost/ops transparency** — API spend, latency wins, infra decisions.

## 4. Thread construction (build-in-public, 6-tweet scaffold)
Pull this week's real metric deltas first; if no real number exists for the hook,
switch pillars — do **not** invent one.

1. **Tweet 1 — Hook (the outcome):** one contrarian truth or a specific, sourced result.
   - *Template:* "We grew {Product} to {$MRR} in {N} days with {constraint, e.g. 0 ads}. Here's the exact system:"
2. **Tweet 2 — Backstory (the pain):** the frustration in the user's own words from the discovery log.
   - *Template:* "I spent {N hours} every {cadence} doing {manual task}. Stupid waste of time. So we scoped a wrapper."
3. **Tweets 3–5 — The system (the steps):** 3 concrete steps, each with a UI clip, query, or diagram.
   - *Template:* "Step {i}: {action} → {result/metric}."
4. **Tweet 6 — CTA:** one direct link. Founder-pricing offers follow
   `_shared/metrics.yaml#commitments` (12-month lock — never "forever"). Cap any
   discount to a real, finite window.

Each claim in the thread must satisfy the rubric's `claim_backed` and
`positioning_different` dimensions.

## 5. Standalone tweet formats
- **One-metric drop:** a single sourced number + the one decision it changed.
- **Before/after:** "Old way: {N min}. New way: {1 click}. Same output."
- **Quote-the-user:** a verbatim discovery-log frustration, framed as "if this is you, we built for you."
Keep under 2 short lines. Link (if any) goes in a reply, not the tweet.

## 6. Reply-based distribution (borrowed audience)
1. Maintain a curated list of **5 mid-sized niche accounts (10k–100k followers)** in
   `state.json`. Refresh weekly; drop accounts whose audience isn't builders/creators/marketers.
2. **Placement window:** reply early per the canonical 15-minute rule in
   `distribution-sop` (don't restate the value here — reference it so it stays in sync).
3. **Value-first only:** a 2–3 sentence contribution that adds a concrete data point,
   clarifies a misconception, or shares a result. Never "Great thread!".
   - *Example:* "Saw this exact bottleneck — our logs showed 82% of latency was the formatting step. Gating that one script saved ~4h/week."
4. **Soft pitch (sub-reply, conditional):** only if your reply clears ~5+ likes, reply
   to *your own* comment with a soft link. One per thread, max.
5. Respect `reply_min_spacing` between replies to avoid throttling patterns.
6. Append every reply (target account, text, link?, engagement) to `reply_log`.

## 7. Warm-DM handoff
Trigger a DM only for someone who **engaged with you today** (replied, quote-tweeted,
or liked the soft pitch). Use the canonical templates in `product-promotion-sop`
(Template A: competitor engagers; Template B: pain-thread hand-raiser) — do not write
new pitch copy here.
- Volume: ≤ `x_warm_dms_per_day` (see metrics.yaml). No bulk/automated blasts.
- If they reply, support within 1h; if silent after 4 days, mark inactive — **no repeat follow-ups**.
- Append every DM + response to `dm_log` for the Customer Researcher.

## 8. Pre-publish gate (eval + HITL)
1. Score `thread_draft`, each `standalone`, and proposed replies against
   `_shared/content-eval-rubric.yaml`. Anything `< 0.80` is **blocked**; attach
   `required_edits` and re-draft.
2. After a draft passes the rubric, route to the **human approval gate**. Nothing
   posts or DMs under the founder identity without explicit approval.
3. On the second consecutive block of the same draft, escalate to a human (see
   `escalation` in the contract).

## 9. KPIs this skill owns (write to daily_report → scorecard)
- Thread impressions, profile clicks, link CTR to product.
- Replies posted, reply→profile-visit rate, sub-pitch conversions.
- Warm DMs sent / replied / converted to trial.
- Net new followers (context only; not a primary goal).
Primary objective is **clicks-to-product and warm DMs that start trials**, not vanity follows.

## 10. Exit
Complete only when every `done_when` condition (contract) is satisfied. If the eval
gate blocks a draft and it can't be fixed within the run, write the blocker to
`daily_report` and exit without publishing — never auto-publish a blocked or
unapproved asset.
