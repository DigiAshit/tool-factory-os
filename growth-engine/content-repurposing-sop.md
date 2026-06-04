---
id: growth-engine/content-repurposing-sop
version: 2
owner_role: Content Strategist
trigger:
  type: event
  on: media_asset_recorded        # podcast episode, product demo, or build-in-public update
  min_cadence: weekly
inputs:
  - { name: source_media, source: artifacts/{product}/media/raw/ }
  - { name: discovery_log, source: opportunity-engine/discovery-log }   # for caption hooks
tools_allowed: [video_cut, caption_render, posthog_read, link_shortener]
outputs:
  - { name: clips,         artifact: artifacts/{product}/clips/{date}/  (9:16 vertical, captioned) }
  - { name: post_drafts,   artifact: artifacts/{product}/clips/{date}/posts.md }  # per-platform copy
  - { name: schedule,      artifact: artifacts/{product}/clips/{date}/schedule.json }
guardrails:
  per_platform_export: true       # re-export clean per platform; no cross-platform watermarks
  linkedin_cta: first_comment     # ref:_shared/metrics.yaml#platform_guardrails.linkedin_links_in_post
  hitl_gate: true                 # approve clips + copy before scheduling
eval: { rubric: _shared/content-eval-rubric.yaml, applies_to: [post_drafts], block_publish_below: 0.80 }
depends_on: [_shared/metrics.yaml, _shared/content-eval-rubric.yaml, growth-engine/founder-authority-sop]
done_when:
  - >=2 high-quality vertical clips produced for the week
  - per-platform copy drafted, rubric-passed, human-approved
  - schedule.json written for cross-posting
---

# Growth Engine — Content Repurposing

Maximize the footprint of every recorded asset by cutting it into short vertical video.

## Step 1 — Extract micro-assets
1. Find high-impact hooks containing a key metric or a contrarian statement (often the
   first 30s of an explanation). Hooks must satisfy `founder-authority-sop` (real numbers).
2. Cut 30–60s vertical clips (9:16).
3. Add clean, large-typography captions. Avoid generic templated styling.

## Step 2 — Cross-post (re-export per platform)
Do **not** post one watermarked file everywhere — platforms de-prioritize content
carrying another platform's watermark or an obviously identical repost. Re-export a
clean master per platform and vary the first frame / caption.
- **TikTok:** description with 3–4 niche tags.
- **YouTube Shorts:** keyword-optimized title.
- **Instagram Reels:** short description; product CTA in bio link.
- **LinkedIn:** upload natively as video; CTA link in the **first comment**.
- **X:** native video tweet; 1-sentence hook + CTA.

## Step 3 — Gate & schedule
Score per-platform copy with the rubric; block < 0.80. After HITL approval, write
`schedule.json`. Target **2 high-quality clips/week**.

## Metrics
Track video views and CTR to product links per platform; feed into the weekly report.

## Exit
Complete on all `done_when` conditions.
