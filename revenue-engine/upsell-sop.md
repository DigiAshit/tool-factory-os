# Revenue Engine - Upsell SOP

## 1. Trigger
Executed by the **Revenue Strategist** and **Product Manager** during feature configuration and Stripe integration.

## 2. Upgrade Trigger Design

### Rule 2.1: Usage-Based Gating
- Identify the core value metric of the product (e.g., number of generated videos, number of database exports, page crawls).
- Set a hard usage limit on the lower tier. When the user approaches **80% of their limit**, display an in-dashboard notification recommending an upgrade.
- When they hit **100%**, block further actions with a modal routing them to the Stripe checkout for the next pricing tier.

### Rule 2.2: Value-Tier Upgrades
- Structure the Good-Better-Best plans so that advanced tiers unlock high-value workflows (e.g., automated API access, priority processing, team collaboration settings).
- Do not hide core functionality behind upsells; only hide features that save additional time for high-usage power users.
- Run monthly audits to ensure that at least 15% of active users upgrade from the base plan to higher tiers.
