---
name: shortlist-deck-builder
description: Turn shortlisted candidates into a client-ready narrative with positioning, strengths mapped to client priorities, honest tradeoffs, and a recommended meeting order. Use this skill whenever the user mentions building a shortlist deck, presenting candidates to a client, prepping finalist materials, or wants each candidate framed around a client's stated priorities — even if they don't explicitly say "deck" or "shortlist."
---

# Shortlist Deck Builder

Produce a client-facing candidate narrative: per-candidate positioning, strengths explicitly tied to the client's priorities, honest tradeoffs, one suggested interview question per candidate, and a recommended meeting order with a reason.

## When to use this

The user has 3–5 candidates who've cleared internal vetting and needs the writeup the client will read before interviews. This is the moment where RGP's framing of the candidate shapes the client's perception — specific framing wins interviews, generic framing wastes them.

## Inputs

Two inputs:

- **`priorities`** — what the client said matters most, in their own words where possible. From the kickoff call, recent email, or the job spec's ideal candidate profile.
- **`candidates`** — 3–5 candidate summaries, each labeled with a name plus 1–2 paragraphs on background, strengths, known gaps. Interview summaries from the `interview-notes-summary` skill work well here.

## Process

For each candidate, in order:

1. 2-sentence **positioning** — why THIS candidate, for THIS role, for THIS client. The positioning should read differently for a different client with different priorities.
2. Top 3 **strengths**, each explicitly mapped to a client priority from the input. Format: `[strength] → [priority it addresses]`.
3. Honest **tradeoffs** — where the candidate is weaker. No filler ("their only weakness is they work too hard").
4. One specific **interview question** the client should ask — either to validate a strength or probe a tradeoff.

After all candidates, a 2-sentence recommended **meeting order** and why. Common pattern: start with the strongest communicator so the client calibrates the bar; end with the most unconventional so the conversation stays fresh.

## Calibration

**Strong strength-to-priority mapping:**
> "Led outbound at [Company] from 0 → $2M ARR in 18 months → directly maps to your 2026 ARR target."

**Weak strength:**
> "Strong sales background."

**Strong tradeoff:**
> "Spent the last 2 years in enterprise; may need coaching on mid-market motion in month 1."

**Weak tradeoff (don't use):**
> "No major weaknesses."

Every candidate has at least one real tradeoff. Writing "no tradeoffs" signals the summary is incomplete.

## Guardrails

- **Don't invent experience.** If a candidate's summary doesn't support a strength, don't list it.
- **Tradeoffs must be real.** No "their only weakness is they work too hard"–style filler.
- **No internal details.** Compensation, negotiation, process details never appear in the client-facing deck.
- **No demographic framing.** Positioning and tradeoffs describe work fit, not country, gender, age, school.
- **Strength → priority mapping must cite the priority by name or paraphrase.** The arrow isn't decorative — it's the argument.

## Output format

ALWAYS use this exact template:

```markdown
## [Candidate 1 name]
**Positioning**: [exactly 2 sentences — why this candidate, this role, this client]

**Top strengths for this role**:
- [strength] → [client priority it addresses]
- [strength] → [client priority it addresses]
- [strength] → [client priority it addresses]

**Tradeoffs**:
- [honest tradeoff]

**Suggested interview question**: [specific question]

## [Candidate 2 name]
...

## Recommended meeting order
[2 sentences — the order + why]
```

## Examples

**Example — positioning done right:**

> "Maya spent 3 years turning Stripe's outbound function into a repeatable motion — exactly the 'build a playbook, don't just run one' profile you described in kickoff. Where she's different from your other finalists is her comfort with ambiguity; she built that playbook from nothing."

Two sentences. References kickoff language ("build a playbook") and names what's different about her.

**Example — positioning done wrong:**

> "Maya is a strong SDR with experience at Stripe. She has a good track record."

Nothing about the client. Nothing about the role. Nothing the client couldn't have gotten from her LinkedIn.

## Failure modes

- **Strengths don't map to priorities** → re-read the priorities input and rewrite the strength-to-priority arrow with the client's own language.
- **Tradeoffs are filler** → every candidate has one real tradeoff; name it specifically.
- **Meeting order rationale is generic** ("start with the strongest") → tie it to a specific candidate-level observation.
