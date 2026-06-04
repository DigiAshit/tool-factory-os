# Opportunity Engine - Scoring Framework

## 1. Trigger
Run this framework after an opportunity passes the Week 1 Validation Check (10+ unprompted leads).

## 2. Scoring Parameters (Max 60 Points)
Evaluate the opportunity against the following six criteria, scoring each from 0 to 10:

| Parameter | Description | Scoring Guide |
|---|---|---|
| **Audience Alignment** | Does this product target creators, digital entrepreneurs, or prosumers already in our distribution range? | 10 = Exact match<br>5 = Partial match<br>0 = Different audience |
| **Workflow Frustration** | Is the pain severe, frequent, and tied directly to workflow bottlenecks? | 10 = Severe daily bottleneck<br>5 = Monthly minor annoyance<br>0 = Purely nice-to-have |
| **Feasibility (30 Days)** | Can a single developer build a working skeleton of the core workflow in under 30 days? | 10 = Under 14 days<br>5 = 15-30 days<br>0 = Requires >30 days or complex AI research |
| **Integration Potential** | Can the tool leverage existing standard APIs (Stripe, Rewardful, OpenAI, PostHog, X)? | 10 = Zero custom integrations<br>5 = Minor custom hooks<br>0 = Requires custom enterprise integrations |
| **Distribution Ease** | Can we piggyback on existing discussions or tap into competitor launch engagers? | 10 = High discussion volume and easy lead mining<br>5 = Moderate discussion volume<br>0 = Hard-to-reach niche |
| **B2B Willingness-to-Pay** | Does the solution save time or generate money for users (making it easy to charge $40-$100/mo)? | 10 = Saves $500+/mo or 10+ hours/week<br>5 = Saves 2-3 hours/week<br>0 = Non-business utility |

## 3. Decision Gate (The 40-Point Threshold)
- **Score >= 40**: Opportunity passes. Proceed to the Build vs Reject Framework.
- **Score < 40**: Opportunity rejected. Return it to the backlog or kill it. Do not spend engineering resources on it.

## 4. Verification Check
- Ensure that the opportunity's score sheet is signed off by the **Portfolio Manager** and logged in the monthly scorecard.
