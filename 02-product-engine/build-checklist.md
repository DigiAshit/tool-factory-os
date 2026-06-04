# Build Checklist - Product Engine

This checklist enforces the strict constraints of the Month 1-2 Skeleton build phase.

## 1. Scope Constraints (Nail One Thing)
- [ ] **Single workflow**: The app has exactly one flow. E.g. Enter keyword -> Get content ideas.
- [ ] **No user accounts**: Use simple token-based access, local storage, or temporary sessions. Do not waste time building OAuth or custom signup pages.
- [ ] **No settings page**: No custom themes, profile avatars, or configuration adjustments. Use hardcoded defaults.
- [ ] **Ugly but functional**: Focus on speed and functionality. The UI can be basic HTML/CSS or standard component libraries. Do not design custom visuals.

## 2. Technical Safeguards (Modularity)
- [ ] **Model Agnostic**: Ensure the AI backend is built with wrappers. We should be able to switch between GPT-4o, Claude 3.5, and Gemini 1.5 in under 5 minutes.
- [ ] **Non-AI core verified**: The non-AI moat (database, editor interface, output export mechanism) is fully operational without third-party LLM calls.

## 3. The 30-Day Limit
- [ ] **Launch Clock**: The product must be deployed and handed to early testers within 30 days of project approval.
- [ ] **No feature creep**: Any feature suggested during the build that is not part of the initial core spec is written to the opportunity backlog.

## 4. Skeleton Validation Gate
- [ ] **Hand off**: Deploy the build and hand it to 5-10 warm leads (from the opportunity discovery list) for free.
- [ ] **Dwell / Usage check**: Monitor if the testers run the tool.
- [ ] **The "Use Twice" Rule**: Do NOT write any new code or add features until at least 5 testers use the core feature at least twice. If they don't, return to the drawing board and revise the core value proposition.
