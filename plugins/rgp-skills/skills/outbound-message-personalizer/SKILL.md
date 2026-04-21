---
name: outbound-message-personalizer
description: Produce 3 personalized outbound message variants for a passive candidate — different angles, each under 90 words, each opening with something specific from their profile. Use this skill whenever the user mentions writing outbound messages, cold outreach, LinkedIn InMails, sourcing messages, or wants to reach a passive candidate without sounding like a bot — even if they don't explicitly say "outreach."
---

# Outbound Message Personalizer

Write 3 short outbound message variants for a specific candidate, each under 90 words, each opening with something concrete from the candidate's profile, each taking a different angle (career growth / impact / flexibility). The goal is a reply rate — not a cold-template carpet bomb.

## When to use this

The user has identified a passive candidate and wants to reach out — but doesn't want to send the same three template messages everyone else in their ATS sends. Short variants let them A/B test tone and hook without writing from scratch each time.

## Inputs

Two inputs:

- **`profile`** — the candidate's LinkedIn, resume, or a background summary. Must include recent roles, projects, tools, public signal (talks, writing, open source).
- **`role_summary`** — the role you're pitching. Title, company, one sentence on what makes it unusually good for this candidate.

## Process

1. Inside `<thinking>` tags, identify 2–3 specific, non-generic details from the candidate's profile. A company they worked at, a project, a tool, a career transition, a numeric achievement. Generic traits ("impressive profile", "great experience") are not details.
2. Write three variants labeled A, B, C. Each:
   - Opens with a specific detail from step 1.
   - Leads with what's in it for them, not us.
   - Has exactly one clear call-to-action at the end.
   - Stays under 90 words.
3. Use three different angles:
   - **A = career growth** (what's the next move on their ladder)
   - **B = impact / mission** (what their work would unlock)
   - **C = flexibility / lifestyle** (timezone, async, travel, autonomy)

## Calibration

**Strong opening (use this style):**
> "Saw you moved from IC at Stripe to leading a 4-person SDR team at Latch — that's the exact arc we're looking for on [client]'s team."

**Weak opening (avoid):**
> "I came across your profile and was impressed by your experience."

The strong version: the candidate knows this message was written FOR them. The weak version could have been sent to anyone.

## Guardrails

- **Don't invent details.** Every opening line traces to the candidate's actual profile. If there's nothing specific enough in the profile, stop and say so — better to request more profile detail than send a hollow message.
- **Never "I hope this finds you well."** It's filler. Cut it and open with the specific detail instead.
- **No emoji, no exclamation marks.** Professional tone. Warmth comes from specificity, not punctuation.
- **Never mention compensation.** Compensation comes up after a reply, not in the opener.
- **One CTA per message.** Two CTAs ("let's chat OR book time OR reply with Y") dilutes the ask.

## Output format

ALWAYS use this exact template:

```markdown
## Variant A — Career growth
[message, plain text, under 90 words]

## Variant B — Impact / mission
[message, plain text, under 90 words]

## Variant C — Flexibility / lifestyle
[message, plain text, under 90 words]
```

## Examples

**Example — good Variant A (career growth angle):**

> "Saw the jump from IC to team-lead at Latch — going from running the playbook to building it. RGP is placing someone with [client], a post-Series B SaaS company that's looking for exactly that arc — someone to stand up their outbound motion from scratch, with real latitude on how to run it. 30 min this week to compare notes?"

80 words. Specific opening. Clear arc-to-arc pitch. One CTA.

## Failure modes

- **Three variants open the same way** → rewrite two of them with different specific details from the profile.
- **CTA is weak** ("let me know if you're interested") → replace with a concrete ask: "30 min this week," "open to a quick call Thursday or Friday?".
- **Message is over 90 words** → cut the second-last sentence first; outbound messages collapse under their own weight past 90 words.
