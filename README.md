# Tool Factory Operating System (TFOS)

This repository contains the operational guidelines, templates, and Claude skills for running a repeatable portfolio-based business that discovers, validates, builds, and grows software assets.

## Repository Layout
- **`01-opportunity-engine/`**: Social listening, competitor analysis, and opportunity scoring framework.
- **`02-product-engine/`**: Strict Month 1-2 Skeleton build checklists and specifications.
- **`03-growth-engine/`**: Warm outreach playbooks, feedback collection, and AI-Human SEO loops.
- **`04-portfolio-engine/`**: Monthly status templates and asset kill/sunset criteria.
- **`05-skills/`**: The specialized Claude skill folders (`SKILL.md`) that can be loaded into Claude.ai, Claude Code, or Antigravity to run workflows.
- **`templates/`**: Operational scorecard and review logs.

## Loading Skills into Antigravity
To load these skills into your Antigravity or Claude agent:
1. Open settings or configure your provider's skill path to point to `tool-factory-os/05-skills/[skill-folder]`.
2. Ensure the skill is enabled. The YAML frontmatter in each `SKILL.md` defines the trigger conditions for loading.
