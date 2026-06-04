---
id: growth-engine/validation-sop
version: 2
title: Social Validation (Testimonials)
not_to_be_confused_with: _shared/metrics.yaml#gates.validation_gate   # that is IDEA validation (10+ leads/7d)
owner_role: [Customer Researcher, Growth Strategist]
trigger:
  type: event
  on: [user_completed_first_week, positive_social_mention_detected]
inputs:
  - { name: usage_events,    source: posthog }                 # core_workflow completions
  - { name: social_mentions, source: x + linkedin + reddit monitors }
tools_allowed: [posthog_read, email_send, x_api_dm, linkedin_api_dm, screenshot_grab]
outputs:
  - { name: testimonial_library, artifact: artifacts/{product}/proof/testimonials.jsonl }
  - { name: social_proof_assets, artifact: artifacts/{product}/proof/screenshots/ }
  - { name: proof_dashboard,     artifact: artifacts/{product}/proof/dashboard.json }
guardrails:
  consent_required: true          # explicit permission before publishing any quote/screenshot/handle
  pii: store consent_basis with every captured testimonial
  hitl_gate: true                 # approve outreach + what gets embedded on the site
depends_on: [_shared/metrics.yaml, growth-engine/founder-authority-sop]
handoff: { to: Product Manager, what: approved proof assets to embed below pricing }
done_when:
  - per product: >=3 video reviews AND >=10 text reviews captured (with consent) before Scale phase
  - approved assets handed to Product Manager for the landing page
---

# Growth Engine — Social Validation (Testimonials)

Capture proof from happy users and turn it into landing-page social proof. NOTE: this
is testimonial capture — distinct from the idea-**validation gate** (10+ unprompted
leads in 7 days) defined in `_shared/metrics.yaml#gates.validation_gate`.

## Step 1 — Direct request sequence
1. From PostHog, identify users who completed the core workflow **5+ times in a week**.
   DM/email:
   - "Hey {Name}, you've been using {Product} a lot — we want to make it better. Open
     to a 60-second screen capture of your first experience? We'll credit your account
     with {reward}."
2. If they decline video, request a 2-sentence text quote:
   - "What was the single biggest time-saver you noticed with {Product}?"
3. **Consent is mandatory** before anything is published — store `consent_basis`.

## Step 2 — Compile social proof
1. Monitor X / LinkedIn / Reddit for unprompted mentions; screenshot them (with
   permission to reuse the handle/quote).
2. Hand approved assets to the Product Manager to embed directly **below pricing**.
3. Maintain `proof_dashboard`: count of verified video + text reviews per product.

## Targets / gate
Minimum **3 video + 10 text** verified reviews per product before it enters the Scale
phase.

## Exit
Complete on all `done_when` conditions.
