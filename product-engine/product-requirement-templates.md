# Product Engine - Product Requirement Document (PRD) Template

This template is utilized by the **Product Manager** to spec out approved MVPs. All PRDs must strictly conform to this structure.

---

# PRD: [Product Name] - Single-Workflow MVP

## 1. Objective & User Persona
- **Audience**: Prosumers, creators, and digital entrepreneurs.
- **Workflow Frustration**: [Describe the exact bottleneck in the user's language, sourced from discovery logs].
- **Core Value Proposition**: [Single sentence explaining how the tool resolves this bottleneck in under 5 minutes].

## 2. Core Workflow Specification
Describe the user steps to perform the single core action:
1. **Input**: [Describe what the user enters, e.g., text, URL, file upload].
2. **Process**: [Describe the backend transformation, e.g., calling OpenAI API, running a script].
3. **Output**: [Describe the result displayed or downloaded by the user, e.g., generated video, clean JSON list].

## 3. Technology Architecture Constraints

### Constraint 3.1: Modular AI Wrapper Design
- **Separation of Concerns**: All LLM and AI models must be treated as hot-swappable plugins. Do not hardcode specific model logic into the core application state or database layer.
- **API Wrapper**: Build a unified AI abstraction layer. Changing the underlying provider (e.g., from OpenAI to Anthropic, or to a local model) must require changing a single configuration key in `.env`.

### Constraint 3.2: Non-AI Moat Requirement
- **Avoid Pure Wrappers**: To prevent competitors from undercutting us, the application must have a non-AI core moat (e.g., custom database schemas, unique workflow rules, integrations with obscure APIs, or specific output formats that are hard to replicate).
- **Core Moat Spec**: [Detail what the non-AI value is. For example, Outrank.so doesn't just call AI; it indexes custom GSC keyword matrices and automates specific posting schedules].

## 4. Launch Metrics
- **Validation Target**: 10+ unprompted leads (Met).
- **B2B Pricing Band**: $40 - $100 per month.
- **Gated Trial**: Credit card required before accessing the free trial.
