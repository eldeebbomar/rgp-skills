---
name: grade-job-preview-test
description: Grade a candidate's Job Preview Test (JPT) submission against a role-specific rubric. Produces per-criterion scores with evidence, a pass/fail decision, and 3-sentence candidate-facing feedback. Use this skill whenever the user mentions grading a JPT, scoring a candidate work sample, evaluating a Stage-2 submission, or wants structured feedback to send to a candidate after a take-home test — even if they don't explicitly call it a "JPT."
---

# Grade Job Preview Test

Evaluate a candidate's JPT submission for a specific role at RGP. Produce internal scores with evidence, a pass/fail decision, and a short candidate-facing feedback note — in a format the team can use directly for the advance/reject decision and the email back to the candidate.

## When to use this

The user has a candidate's JPT submission (code, document, analysis, video, whatever the role's JPT asks for) plus the role-specific rubric. They need a structured grade *plus* a drafted feedback note for the candidate. This is RGP's Stage 2 — medium volume, higher stakes, the gate before live interviews.

## Inputs

Three inputs, all required:

- **`role_summary`** — one-paragraph summary of the role: title, level, key responsibilities, must-have skills.
- **`rubric`** — the role-specific JPT rubric. Should list 4–6 criteria with descriptions of what each measures.
- **`submission`** — the candidate's submitted work. Paste as-is; don't summarize. If the submission is a file format you can't paste (a .docx, a video), ask the user to paste the text content or a transcript.

## Process

Ground every score in the submission. Don't defer to the rubric's wording without pointing to the specific element that earned the score.

1. Read the role summary, rubric, and submission carefully. The order matters — the role frames what "good" looks like.
2. Inside `<thinking>` tags, match specific parts of the submission to each rubric criterion before scoring.
3. Score each criterion 1–5. For every score, cite the exact element of the submission that drove it.
4. Write one improvement suggestion per criterion scored below 4. Specific suggestions ("add error handling for empty inputs") beat vague ones ("the code could be cleaner").
5. Decide overall Pass or Fail. Pass = the submission meets the bar to move to live interviews. Fail = it doesn't.
6. Draft 3-sentence candidate-facing feedback. Professional, specific, kind. Translate internal scores into plain language — the candidate must never see rubric numbers, the word "rubric," or the abbreviation "JPT."

## Calibration

- **Pass**: submission demonstrates the core competency with minor rough edges. A teammate at this level would be productive in the first week.
- **Fail**: submission misses a core competency, or has enough gaps that onboarding would be costly.
- **Borderline**: if you're genuinely torn between Pass and Fail, lean Fail and note what would have tipped it. Borderline candidates who Pass consistently underperform; it's cheaper to say Fail with a kind note.

## Guardrails

- **Don't invent details.** If the submission doesn't show something, the score reflects its absence.
- **Missing rubric is a hard stop.** If the rubric is missing or ambiguous, ask for clarification before grading. Guessing the rubric generates inconsistent grades.
- **Candidate-facing feedback uses plain language.** Never reference "rubric", "JPT", "score", "criterion", or numeric scores. Say "we've decided not to move forward at this stage," not "you failed."
- **No moral commentary.** The feedback is about the work, not the candidate as a person.

## Output format

ALWAYS use this exact template:

```markdown
## Criterion Scores
| Criterion | Score | Evidence | Improvement (if < 4) |
| --- | --- | --- | --- |
| [criterion name] | X/5 | [specific element from submission] | [concrete suggestion, or leave blank if ≥ 4] |

## Overall
**Pass** | **Fail** — [one-sentence internal rationale]

## Feedback to Candidate
[exactly 3 sentences, candidate-facing, no internal terms]
```

## Examples

**Example — candidate-facing feedback done right:**

> "Thank you for taking the time to complete the take-home. We were particularly impressed by your approach to modeling customer churn, especially the feature-selection rationale. After careful review we've decided not to move forward at this stage; for roles like this we prioritized candidates with deeper experience in production ML pipelines."

Three sentences. Specific praise. Specific reason. No internal language.

**Example — candidate-facing feedback done wrong:**

> "You scored 2/5 on 'production readiness' per the JPT rubric. Failing. Better luck next time."

Internal terms. Score leak. Cold. Not what gets sent.

## Failure modes

- **Claude tries to grade without a rubric** → stop and ask; never proceed.
- **Feedback references scores or rubric terms** → rewrite in plain language before sending.
- **Overall is forced to Pass on a borderline case** → default to Fail; the team can override with context.
