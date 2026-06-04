# Growth Engine - Go-to-Market (GTM) SOP

## 1. Trigger
Executed by the **Growth Strategist** when a product passes the Month 2 Skeleton Gate and enters the public scaling phase.

## 2. Page Conversion & Landing Page Optimization (CRO)
To maximize visitor-to-trial conversion, enforce these structural rules on the product landing page:
1. **The Hero Header**: Clearly state the "different" positioning.
   - *Example: "The text-to-video wrapper for creators who need to generate 1 Reel in under 60 seconds with 1 click."*
2. **Value-First CTA**: Place a primary call to action (e.g., *"Try it Free for 7 Days"*) immediately above the fold. Include a microcopy subtext: *"Credit card required. Cancel anytime in 1 click."*
3. **No-Friction Checkout**: Route the CTA button directly to a pre-filled Stripe checkout session. Avoid multi-step signups before payment collection.
4. **Embedded Social Proof**: Display 3-5 screenshots of happy user tweets or video reviews directly below the CTA.

## 3. A/B Testing Routine
- Run concurrent A/B experiments using tools like PostHog.
- Focus tests strictly on:
  - Landing page headlines (Hook)
  - Pricing display (e.g., highlighting annual discount vs monthly cost)
  - CTA copy (e.g., *"Start 7-Day Trial"* vs *"Generate My First Video"*)
- Declare a winner after a minimum of 200 visits per variant.
