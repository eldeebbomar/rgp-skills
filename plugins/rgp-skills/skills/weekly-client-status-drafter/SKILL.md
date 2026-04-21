---
name: weekly-client-status-drafter
description: Turn a week of activity notes into a polished, email-ready client status update under 250 words. Concise, confident, forward-leaning, numbers where possible. Use this skill whenever the user mentions a weekly client update, a status email, a Friday recap to a client, or is drafting a recurring touchpoint to an active account — even if they don't explicitly say "status" or "update."
---

# Weekly Client Status Drafter

Convert the week's rough activity notes into a client-ready status update. 250 words max, led by a one-line headline, numbers where they're available, specific asks where the client needs to decide.

## When to use this

The user is an account manager closing out the week on an active role. They have a mix of "we screened 20 candidates, 5 went to JPT, 2 passed, 1 scheduled for client interview, client asked about comp range, need to circle back on timezone requirement." They need that turned into a clean email in under 5 minutes.

## Inputs

Two inputs:

- **`notes`** — raw activity notes from the week. Bullets OK. Includes candidate counts, milestones, blockers, open threads with the client.
- **`client_context`** — 2–4 lines on the client: roles open, timeline, communication style preferences (formal vs casual), anything else that shapes tone.

## Process

1. Lead with a one-line headline — the single most important thing from this week. If the week had a clear win, lead with it. If it had a clear problem, lead with that.
2. Wins this week: 2–4 bullets with numbers where possible.
3. In progress: 2–3 bullets on active work without over-promising.
4. Blockers or decisions needed from the client: 0–2 bullets. Specific; ask clear questions.
5. Next week: one short paragraph.

## Calibration

**Strong bullet (use this style):**
> "Shipped 5 vetted candidates to the SDR role — 2 now scheduled for your Friday panel."

**Weak bullet (rewrite):**
> "Made progress on the SDR role."

The difference: strong bullets carry numbers and commit to outcomes; weak bullets are filler. The client reads this in 30 seconds — every bullet must earn its line.

## Guardrails

- **Never invent numbers.** If the notes don't have a count, describe qualitatively ("several candidates") rather than making up a number.
- **Stay under 250 words.** If you go over, cut the "In progress" section first. Clients who get 400-word status emails stop reading them.
- **Never reveal internal details.** No cost/margin discussion. No sourcing-channel specifics. No internal candidate scoring.
- **Match the client's tone** per `client_context`. A casual client gets a casual update; a formal client gets a formal one.

## Output format

ALWAYS use this exact template:

```markdown
**Headline**: [one line — the most important thing this week]

**Wins this week**
- [bullet with numbers]
- [bullet with numbers]

**In progress**
- [bullet — active work, honest scope]
- [bullet]

**Decisions needed from you**
- [specific question], or "None this week."

**Next week**
[one short paragraph — what's planned]
```

## Examples

**Example — clear decisions-needed bullet:**

> "Do you want to raise the comp range to $70–85k? Two strong candidates declined at $60–70k citing market rate; a bump would reopen the top of our pipeline."

Specific, framed with evidence, asks for a clear decision.

**Example — vague decisions-needed bullet (don't do this):**

> "Comp might be an issue."

Leaves the client with no action.

## Failure modes

- **Over 250 words** → cut "In progress" first, then soften wins.
- **Headline is generic** ("here's your weekly update") → rewrite it to name the most important thing specifically.
- **Bullets invent numbers** → replace with qualitative phrasing until the account manager confirms counts.
