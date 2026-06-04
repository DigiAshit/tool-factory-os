---
# CONTRACT. CANONICAL owner of warm-DM templates + outreach rules.
id: growth-engine/product-promotion-sop
version: 2
owner_role: [Twitter Strategist, Growth Strategist]
trigger:
  type: event
  on: warm_lead_available        # from distribution-sop / launch-sop / twitter-growth-sop
inputs:
  - { name: warm_leads, source: artifacts/{product}/**/leads-*.jsonl }   # engagers only
  - { name: discovery_log, source: opportunity-engine/discovery-log }
state:
  reads:  artifacts/{product}/dm/state.json     # sent counts, statuses, inactive marks
  writes: artifacts/{product}/dm/state.json
tools_allowed: [x_api_dm, linkedin_api_dm, link_shortener]
outputs:
  - { name: dm_log, artifact: artifacts/{product}/dm/dms-{date}.jsonl }   # feeds Customer Researcher
guardrails:
  x_dms_per_day:        ref:_shared/metrics.yaml#platform_guardrails.x_warm_dms_per_day
  linkedin_dms_per_day: ref:_shared/metrics.yaml#platform_guardrails.linkedin_warm_dms_per_day
  cold_spam: forbidden            # ONLY message people who engaged a competitor launch or a pain thread
  pii: every lead row must carry source + consent_basis; no DMs to non-engagers
  hitl_gate: true                 # approval before sending under founder identity
eval: { rubric: _shared/content-eval-rubric.yaml, applies_to: [dm_log], block_publish_below: 0.80 }
depends_on: [_shared/metrics.yaml, _shared/content-eval-rubric.yaml, growth-engine/founder-authority-sop]
done_when:
  - all sends within per-platform caps
  - responders supported within 1h; non-responders marked inactive after 4 days (no repeat follow-ups)
  - every DM + response appended to dm_log
---

# Growth Engine — Product Promotion (Warm DMs)

Canonical home of the warm-DM motion. Other skills route engagers here; they must not
write their own pitch copy.

## Eligibility (no cold spam)
Only DM someone who (a) engaged a competitor launch, or (b) raised a hand on a pain
thread. Every lead must carry `source` + `consent_basis`. Never DM strangers.

## Style
- Under 3 sentences. No corporate greeting. Address the specific pain immediately and
  offer a frictionless test. Positioning inherited from `founder-authority-sop`.

## Templates
**A — Competitor engager**
> "Hey {Name}, saw you upvoted/commented on {Competitor}'s launch. We built a lean
> wrapper, {Product}, that does {single core workflow} in 1 click (cuts out {pain}).
> Want to try it? I can unlock {trial credit / founder tier} for you."

**B — Pain-thread hand-raiser**
> "Hey {Name}, saw your post about hating {frustration}. We built {Product} to automate
> exactly that for our own workflow. Quick link to try: [URL] — does it kill the pain?"

## Execution rules
1. Volume ≤ per-platform caps (see metrics.yaml; X and LinkedIn tracked separately in `state.json`).
2. If they respond, support within **1 hour**. If silent after **4 days**, mark inactive —
   **no repeat follow-ups**.
3. Append every DM + response to `dm_log` for the Customer Researcher.
4. Every outbound DM passes the rubric + HITL gate before sending.

## Exit
Complete when `done_when` is satisfied.
