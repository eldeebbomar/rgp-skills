---
name: candidate-rejection-email
description: Draft an empathetic, specific candidate rejection email under 150 words. Warm, professional, honest — without corporate filler. Use this skill whenever the user mentions drafting a rejection, telling a candidate they didn't get the role, writing a "not moving forward" note, or is worried about how to deliver hard news well — even if they don't explicitly say "rejection" or "email."
---

# Candidate Rejection Email Draft

Write a rejection email that respects the candidate's time and effort while being honest about the decision. Warm, specific, under 150 words, no corporate filler.

## When to use this

The user has decided not to advance a candidate (from any stage) and needs to send the news. The skill handles the awkward part — being kind without being fake, being specific without being brutal.

## Inputs

Four inputs, all required:

- **`name`** — candidate's first name.
- **`role`** — role title the candidate applied for.
- **`reason`** — internal rejection reason. Do NOT quote this verbatim to the candidate; it's context for you.
- **`observations`** — 2–3 specific observations from the interview(s). What the candidate did well, what concerned the team, moments that stood out.

## Process

1. Open with direct acknowledgment and thanks. No throat-clearing ("I hope this finds you well").
2. Name one genuine positive signal from the observations. If there's nothing genuine, skip this step — warmth beats fake flattery.
3. Deliver the decision in one sentence. Use "decided" or "won't be moving forward."
4. Give one specific, actionable reason drawn from the observations — not the internal rejection reason verbatim. The reason should tell the candidate something they could work on or position differently next time.
5. Close with a forward-looking line (future opportunities, feedback openness) ONLY if genuine for this candidate.
6. Sign off warmly. Avoid "best regards"; use "Thank you again" or "Wishing you well."

## Calibration

**Strong specific reason:**
> "For this role we prioritized candidates with direct experience running SDR workflows end-to-end, and we saw stronger track records on that specifically."

**Weak reasons (avoid):**
- "We found someone better." — too generic.
- "You didn't do well on the call." — too blunt, not actionable.
- "We've decided to go in a different direction." — corporate filler.

The strong version tells the candidate *something they could use* for their next application.

## Guardrails

- **Never invent praise.** If the observations don't support a positive signal, skip the opener. Fake warmth reads as fake and damages RGP's reputation with the candidate network.
- **Never reveal internal language verbatim.** The internal reason is your frame, not the message.
- **Never promise future consideration.** Only mention future opportunities if the observations genuinely suggest a different role could fit.
- **Never reference competitors, comp, or other candidates.** None of that is the candidate's business.
- **Word count: under 150.** Count them. If you're over, cut the forward-looking line first.

## Output format

ALWAYS use this exact template:

```
Subject: [subject line]

[email body — plain text, under 150 words, signed warmly]
```

## Examples

**Example — good rejection email:**

> Subject: Update on the SDR role at Acme
>
> Hi Maya,
>
> Thank you for the time you spent on the take-home and the live interview — we appreciated both.
>
> One thing that stood out was your thoughtfulness about onboarding workflows; that's rare in an SDR interview.
>
> After careful consideration, we've decided not to move forward with your candidacy for the SDR role. For this specific position we prioritized candidates with direct experience running outbound cadences in B2B SaaS at $50k+ ACV, and we saw stronger track records on that specifically.
>
> We'd be happy to keep you in mind if a role closer to your experience opens up. Wishing you well in your search.
>
> — The RGP team

142 words. Specific praise. Specific reason. No filler. Room to keep the door open.

## Failure modes

- **Output is too corporate** → cut any phrase that could have come from any company (e.g., "moving in a different direction").
- **Praise feels forced** → drop it; warmth in the rest of the email carries it.
- **Reason is generic** → pull a more specific one from the observations, or mark the skill as needing more detail in the observations.
