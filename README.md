# rgp-skills

The **Remote Growth Partners** skill library for Claude Code and Cowork — 13 starter skills in [Anthropic Skill Creator](https://claude.com/plugins/skill-creator) format covering recruiting vetting, client ops, sourcing, and internal ops.

## What's here

```
.claude-plugin/
  plugin.json        ← plugin manifest (points at skills/)
  marketplace.json   ← in-repo marketplace for direct-from-GitHub install
skills/
  README.md                           conventions + Skill Creator usage
  score-video-screen/SKILL.md         Vetting
  grade-job-preview-test/SKILL.md
  interview-notes-summary/SKILL.md
  candidate-comparison-matrix/SKILL.md
  candidate-rejection-email/SKILL.md
  weekly-client-status-drafter/SKILL.md   Client Ops
  client-intake-to-job-spec/SKILL.md
  shortlist-deck-builder/SKILL.md
  role-spec-quality-check/SKILL.md
  outbound-message-personalizer/SKILL.md  Sourcing
  linkedin-profile-fit-assessment/SKILL.md
  sop-authoring-assistant/SKILL.md        Internal
  meeting-notes-to-actions/SKILL.md
```

## Install (RGP team)

Run these two commands **inside Claude Code or Cowork** (not a web UI):

```
/plugin marketplace add eldeebbomar/rgp-skills
/plugin install rgp-skills@rgp-team
```

All 13 skills register at once. Claude invokes the right one automatically when your ask matches the skill's description — no pasting prompts.

**Verify it worked**:

```
/skills list
```

You should see 13 `rgp-skills:<slug>` entries.

**Try one**:

> "score this video screen for me: [paste a candidate transcript]"

Claude should pick the `score-video-screen` skill and run it.

## Updating the skills

Source of truth lives in the private `eldeebbomar/hub-rgp` repo at `skills/<slug>/SKILL.md`. This public repo mirrors those files so the team can install via `/plugin`.

To pull the latest:

```bash
python scripts/sync_from_hub_rgp.py
git add skills/
git commit -m "sync: pull latest skills from hub-rgp"
git push origin main
```

Or trigger the **Sync from hub-rgp** GitHub Action manually (Actions tab → Run workflow). It runs on a daily schedule too, but the manual trigger is how you push an edit the moment it lands in hub-rgp.

Either path requires a `HUB_RGP_READ_TOKEN` secret set on this repo — a GitHub PAT with read access to the private `eldeebbomar/hub-rgp` repo.

## SKILL.md conventions

See [skills/README.md](./skills/README.md) for the authoring conventions (pushy descriptions, imperative voice, calibration blocks for judgment skills, failure-modes section).

## License

Internal RGP tooling. Public only so the team can `/plugin install` without GitHub auth.
