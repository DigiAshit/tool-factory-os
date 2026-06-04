---
# CONTRACT. CANONICAL owner of the conversation-piggybacking / reply-placement rule.
id: growth-engine/distribution-sop
version: 2
owner_role: [Twitter Strategist, LinkedIn Strategist]
trigger: { type: scheduled, cadence: daily }
inputs:
  - { name: target_accounts, source: state.json (curated list of 10-15 accounts) }
  - { name: notifications,   source: x_api + linkedin_api post alerts }
state:
  reads:  artifacts/{product}/distribution/state.json
  writes: artifacts/{product}/distribution/state.json
tools_allowed: [x_api_reply, linkedin_api_comment, posthog_read, link_shortener, screenshot_grab]
outputs:
  - { name: reply_log,    artifact: artifacts/{product}/distribution/replies-{date}.jsonl }
  - { name: warm_leads,   artifact: artifacts/{product}/distribution/leads-{date}.jsonl }  # handed to product-promotion-sop
  - { name: daily_report, artifact: artifacts/{product}/distribution/report-{date}.json }
canonical:
  reply_placement_window_minutes: 15     # SOURCE OF TRUTH; other skills reference this key
guardrails:
  reply_min_spacing: ref:_shared/metrics.yaml#platform_guardrails.reply_cadence_min_minutes_between
  no_promo_in_primary_reply: true
  hitl_gate: true                         # human approval before any soft-pitch link under founder identity
eval: { rubric: _shared/content-eval-rubric.yaml, applies_to: [reply_log], block_publish_below: 0.80 }
depends_on: [_shared/metrics.yaml, _shared/content-eval-rubric.yaml, growth-engine/founder-authority-sop, growth-engine/product-promotion-sop]
done_when:
  - target list has 10-15 active accounts
  - >=1 value-first reply per monitored thread, within the 15-minute window + spacing guardrail
  - qualifying engagers appended to warm_leads for the DM handoff
---

# Growth Engine — Distribution (Conversation Piggybacking)

Tap existing attention streams by being early and useful in other people's replies.
This SOP defines the canonical **15-minute reply placement window** that
`twitter-growth-sop` and `linkedin-growth-sop` reference.

## Step 1 — Monitor target accounts
- Curate 10–15 industry influencers / mid-sized accounts (10k–100k followers) who
  speak to our audience (creators, builders, marketers). Store in `state.json`.
- Turn on post alerts (mobile push or RSS) for each.

## Step 2 — The 15-minute response rule
- When a target posts a new thread, reply within **15 minutes** to secure high
  placement. (Canonical value: `canonical.reply_placement_window_minutes`.)
- **Constructive contribution:** 2–3 sentences that add a concrete data point or
  clarify a misconception. Inherit tone/positioning from `founder-authority-sop`.
  Do **not** promote the product in the primary reply.
  - Example: "We hit this exact bottleneck — logs showed 82% of latency was the
    formatting step. Gating that one script saved ~4h/week."
- Respect `reply_min_spacing` between replies (anti-throttling).

## Step 3 — Soft pitch (sub-reply, conditional)
- Only if your primary reply clears ~5+ likes, reply to *your own* comment with a
  soft link. One per thread, max. This link is a publish action → **HITL approval**.
  - Example: "We automated this into a tiny script — if you're stuck here, try it: [URL]"

## Step 4 — Handoff
- Append engagers who respond positively to `warm_leads`. The DM motion is owned by
  `product-promotion-sop` (templates + caps) — do not pitch in DMs from this skill.

## Exit
Complete when `done_when` is satisfied. Replies are scored by the rubric; blocked
replies are not posted.
