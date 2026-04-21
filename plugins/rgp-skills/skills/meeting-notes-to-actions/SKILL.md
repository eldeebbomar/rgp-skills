---
name: meeting-notes-to-actions
description: Extract action items with owners and deadlines from meeting notes or a transcript. Returns a clean action table plus decisions made and open questions — never invents commitments. Use this skill whenever the user mentions meeting notes, a transcript, standup notes, recapping a call, or wants action items pulled out of a conversation — even if they don't explicitly say "action items."
---

# Meeting Notes → Action Items

Pull every commitment, decision, and open question out of meeting notes. Every action gets a named owner and a specific due date. Never invent commitments; never infer decisions that weren't made.

## When to use this

The user has meeting notes or a transcript (their own, or auto-generated from a tool like Granola). The meeting ended 10 minutes ago and now it's time to send the "here's what we agreed" recap — or load tasks into the team's tracker. This skill handles the extraction so the AM / manager can focus on sending.

## Inputs

One input:

- **`notes`** — raw meeting notes or transcript. Messy bullet-form or narrative is fine. Auto-generated transcripts with timestamps also work — the skill reads through them.

## Process

1. Inside `<thinking>` tags, list every phrase in the notes that sounds like a **commitment** ("I'll send…", "can you do…"), a **decision** ("let's go with…", "we agreed…"), or an **open question** ("we didn't decide…", "need to ask…"). Do this before building the table; this catches commitments buried in narrative text that are easy to miss in a single pass.
2. Build the Action Items table. Every row must have: Action, Owner, Due (YYYY-MM-DD), Context.
3. If the notes don't state an owner, mark Owner as `⚠️ TBD` and note it — never guess who owns something.
4. If the notes don't state a due date, infer conservatively (e.g., "next week" → next Friday) and prefix the inferred value with ⚠️ so the user can confirm.
5. Capture decisions that were actually made in a separate bulleted section.
6. Capture open questions (raised but not resolved) in a separate bulleted section.

## Calibration

**Strong action (use this style):**
> "Send vetted candidate list to Acme for the SDR role | Omar | 2026-04-22 | Acme needs to interview by Friday."

**Weak action (rewrite):**
> "Omar will send stuff."

Strong = specific scope, named owner, concrete date, one-line context. Weak = none of the above.

**Strong decision (capture):**
> "Decided to pause the Marketing Ops role until Q3."

**Weak decision (don't capture):**
> "We talked about the Marketing Ops role."

Talking isn't deciding. Only include things the meeting actually resolved.

## Guardrails

- **Don't invent commitments.** If no one owns something, Owner = `⚠️ TBD`. It's the meeting notes that are incomplete, not a problem to paper over.
- **Don't invent decisions.** Only what was actually resolved. Speculation reads as fact after the meeting.
- **Dates in YYYY-MM-DD format.** If "next week," infer the date and prefix ⚠️.
- **Flag incomplete notes.** If the notes are clearly partial (missing a segment, ending mid-sentence), write "Notes may be incomplete" at the top.
- **Don't interpret conflict.** If two people seemed to disagree, capture both positions in "Open questions" — don't pick a winner.

## Output format

ALWAYS use this exact template:

```markdown
## Action Items
| Action | Owner | Due | Context |
| --- | --- | --- | --- |
| [specific action] | [Name, or ⚠️ TBD] | [YYYY-MM-DD, or ⚠️ prefix if inferred] | [one-line context] |

## Decisions made
- [decision]

## Open questions
- [question that was raised but not resolved]
```

## Examples

**Example — handling "next week" inference:**

> | Send vetted candidate list to Acme | Omar | ⚠️ 2026-04-24 | Acme said "get it to me by end of next week" |

The ⚠️ tells the user to confirm the date before committing it to the tracker.

**Example — handling ambiguous ownership:**

> | Follow up with Acme's hiring lead on the start-date change | ⚠️ TBD | ⚠️ 2026-04-24 | Raised in the call; no one volunteered to own. |

The user sees exactly what they need to confirm — both the owner and the date.

## Failure modes

- **Commitments missed** → they were probably buried in narrative; re-read with the specific phrasing in mind ("I'll", "can you", "we'll", "I need to").
- **Decisions inflated** → drop anything that was "discussed" but not actually resolved.
- **All dates prefixed with ⚠️** → that's fine; it means the notes were vague. The user will calibrate the dates before sending.
