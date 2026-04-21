---
name: linkedin-profile-fit-assessment
description: Score a LinkedIn profile against a role on 5 fit dimensions and decide Reach out / Skip / Needs human review in under 2 minutes per profile. Returns a one-sentence outbound hook if reaching out. Use this skill whenever the user mentions triaging a LinkedIn profile, running through a sourcing list, making a fast reach-out decision, or batch-scoring candidates against a role — even if they don't explicitly say "fit."
---

# LinkedIn Profile → Fit Assessment

Fast sourcing triage. Score a profile on 5 dimensions, compute the average, make a binary-ish decision (Reach out / Skip / Needs human review), and — if reaching out — propose a one-sentence hook the recruiter can use in the outbound.

## When to use this

The user is working through a sourcing list and wants to decide quickly whether a profile is worth the reach-out effort. This skill replaces the "I'll triage these when I have time" bottleneck that stalls every sourcing push.

## Inputs

Two inputs:

- **`role_summary`** — the role: title, must-haves, timezone requirements, hard disqualifiers.
- **`profile`** — the candidate's LinkedIn profile content. "About" section + recent roles + skills is enough. Either pasted text or a structured summary.

## Process

1. Inside `<thinking>` tags, check each rubric item against the profile before scoring. The thinking step keeps the decision grounded in the profile, not in a gut reaction.
2. Score each dimension 1–5 with a one-line rationale citing a specific profile element.
3. Compute the average (1 decimal place).
4. Make the decision per the thresholds below.
5. If Reach out: propose a one-sentence hook — a specific detail from the profile the recruiter could use to open the outbound.

## The rubric

Score 1–5 on each:

1. **Skills match** — how close are the candidate's demonstrated skills to the must-haves?
2. **Experience level** — right seniority for this role?
3. **Career trajectory** — upward / lateral / regressing?
4. **Location / timezone fit** — compatible with role requirements?
5. **Likely responsiveness** — recent activity, openness signals (e.g., "#OpenToWork"), recent job change.

## Decision thresholds

- **Reach out**: average ≥ 3.5 AND location/timezone is compatible (no hard disqualifier).
- **Skip**: average < 2.5, OR a hard disqualifier (wrong timezone, recent layoff with no openness signal, clearly overqualified with no motivation signal).
- **Needs human review**: anything in between, OR an unusual trajectory that might still be interesting (career change, gap year, non-traditional path).

## Guardrails

- **Don't invent responsiveness.** If the profile doesn't show recent activity, score responsiveness low and say so. Inflated responsiveness scores waste recruiter time.
- **Never base fit on name, gender, ethnicity, or appearance.** This is a hard rule.
- **Don't penalize gaps without cause.** A gap year isn't negative trajectory — note it and proceed; let human review handle context.
- **Default to Needs human review on unusual profiles.** If the score is ambiguous and the profile is interesting, route to human review rather than Skip.

## Output format

ALWAYS use this exact template:

```markdown
## Fit Scores
| Dimension | Score | Rationale |
| --- | --- | --- |
| Skills match | X/5 | [specific profile element] |
| Experience level | X/5 | [specific profile element] |
| Trajectory | X/5 | [specific profile element] |
| Location / timezone | X/5 | [specific profile element] |
| Responsiveness | X/5 | [specific profile element] |

## Average fit
**X.X / 5**

## Decision
**[Reach out / Skip / Needs human review]** — [rationale]

## Hook (if Reach out)
[one sentence referencing a specific profile detail]
```

## Examples

**Example — good hook:**

> "Noticed you spent 2 years scaling outbound at Latch from 20 to 200 accounts — we're placing someone with a client tackling exactly that transition."

Specific, flattering without fawning, sets up the outbound.

**Example — weak hook (don't use):**

> "Your experience looks like a great match for our client."

Generic. Could be sent to anyone. No opening.

## Failure modes

- **Responsiveness score inflated with no evidence** → drop to 2/5 and note "no recent activity signal."
- **Decision forced to Reach out on ambiguous average** → default to Needs human review; recruiters prefer a small review queue to a noisy outbound list.
- **Hook is generic** → re-read the profile and pull a specific moment or number.
