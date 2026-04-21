# RGP Skills (SKILL.md format)

This folder holds RGP's AI skills in the **SKILL.md format** used by Anthropic's [Skill Creator plugin](https://claude.com/plugins/skill-creator) and Claude Code skills generally. Each skill is a folder with a `SKILL.md` at the root — YAML frontmatter (`name`, `description`) plus a markdown body.

These are the **source of truth** for the 13 starter skills. The same content lives in Supabase rows (`public.ai_skills.prompt_body` + `description`) so the RGP OS web UI at `/ai/skills` can render them; a migration keeps the two in sync. If you edit a SKILL.md here, update the corresponding `UPDATE` in the sync migration so the next deploy writes the change to the DB.

## Layout

```
skills/
├── README.md                                 ← you are here
├── score-video-screen/SKILL.md               ← Vetting
├── grade-job-preview-test/SKILL.md
├── interview-notes-summary/SKILL.md
├── candidate-comparison-matrix/SKILL.md
├── candidate-rejection-email/SKILL.md
├── weekly-client-status-drafter/SKILL.md     ← Client Ops
├── client-intake-to-job-spec/SKILL.md
├── shortlist-deck-builder/SKILL.md
├── role-spec-quality-check/SKILL.md
├── outbound-message-personalizer/SKILL.md    ← Sourcing
├── linkedin-profile-fit-assessment/SKILL.md
├── sop-authoring-assistant/SKILL.md          ← Internal
└── meeting-notes-to-actions/SKILL.md
```

Workflow grouping in RGP OS (vetting / client-ops / sourcing / internal) lives in the DB column `ai_skills.workflow`; it isn't reflected in the folder layout because Claude Code skills are workflow-agnostic.

## Conventions (from the Skill Creator plugin)

Each SKILL.md follows these conventions, drawn directly from the plugin's own [SKILL.md](https://github.com/anthropics/skills) writing guide:

1. **Minimal YAML frontmatter** — only `name` and `description`. The description is the primary triggering mechanism, so it's written to be *pushy* (includes "Use this skill whenever the user mentions…") and covers when-to-use context, not just what the skill does.
2. **Imperative voice** throughout the body. "Open the spec", not "You should open the spec".
3. **"ALWAYS use this exact template"** pattern for output formats. The template is a code block showing the exact structure.
4. **Explain the why**, not just the what. Each section has a sentence or two on why the rule exists — the model follows it better when it understands the reasoning.
5. **Progressive disclosure.** Keep the SKILL.md body focused. Large references (rubrics, long docs, calibration examples) can move to `references/` subfolders in a future revision if a skill outgrows 500 lines.
6. **Calibration for judgment skills.** Any skill that scores, ranks, or recommends includes a calibration block anchoring the scale.
7. **Guardrails explained.** Every guardrail has a short reason — "Never invent quotes" is followed by *why it matters* (invented evidence damages team trust).
8. **Failure modes section.** The end of each skill names 2–3 common failure patterns with concrete recoveries.

## Using these with the Skill Creator plugin

If you have the Skill Creator plugin installed in Claude Code (`claude plugin install skill-creator@claude-plugins-official`), you can:

- **Run evals** on any of these skills against real RGP tasks:
  ```
  /skill-creator executor
  ```
- **Grade outputs** against expectations:
  ```
  /skill-creator grader
  ```
- **Benchmark** a skill across many runs to measure variance:
  ```
  /skill-creator benchmark ./skills/score-video-screen --runs 5
  ```
- **Improve** a skill based on feedback:
  ```
  /skill-creator analyzer ./skills/score-video-screen
  ```

See the plugin's own [SKILL.md](https://github.com/anthropics/skills/blob/main/skill-creator/SKILL.md) for full workflow docs.

## Syncing to RGP OS

The DB row for each skill (in `public.ai_skills`) mirrors the SKILL.md content:

- `name` column → SKILL.md frontmatter `name`
- `description` column → SKILL.md frontmatter `description`
- `prompt_body` column → everything AFTER the frontmatter (the markdown body)

The sync migration `supabase/migrations/20260421120000_a8000000-aaaa-4aaa-aaaa-000000000001.sql` writes the current bodies into the DB. When you edit a SKILL.md here, update the migration (or write a new one) so a deploy picks it up.

## Why keep both a folder AND DB rows?

- **The folder** is the authoring surface. It's Git-versioned, reviewable in PRs, installable in Claude Code via the plugin.
- **The DB rows** power the RGP OS UI — the `/ai/skills` library, the "Run in Claude" button, the feedback and XP loops.

Both point at the same content; the folder wins on authoring ergonomics, the DB wins on in-app UX.
