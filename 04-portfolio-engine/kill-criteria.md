# Kill Criteria - Portfolio Engine

This document establishes the strict criteria and timelines for retiring ideas, skeletons, and active products.

## 1. Phase 1: Idea Kill Gate (Week 1)
- **Condition**: A raw concept is broadcasted to the target audience.
- **Trigger**: **Fewer than 10 unprompted reaches** (DMs, comments, emails) within 7 days of the broadcast.
- **Decision**: **Kill**. Do not create a repository, write specifications, or draft any code.

## 2. Phase 2: Skeleton Kill Gate (Month 2)
- **Condition**: The minimal skeleton is deployed and given to 5-10 testers.
- **Trigger**: **Fewer than 5 testers use the core feature at least twice** over a 14-day test period.
- **Decision**: **Kill or Pivot**. Do not add features or write custom UI. If pivoting, strip back to a different core feature; if killing, archive the codebase.

## 3. Phase 3: Scaling Kill Gate (Month 6+)
- **Condition**: An active product is charging customers.
- **Trigger**: The product satisfies any of the following:
  - Monthly churn exceeds **10%** for two consecutive months.
  - Stagnant or declining MRR for three consecutive months.
  - The single selected growth channel has CAC > LTV after 60 days of testing.
- **Decision**: **Kill**. Begin the Sunset Protocol: notify users, disable recurring subscriptions, and offer a simple static export of their data.
