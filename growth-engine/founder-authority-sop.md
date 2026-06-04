---
# CONTRACT. This is a STANDARD consumed by every content-producing skill.
id: growth-engine/founder-authority-sop
version: 2
type: standard                      # not scheduled; consulted + audited
owner_role: [LinkedIn Strategist, Twitter Strategist]
trigger:
  type: on_demand                   # consulted before any public asset is drafted
  audit_cadence: weekly             # owner audits a sample of published assets
inputs:
  - { name: discovery_log, source: opportunity-engine/discovery-log }   # verbatim frustration language
  - { name: real_numbers,  source: stripe + posthog (scorecard) }
outputs:
  - { name: audit_log, artifact: artifacts/{product}/authority-audit-{date}.json }
enforced_by: _shared/content-eval-rubric.yaml   # this standard IS the rubric's intent
depends_on: [_shared/metrics.yaml, _shared/content-eval-rubric.yaml]
consumed_by: [twitter-growth-sop, linkedin-growth-sop, launch-sop, distribution-sop, product-promotion-sop, go-to-market-sop, content-repurposing-sop]
done_when:
  - any audited asset that violates a rule below is sent back with required_edits
---

# Growth Engine — Founder Authority (Positioning Standard)

This is the single source of truth for positioning and credibility across every
public channel. Other skills inherit these rules and must not restate them. The
rules are mechanically enforced by `_shared/content-eval-rubric.yaml`.

## Rule 1 — Real Numbers Only
- No vague claims ("massive growth", "huge volume", "thousands of users"). Use a
  precise number sourced from the scorecard / Stripe / PostHog.
  - Bad: "Our video tool is growing fast!"
  - Good: "We went 12 WAU → 87 WAU in 14 days by changing one CTA line."
- Numbers may never be fabricated. If no real number supports the claim, change the
  claim. (Rubric dimension: `claim_backed`.)
- Financial proof: prefer a Stripe screenshot of net revenue / growth curve over prose.

## Rule 2 — Different, not Better
- Do not argue you are "better" than a giant by listing minor features. Position as
  fundamentally different for a specific sub-audience. (Rubric dimension: `positioning_different`.)
  - Them: "All-in-one content platform, 200 settings."
  - Us: "Text-to-video wrapper for creators who need 1 Reel in under 60s, 1 click."

## Rule 3 — Speak the Frustrated User's Language
- Use the exact phrases from the discovery log. Reflecting the user's own words back
  builds instant authority because they feel understood. (Rubric dimension: `voice_authenticity`.)

## Rule 4 — Honest Scarcity
- Offers use finite, real windows only. Founder pricing locks for
  `ref:_shared/metrics.yaml#commitments.founder_pricing_lock_months` — never "forever".
  (Rubric dimension: `no_banned_phrases`.)

## Quality gate
Every draft is scored by the rubric before the human approval gate. Assets below the
rubric threshold are blocked, never published. The weekly audit re-checks a sample of
already-published assets and logs violations to `audit_log`.
