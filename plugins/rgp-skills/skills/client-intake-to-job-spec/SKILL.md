---
name: client-intake-to-job-spec
description: Convert client kickoff call notes into a structured, sourcing-ready job spec. Flags every section where the notes are silent or ambiguous instead of inventing requirements. Use this skill whenever the user mentions a kickoff call, a discovery call, intake notes, or turning a conversation with a client into a written job spec — even if they don't explicitly say "spec" or "intake."
---

# Client Intake → Job Spec

Turn raw kickoff-call notes into a structured job spec the recruiting team can start sourcing against. The skill's most important job is not writing the spec — it's catching the gaps, so the account manager knows exactly what questions to send back to the client before sourcing starts.

## When to use this

The user just got off a kickoff call with a client and has notes. They need a job spec that's either ready to hand to the recruiting team, or flagged clearly where confirmation is needed. Sourcing against a half-complete spec burns the team's time; catching gaps here saves a week.

## Inputs

One input:

- **`notes`** — raw notes from the client kickoff call. Can be messy or incomplete; that's expected. The skill flags gaps rather than inventing.

## Process

1. Fill every section of the output format.
2. For any section where the notes are silent or ambiguous, write `⚠️ NEED TO CONFIRM: [specific question for the client]` instead of guessing. The ⚠️ is how the account manager knows what's still open.
3. Don't pad. If the must-haves are 3 items, list 3 — not 5. Inventing must-haves produces candidates the client doesn't want.
4. End with a numbered list of ALL ⚠️ questions collected in one place, ready to copy into an email back to the client.

## Calibration

**Strong must-have (falsifiable):**
> "2+ years outbound SDR experience in B2B SaaS with $50k+ ACV"

**Weak must-have (rewrite or flag):**
> "Strong communication skills"
> → Either make it falsifiable ("Proven async written communication — require a writing sample in the JPT"), or flag it: `⚠️ NEED TO CONFIRM: What does "strong communication skills" mean for this role — a writing-heavy role, a live-call-heavy role, both?`

The rule: a must-have should let you reject a candidate. If it doesn't, it's decoration.

## Guardrails

- **Don't invent requirements.** Every must-have traces to a line in the notes.
- **Compensation range comes from the notes or gets flagged.** Never make one up.
- **Start date and timezone**: if not stated, flag with ⚠️. These are the two most common gaps and the two most common sources of wasted sourcing cycles.
- **Zero support = ⚠️.** If a section has no support in the notes, don't guess; flag it and explain what's missing.

## Output format

ALWAYS use this exact template:

```markdown
## Role title and level
[e.g., Senior SDR, II]

## Must-have skills (3–5)
- ...

## Nice-to-have skills (3–5)
- ...

## Day-to-day responsibilities
- [5–7 bullets]

## Tools and stack
- ...

## Hours / timezone overlap required
- ...

## Ideal candidate profile
[2 sentences]

## Disqualifiers
- ...

## Compensation range
[from notes, or "⚠️ NEED TO CONFIRM"]

## Start timeline
[from notes, or "⚠️ NEED TO CONFIRM"]

## Questions to send back to the client
1. ...
2. ... (only if there are ⚠️ items above; otherwise "None — spec is ready for sourcing.")
```

## Examples

**Example — useful flag:**

> Compensation range: `⚠️ NEED TO CONFIRM: Client mentioned "competitive" without a range. Do they have a band approved, or do they want us to benchmark?`

The account manager can copy that directly into an email.

**Example — unhelpful flag:**

> Compensation range: `Not specified in notes`

True but not actionable. The ⚠️ version tells the AM what to ask for.

## Failure modes

- **Claude invents a must-have** → stop and re-read; if the must-have doesn't trace to the notes, flag it instead.
- **All sections filled without any ⚠️** → re-read the notes with fresh eyes; kickoff notes almost always have gaps. Zero flags is suspicious.
- **⚠️ questions at the bottom don't match the flags in the body** → regenerate the bottom list from the body.
