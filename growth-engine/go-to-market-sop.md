---
id: growth-engine/go-to-market-sop
version: 2
owner_role: Growth Strategist
trigger:
  type: event
  on: passed(_shared/metrics.yaml#gates.month2_skeleton_gate)   # enters public scaling phase
inputs:
  - { name: positioning,   source: growth-engine/founder-authority-sop }   # the "different" line
  - { name: proof_assets,  source: growth-engine/validation-sop }          # testimonials below pricing
  - { name: cro_metrics,   source: posthog }
tools_allowed: [posthog_read, posthog_experiments, stripe_read, web_publish]
outputs:
  - { name: landing_spec,    artifact: artifacts/{product}/gtm/landing-spec.md }
  - { name: experiment_plan, artifact: artifacts/{product}/gtm/experiments.json }
  - { name: cro_report,      artifact: artifacts/{product}/gtm/cro-report-{date}.json }
guardrails:
  hitl_gate: true                 # approve landing changes + checkout flow before publish
  checkout_account_ownership: must_resolve   # see section 2.3
depends_on: [_shared/metrics.yaml, growth-engine/founder-authority-sop, growth-engine/validation-sop]
done_when:
  - landing page implements sections 2.1-2.4
  - every A/B test conforms to _shared/metrics.yaml#experiment_standard (NOT a fixed visit count)
  - winners declared only at the planned horizon with significance met
---

# Growth Engine — Go-To-Market (Landing & CRO)

Runs when a product clears the Month-2 skeleton gate. Maximize visitor→trial without
breaking trial→paid.

## 2.1 Hero
State the "different" positioning verbatim from `founder-authority-sop`.
- "The text-to-video wrapper for creators who need 1 Reel in under 60s, 1 click."

## 2.2 Primary CTA
Place the primary CTA early and repeat it down the page (the old "above the fold" framing
is necessary-not-sufficient on long mobile pages). Microcopy under it sets expectations,
e.g. "Cancel anytime in 1 click."

## 2.3 Checkout — decide the trial tradeoff explicitly
Credit-card-required trials raise trial→paid but **cut trial starts**. Treat it as a test
(section 3), not a default. Whichever you choose, resolve account ownership: collect email →
provision the account → then Stripe Checkout, OR use Stripe Checkout with account
provisioning on the success webhook. Never route to a pre-filled checkout that leaves
"who owns this account?" undefined.

## 2.4 Social proof
Embed 3–5 approved testimonials from `validation-sop` directly below pricing.

## 3. A/B testing routine
Run experiments in PostHog conforming to `_shared/metrics.yaml#experiment_standard`:
- Measure **conversions, not visits**; size each arm from baseline CVR + target MDE +
  power before launching. (The old "declare a winner after 200 visits" rule is removed —
  200 visits is a handful of conversions and decides on noise.)
- Test one lever at a time: hero hook, pricing display (annual vs monthly), CTA copy,
  CC-required vs not.
- No peeking; declare a winner only at the planned horizon with significance met.

## Exit
Complete on all `done_when` conditions.
