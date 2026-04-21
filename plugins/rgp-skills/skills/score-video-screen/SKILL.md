---
name: score-video-screen
description: Score a candidate's video screen transcript against RGP's 5-criterion rubric and recommend Advance/Hold/Pass. Use this skill whenever the user mentions scoring a video screen, evaluating a Stage-1 candidate call, grading a screening transcript, or wants a structured decision on whether to advance a candidate after a first-round video — even if they don't explicitly ask for a "rubric" or "score."
---

# Score Video Screen

Grade an offshore candidate's video screen for a US-based sales, marketing, or operations role at RGP. Produce a rubric table with evidence quotes, a red-flag list, and a binary-ish decision (Advance / Hold / Pass) — in a format the team can drop straight into a shortlist doc.

## When to use this

The user has a video screen transcript (or rough notes from one) and needs a consistent, evidence-grounded scoring before deciding whether to move the candidate to the Job Preview Test stage. This is RGP's Stage 1 of the 4-stage funnel — high volume, fast triage, needs to be repeatable.

## Inputs

The user pastes a single input:

- **`transcript`** — the full text of the candidate's video screen. Complete transcript, not a summary. If the user pastes a summary, stop and ask for the full transcript — the skill's judgments rely on specific quotes.

## Process

Work through the rubric in order. Don't jump to a recommendation before grounding every score in the transcript.

1. Read the transcript end-to-end before scoring anything.
2. Inside `<thinking>` tags, note specific quotes or moments that bear on each rubric criterion. The thinking step matters because it forces evidence-first scoring — without it, scores drift toward gut reactions.
3. Score each rubric criterion 1–5. Cite the quote or observation behind every score.
4. List red flags. If none, say so explicitly — don't invent problems to look thorough.
5. Recommend Advance / Hold / Pass. Default to Hold when evidence is mixed; do not force a decision.

## The rubric

Score each criterion 1–5:

1. **English fluency and clarity** — can the candidate be understood on a US client call?
2. **Communication and active listening** — do they answer the question asked, or talk past it?
3. **Relevant experience** — how close is their background to the role?
4. **Energy and engagement** — do they sound present, interested, curious?
5. **Fit for remote-async work** — do they ask good clarifying questions, work without hand-holding?

## Calibration

Anchor the scale before scoring. Consistency across candidates matters more than precision within a candidate.

**English fluency**:
- 5/5: complete sentences, precise vocabulary, handles clarifying follow-ups without losing the thread.
- 3/5: understandable but accent or vocabulary occasionally requires re-parsing.
- 1/5: multiple points where meaning is unclear even from context.

**Relevant experience**:
- 5/5: directly did the role at a comparable company in the last 2 years.
- 3/5: adjacent role or adjacent industry — transferable but requires ramp.
- 1/5: no clear line from past experience to this role.

## Guardrails

These exist because the skill gets used in high volume — guardrails prevent common failure modes that compound across many candidates.

- **Never invent quotes or observations.** If you can't cite a specific transcript moment, lower the score rather than guess. Invented evidence damages team trust faster than any other failure.
- **Short-transcript signal**: if the transcript is under 200 words, note at the top that the sample is small and score with lower confidence.
- **No demographic proxies**: fit judgments must be based on observed behavior, not country, accent, or background. This is non-negotiable.
- **Default to Hold on mixed evidence.** Forcing Advance or Pass when signals conflict is how mishires happen.

## Output format

ALWAYS use this exact template:

```markdown
## Rubric Scores
| Criterion | Score | Evidence |
| --- | --- | --- |
| English fluency | X/5 | "direct quote from transcript" |
| Communication | X/5 | "direct quote from transcript" |
| Relevant experience | X/5 | "direct quote from transcript" |
| Energy/engagement | X/5 | "direct quote from transcript" |
| Remote-async fit | X/5 | "direct quote from transcript" |

## Red Flags
- [specific concern with quote], or "None observed"

## Recommendation
**[Advance / Hold / Pass]** — [one-sentence rationale tied to the scores]
```

## Examples

**Example — good evidence citation:**

> Input: "…I worked at Stripe for 3 years as an SDR, starting on inbound and moving to outbound within 6 months…"
>
> Output row: `| Relevant experience | 5/5 | "3 years as an SDR at Stripe, inbound → outbound within 6 months" |`

**Example — weak evidence citation (don't do this):**

> Output row: `| Relevant experience | 5/5 | "Candidate has strong sales background" |`

The first cites a specific claim in the transcript. The second is a judgment without evidence — it gives the reader nothing to audit.

## Failure modes

- **Scores wildly differ between runs of the same transcript** → rubric is being interpreted inconsistently; re-read the calibration section before scoring.
- **Output invents a quote** → the transcript was too short or ambiguous; either ask for a fuller transcript or lower the confidence and flag at the top.
- **Recommendation forces Advance despite mixed scores** → default to Hold; write a one-sentence rationale that names the specific tension.
