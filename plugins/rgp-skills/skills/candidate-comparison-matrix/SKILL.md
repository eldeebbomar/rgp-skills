---
name: candidate-comparison-matrix
description: Compare 3–5 shortlisted candidates side-by-side on role-specific dimensions. Returns a decision-ready matrix, a recommended ranking, and the single most important tradeoff to flag. Use this skill whenever the user mentions comparing candidates, wants a shortlist matrix, is prepping a client deck, needs to rank finalists, or is stuck deciding between two strong candidates — even if they don't explicitly say "matrix" or "comparison."
---

# Candidate Comparison Matrix

Turn 3–5 candidate summaries into a side-by-side comparison across the dimensions that actually matter for THIS specific role — not a generic list. Produce a matrix, a recommended ranking with rationale, and one sentence on the tradeoff the client should know about.

## When to use this

The user has shortlisted 3–5 candidates and needs to decide (or help a client decide) who to prioritize. This skill is the synthesis step between individual interview summaries and the final shortlist deck.

## Inputs

Two inputs:

- **`role_summary`** — the role, its priorities, and the client's stated must-haves. Paste the job spec or the key priorities from the kickoff.
- **`candidates`** — 3–5 candidate summaries, each labeled with a name and 1–2 paragraphs on background, experience, standout signals. Interview summaries from the `interview-notes-summary` skill work well here.

## Process

1. Inside `<thinking>` tags, derive the 6–8 dimensions that actually matter for THIS role. Tie each to the role context — if the role prioritizes async communication, that's a dimension; if it prioritizes outbound volume, that's a dimension. Do not use a generic list of "communication / skills / experience / fit."
2. For each candidate, fill each dimension with ≤1 sentence or a numeric score. Keep cells short so the matrix stays scannable on one screen.
3. Recommend a ranking (1st, 2nd, 3rd, …) with a 2-sentence rationale per rank that references specific dimensions.
4. End with one sentence on the single tradeoff the client should know — where the top pick is weaker than the runner-up.

## Calibration

Dimensions must be specific enough to be measurable:

**Strong dimension:**
- "Timezone overlap with SF team (hours)"
- "Proven outbound volume at scale"
- "Domain fluency in SaaS sales cycles"

**Weak dimension (rewrite these):**
- "Good communicator" → "Proven async written communication"
- "Team player" → "Evidence of cross-functional collaboration"

The rule: if two candidates could be honestly scored the same on a dimension despite clearly being different, the dimension is too generic.

## Guardrails

- **Don't invent experience.** If a candidate's summary doesn't support a claim, don't put it in the matrix. The matrix is an audit surface.
- **Don't force a rank if candidates are genuinely tied.** Tied candidates should be labeled "1st (tie)" — the client can break the tie live.
- **No demographic dimensions.** Dimensions describe work fit. Never country, age, gender, school prestige.
- **At minimum 3 candidates.** If fewer than 3 are provided, note it — the matrix is less useful at 2 candidates; a straight A-vs-B comparison is often clearer.

## Output format

ALWAYS use this exact template:

```markdown
## Comparison Matrix
| Dimension | Candidate A | Candidate B | Candidate C |
| --- | --- | --- | --- |
| [dimension 1] | [≤1 sentence or score] | ... | ... |

## Recommended Ranking
1. **[Name]** — [2-sentence rationale referencing specific dimensions]
2. **[Name]** — [2-sentence rationale]
3. **[Name]** — [2-sentence rationale]

## Tradeoff to Flag
[one sentence — where the top pick is weaker than the runner-up]
```

## Examples

**Example — strong rationale in ranking:**

> "**Maya** — Highest on outbound volume (demonstrated 500/wk at Latch) and timezone overlap (6 hours with SF). Slightly below Diego on domain fluency but the gap closes within a month of onboarding."

That sentence lets the next reader see the exact tradeoff you weighed.

## Failure modes

- **Dimensions are too generic** → rewrite until two different candidates score differently on the dimension.
- **Ranking rationale doesn't reference the matrix** → the matrix and the rationale should read as the same argument from two angles.
- **Tradeoff to flag is vague** → name the specific dimension and by how much the top pick trails.
