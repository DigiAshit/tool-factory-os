# Product Engine - MVP Scoping Framework

## 1. Trigger
This framework is executed by the **Product Manager** and **Co-Founder Builder** during the initial scoping phase of an approved project.

## 2. Core Rules for MVP Scoping

### Rule 2.1: The Single Workflow Boundary
- **One Product, One Core Action**: The MVP must solve exactly one core workflow frustration. If the product is a video tool, it does one thing (e.g., converts text to video). It does not have video editing, multi-track timelines, stock asset libraries, or voiceover settings.
- **Strip Feature Creep**: Remove onboarding tutorials, custom dashboard layouts, account profile configurations, integration integrations, or alternative payment methods. The only pages allowed are:
  - Landing Page (with pitch and pricing)
  - Checkout Gate (Stripe payment)
  - Core Dashboard (executing the single workflow)
  - Basic Settings (cancel subscription button)

### Rule 2.2: The 30-Day Build Limit
- **Strict Time Gate**: The product builder must deploy the minimal working skeleton to production within **30 days** of contract signing.
- **Fail-Fast Trigger**: If the builder cannot launch the skeleton in 30 days, the project is paused. The CEO must run a Keep/Kill audit. If the delay is due to architecture over-complexity, strip the architecture down or kill the project immediately.

## 3. Quality Check
- Confirm that the MVP spec document details only one core user action.
- Verify that the development roadmap contains a release date set exactly 30 days or less from the start date.
