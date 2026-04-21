---
name: interview-notes-summary
description: Transform raw interview notes into a structured summary with strengths, concerns, culture-fit signal, and a recommendation. Use this skill whenever the user mentions interview notes, wants to summarize an interview, needs to turn scribbled post-call thoughts into a team-ready summary, or is prepping to share interview takeaways in a shortlist doc — even if they don't explicitly say "summarize" or "summary."
---

# Interview Notes → Summary

Turn raw, messy interview notes into a decision-ready summary with strengths, concerns, culture-fit signal, and an Advance / Hold / Pass recommendation — in a format that drops straight into a shortlist doc.

## When to use this

The user just finished an interview and has rough notes. They need a structured writeup in minutes, not an hour. This skill replaces the muscle-memory "I'll write this up later" that never gets written up.

## Inputs

One input:

- **`notes`** — raw interview notes, as the user wrote them. Can be messy, bullet-form, prose, shorthand. The messier the better — this skill's value is in structuring chaos. If the notes are already structured (someone already summarized), the skill still works but it's less useful.

## Process

1. Inside `<thinking>` tags, extract the most load-bearing moments from the notes. Prioritize direct quotes and specific observations over paraphrases. The thinking step matters because it prevents you from filtering through a vague impression — you work from what the candidate actually said or did.
2. Write a 3-sentence summary covering background, relevant experience, and standout signal.
3. Top 3 strengths. Each must cite a direct quote or concrete observation from the notes.
4. Top 3 concerns. Same evidence standard.
5. Rate culture fit 1–5 with a one-sentence rationale grounded in observed behavior.
6. Recommend Advance / Hold / Pass with a one-sentence rationale.

## Calibration

The difference between a useful strength and a useless strength is evidence:

**Strong strength (use this style):**
> "Answered the async-work question with a concrete example — shipped a project across a 6-hour timezone offset using Loom videos and written standups by default."

**Weak strength (avoid):**
> "Seems like a good communicator."

The strong version lets the next reader audit your judgment. The weak version is pure vibes — the next reader has to take your word for it.

Same standard for concerns. "Concerned about communication" is noise. "Gave a rambling 4-minute answer to 'what's your biggest weakness' — didn't self-correct" is signal.

## Guardrails

- **Every observation traces to a line in the notes.** If you can't find it, drop it.
- **Short or incomplete notes**: if the notes are under 100 words or obviously partial, flag "Notes may be incomplete — proceed with lower confidence" at the top.
- **Default to Hold on mixed evidence.** Don't force Advance or Pass when the signal is unclear.
- **Culture fit ≠ demographics.** Culture fit is about observed behavior (curiosity, collaboration style, how they take feedback). Never about country, accent, age, gender.

## Output format

ALWAYS use this exact template:

```markdown
## Summary
[exactly 3 sentences covering background, relevant experience, standout signal]

## Strengths
- [direct quote or specific observation] — [what it tells us about this candidate]
- [direct quote or specific observation] — [what it tells us]
- [direct quote or specific observation] — [what it tells us]

## Concerns
- [direct quote or specific observation] — [what it tells us]
- [direct quote or specific observation] — [what it tells us]
- [direct quote or specific observation] — [what it tells us]

## Culture Fit
**X/5** — [rationale grounded in observed behavior]

## Recommendation
**[Advance / Hold / Pass]** — [one-sentence rationale]
```

## Failure modes

- **Strengths/concerns read as vibes** → re-read the notes and pull the specific quote. If you can't find one, the point wasn't actually observed.
- **Summary is 5+ sentences** → cut to 3. The user who reads this will make a decision in 15 seconds.
- **Recommendation doesn't match the balance of strengths vs concerns** → it's OK to Hold on a candidate with strong answers; write a rationale that names the specific concern that's holding them back.
