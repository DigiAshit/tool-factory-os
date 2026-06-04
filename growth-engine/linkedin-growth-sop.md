---
id: growth-engine/linkedin-growth-sop
version: 2
owner_role: [LinkedIn Strategist, Founder]
trigger: { type: scheduled, cadence: daily, window: 08:00-10:00 local }
inputs:
  - { name: product_state,   source: _shared scorecard }
  - { name: recent_metrics,  source: posthog + stripe }       # MRR/WAU/cost deltas, wins AND losses
  - { name: discovery_log,   source: opportunity-engine/discovery-log }
  - { name: launch_assets,   source: growth-engine/launch-sop (launch days only) }
state:
  reads:  artifacts/{product}/linkedin/state.json
  writes: artifacts/{product}/linkedin/state.json
tools_allowed: [linkedin_api_post, linkedin_api_comment, linkedin_api_dm, posthog_read, stripe_read, link_shortener, screenshot_grab]
outputs:
  - { name: post_draft,   artifact: artifacts/{product}/linkedin/post-{date}.md }
  - { name: reply_log,    artifact: artifacts/{product}/linkedin/replies-{date}.jsonl }
  - { name: dm_log,       artifact: artifacts/{product}/linkedin/dms-{date}.jsonl }
  - { name: daily_report, artifact: artifacts/{product}/linkedin/report-{date}.json }
guardrails:
  links_in_post:  ref:_shared/metrics.yaml#platform_guardrails.linkedin_links_in_post   # = 0; link goes in first comment
  dms_per_day:    ref:_shared/metrics.yaml#platform_guardrails.linkedin_warm_dms_per_day
  hitl_gate: true
  identity: numbers come from scorecard only; never fabricate
eval: { rubric: _shared/content-eval-rubric.yaml, applies_to: [post_draft, reply_log], block_publish_below: 0.80 }
depends_on:
  - _shared/metrics.yaml
  - _shared/content-eval-rubric.yaml
  - growth-engine/founder-authority-sop
  - growth-engine/distribution-sop       # 15-min reply rule
  - growth-engine/product-promotion-sop  # DM templates
escalation:
  - eval blocks 2x -> escalate to human with required_edits
  - post flagged / reach throttled -> log incident to daily_report
done_when:
  - 1 post_draft passes eval (>=0.80) AND human-approved, posted once in the morning window
  - outbound link placed in the FIRST COMMENT (never the post body)
  - >=3 value-first comments logged on others' posts within the 15-min window
  - DMs <= cap; daily_report written
---

# Growth Engine — LinkedIn Growth (Journey-Based)

Build organic distribution by documenting the raw founder journey. No generic business
advice, no press releases. Positioning inherited from `founder-authority-sop`.

## 1. Daily output target
- 1 journey post (section 3), posted once in the 08:00–10:00 window.
- ≥3 value-first comments on others' posts (use `distribution-sop`'s 15-min rule).
- ≤ cap warm DMs via `product-promotion-sop` templates.

## 2. Content pillars (rotate; don't repeat two days running)
1. **Revenue updates** — recent MRR gains *and* losses, with the cause.
2. **Behind-the-scenes building** — raw UI iterations, a codebase simplification, a co-founder debate.
3. **Feature pauses/kills** — why you killed/paused something and the lesson.
4. **Operational insights** — automation, systems, holding-company structure.

## 3. Post format
1. **Hook:** one high-impact line with a specific, sourced metric.
   - "We spent $1,200 on API costs last month. Here's exactly what we learned about scaling AI wrappers."
2. **Body:** short, punchy — max ~2 lines per paragraph. Problem → test → result → rule.
3. **Close:** one interactive question ("How do you handle API cost scaling? Reply below.").
4. **Link:** in the **first comment**, never in the post body (see `links_in_post` guardrail —
   placing links in-body triggers reach penalties).

## 4. Engagement & DMs
- Comment value-first on target accounts (no "Great post!"); inherit the 15-min window
  and spacing from `distribution-sop`.
- Move warm repliers to DMs via `product-promotion-sop`, within `dms_per_day`.

## 5. Pre-publish gate
Score `post_draft` + comments with the rubric; block < 0.80 with `required_edits`.
After passing, route to HITL approval. Nothing posts under the founder identity unapproved.

## 6. Exit
Complete only on all `done_when` conditions. On an unfixable block, log to
`daily_report` and exit without posting.
