# Opportunity Engine - Build vs Reject Framework

## 1. Trigger
This framework is run by the **CEO** and **Portfolio Manager** once an opportunity scoring sheet achieves a score of 40 or higher.

## 2. Decision Tree Gate Checks
To approve a project for development, all of the following checks must be answered with a **YES**. If any check is a **NO**, the project must be rejected.

```mermaid
graph TD
    Start[Scored Opportunity >= 40] --> Q1{Is there 1 active MVP limit free?}
    Q1 -- No --> Reject[REJECT: Freeze and hold in queue]
    Q1 -- Yes --> Q2{Is co-founder signed on equity-only?}
    Q2 -- No --> Reject
    Q2 -- Yes --> Q3{Is validation target met (10+ leads)?}
    Q3 -- No --> Reject
    Q3 -- Yes --> Q4{Can it be built as a single workflow in 30 days?}
    Q4 -- No --> Reject
    Q4 -- Yes --> Approve[APPROVE: Initialize MVP Spec]
```

### Checklist Detail:
1. **Active project limit check**: Are we running no more than **one active MVP build** at this time? (We must never build multiple projects concurrently; focus resources on one project until it passes validation or is killed).
2. **Co-founder contract check**: Do we have a signed TMaker Co-Founder Agreement with a developer partner (stipulating equity split, monthly profit distributions, zero salaries, and IP assignment to the holding company)?
3. **Validation verification check**: Are the 10+ unprompted leads verified and logged?
4. **Scope check**: Can the core workflow be deployed as a minimal skeleton within 30 days by a single developer?

## 3. Outputs
- **Approved**: Document decision in the Weekly CEO Review logs, initialize the MVP spec, and assign the project to the selected co-founder.
- **Rejected/Held**: Hold the project in the backlog until resources free up or renegotiate contract parameters.
