# Product Engine - Product Review Systems

## 1. Trigger
This review process is executed by the **Product Manager** and **Customer Researcher** at the end of the project's second month in production (Month 2).

## 2. The Month 2 Skeleton Validation Gate

### Heuristic: The "Use Twice" Rule
- **The Problem**: Founders often waste time building advanced dashboards, onboarding flows, and secondary features for products that users don't actually care about.
- **The Gate**: We freeze all new feature development until the core skeleton has proven engagement.
- **The Rule**: **At least 5 target testers must use the core workflow at least twice in Month 2.**
  - If a user signs up, clicks once, and leaves, they do not count.
  - They must perform the core action (e.g., generate a video, run a crawl, export a report) at least two separate times during the month.

### Decision Actions:
- **PASS**: If 5+ testers have used the core workflow at least twice in Month 2, the skeleton is validated. You are permitted to build secondary features (e.g., user profiles, history logs, integrations) and proceed to scaling the Growth Engine.
- **FAIL**: If fewer than 5 testers have used the core workflow twice, **freeze all feature additions immediately.**
  - Review the product analytics (PostHog replays) to see where users get stuck.
  - If the core workflow does not solve the user frustration, pivot the workflow or **kill the project** under the Sunset Protocol. Do not add features to solve a lack of core utility.

## 3. Quality Check
- Maintain a PostHog or database audit log showing the user IDs, timestamps, and core actions taken by the 5+ testers.
- Verify that the development branch has no feature pull requests merged during a FAIL state.
