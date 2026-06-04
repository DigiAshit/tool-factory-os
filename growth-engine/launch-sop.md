---
id: growth-engine/launch-sop
version: 2
owner_role: [Growth Strategist, CEO]
trigger: { type: event, on: public_launch_day }
inputs:
  - { name: positioning,   source: growth-engine/founder-authority-sop }
  - { name: thread_asset,  source: growth-engine/twitter-growth-sop }      # uses the 6-tweet scaffold
  - { name: warm_list,     source: growth-engine/product-promotion-sop }   # mined competitor engagers
tools_allowed: [producthunt_post, x_api_post, linkedin_api_post, x_api_dm, linkedin_api_dm, posthog_read, stripe_read]
outputs:
  - { name: ph_assets,      artifact: artifacts/{product}/launch/producthunt.md }
  - { name: launch_posts,   artifact: artifacts/{product}/launch/posts.md }
  - { name: hourly_report,  artifact: artifacts/{product}/launch/hourly-{date}.jsonl }
guardrails:
  founder_pricing_lock_months: ref:_shared/metrics.yaml#commitments.founder_pricing_lock_months  # 12, not "forever"
  dm_caps: ref:_shared/metrics.yaml#platform_guardrails    # per product-promotion-sop
  hitl_gate: true                 # CEO + founder approve all launch-day assets
eval: { rubric: _shared/content-eval-rubric.yaml, applies_to: [launch_posts, ph_assets], block_publish_below: 0.80 }
depends_on:
  - _shared/metrics.yaml
  - _shared/content-eval-rubric.yaml
  - growth-engine/founder-authority-sop
  - growth-engine/twitter-growth-sop
  - growth-engine/product-promotion-sop
done_when:
  - PH live at 12:01 AM PST with clean assets + founder first comment
  - X thread + LinkedIn post published (LinkedIn link in first comment)
  - warm blast sent within caps; hourly metrics tracked for 24h; >=5 paying subs targeted
---

# Growth Engine — Launch Day

## Phase 1 — Product Hunt
1. Schedule launch for **12:01 AM PST**.
2. Clean, non-AI-looking screenshots demonstrating the core workflow step-by-step.
3. Founder first comment: why you built it (the raw frustration), the core moat, and a
   finite launch offer. Offer terms follow `founder_pricing_lock_months` — e.g. "first
   100 users lock founder pricing at $49/mo for 12 months" (never "forever").

## Phase 2 — Social distribution
1. **X thread:** publish the prepared thread built with `twitter-growth-sop`'s 6-tweet
   scaffold (outcome hook → backstory → steps → CTA).
2. **LinkedIn post:** journey-based; link in the **first comment**.
3. **Warm blast:** announce to the mined competitor-engager list using
   `product-promotion-sop` templates, within DM caps. No cold spam.

## 3. Metrics
Track visits, signups, and trial→paid hourly for the first 24h in `hourly_report`.
Target ≥ 5 paying subscribers from launch day.

## Gate
All launch assets pass the rubric + CEO/founder HITL approval before going live.

## Exit
Complete on all `done_when` conditions.
