---
name: role-spec-quality-check
description: Review a job spec for ambiguity, missing fields, conflicting requirements, and unrealistic asks before sourcing starts. Returns client-ready questions to send back. Use this skill whenever the user mentions reviewing a spec, checking if a job spec is ready for sourcing, catching problems before kicking off a search, or wants a second pair of eyes on a draft spec — even if they don't explicitly say "quality check" or "review."
---

# Role Spec Quality Check

Diagnose a job spec across 4 categories of problems and produce specific, client-ready questions the account manager can copy into an email. Designed to be the final gate before sourcing begins — catching one ambiguity here saves the team a week of wasted outreach.

## When to use this

The user has a drafted job spec — either from the `client-intake-to-job-spec` skill or from the client directly — and wants to validate it before the recruiting team starts sourcing. This is a diagnostic skill: it doesn't rewrite the spec, it surfaces what needs clarification.

## Inputs

One input:

- **`spec`** — the complete draft job spec. Paste the full document; the skill reads end-to-end.

## Process

1. Inside `<thinking>` tags, read the spec end-to-end before categorizing. Do not go section-by-section — many problems only show up when two sections contradict each other.
2. Organize findings into 4 diagnosis sections (see Output format):
   - **Ambiguities** — requirements that could be read two ways.
   - **Missing fields** — anything essential the spec doesn't answer (timezone, tools, disqualifiers, compensation, start date, level).
   - **Conflicting requirements** — asks that are hard to satisfy simultaneously.
   - **Unrealistic asks** — red flags that will waste the team's time.
3. Produce a final numbered list of questions for the client. Each question targets a specific flagged issue.

## Calibration

**Strong question (specific, actionable):**
> "You listed 'must have SaaS sales experience' and 'open to first-time sellers with strong business acumen.' Which takes priority if we find candidates who meet one but not the other?"

**Weak question (rewrite):**
> "Can you clarify the experience requirements?"

The weak version gives the client nothing to respond to. The strong version names the conflict and forces a specific choice.

**Example of an unrealistic ask to flag:**
> "5 years experience at a role that has only existed for 2 years."
> Flag it. Don't just pass it through.

**Example of a realistic-sounding ask that's actually conflicting:**
> "Must work US hours" + "Must be based in Manila."
> 12-hour overlap isn't physically possible without night shift. Flag as a conflict and ask which takes priority.

## Guardrails

- **Don't invent issues.** If a section has nothing to report, say "None." A clean spec is a real outcome — falsifying issues to look thorough erodes the signal.
- **Don't rewrite the spec.** This skill diagnoses; it doesn't author. Rewriting is a separate task.
- **Every question at the bottom must trace back to a flagged issue above.** No questions without a diagnosis upstream.
- **"Experience" is usually ambiguous.** "5 years of SaaS experience" could mean 5 years in SaaS companies, 5 years in a SaaS sales role, 5 years closing SaaS deals — the three are very different pipelines.

## Output format

ALWAYS use this exact template:

```markdown
## Ambiguities
- [ambiguity with the specific language], or "None"

## Missing fields
- [what's missing], or "None"

## Conflicting requirements
- [requirement A] vs [requirement B] — [why this conflict matters], or "None"

## Unrealistic asks
- [ask] — [why it's unrealistic], or "None"

## Questions to send back to the client
1. [specific question tied to a flagged issue]
2. ... (only if there are ⚠️ items above; otherwise "None — spec is ready for sourcing.")
```

## Failure modes

- **Claude reports "all clear" on a spec with obvious issues** → re-read with fresh eyes; most specs have at least a timezone or start-date gap.
- **Questions at the bottom are generic** → each should name the specific phrase or field from the spec it's asking about.
- **Flagged issues don't show up in the final question list** → regenerate the question list by walking through each diagnosis section.
