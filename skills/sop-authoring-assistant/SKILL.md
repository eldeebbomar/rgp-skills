---
name: sop-authoring-assistant
description: Turn rough notes on how a task is done into a clean, repeatable Standard Operating Procedure. Flags any step where the notes are ambiguous; never invents a step. Use this skill whenever the user mentions writing an SOP, documenting a process, capturing a workflow for a new hire, or turning tribal knowledge into something a teammate could follow — even if they don't explicitly say "SOP."
---

# SOP Authoring Assistant

Convert rough notes on a process into a Standard Operating Procedure clear enough that a new team member could follow it end-to-end. The skill's most important job is NOT inventing steps — if the notes are ambiguous, the SOP says so.

## When to use this

The user has done a task enough times to know how it works but hasn't written it down. They've scribbled notes, maybe dictated it in a voice memo, and now need to hand it to a new team member or a placed RGP contractor. This is the skill that turns muscle memory into documentation.

## Inputs

One input:

- **`notes`** — rough notes on how someone currently performs the task. Can be messy, bullet-form, narrative, out of order. If the notes are already structured, the skill still runs but adds less value.

## Process

1. Inside `<thinking>` tags, identify the **start state** (what triggers the task, what inputs are required) and the **end state** (what the task produces, how to tell it's done). This framing keeps the steps bounded.
2. Write the SOP using the structure in Output format.
3. Use **imperative voice** for every step ("Open…", "Paste…", "Click…"). Never "You should…" or "You might want to…".
4. One action per numbered step. If a step contains two verbs, split it.
5. For any step where the notes are unclear or incomplete, write `⚠️ UNCLEAR: [what's missing]` as the step and continue. Do not guess.
6. In "Edge cases", cover at least one failure path — what happens when the input is missing, what happens when a step errors.

## Calibration

**Strong step (specific, imperative, one action):**
> "3. Open the Clients table in Supabase and filter for `status = 'Active'`."

**Weak steps (rewrite):**
- "3. Check the clients." — too vague; what does "check" mean?
- "3. Open the Clients table in Supabase, filter by active status, copy the top 10 into a new spreadsheet." — three actions in one; split into 3a, 3b, 3c.

The rule: a new team member reading step 3 should know what to click, where to click, and what to do next.

## Guardrails

- **Never invent steps not in the notes.** If the notes skip a step, flag it with `⚠️ UNCLEAR` rather than filling it in.
- **Never merge actions.** One numbered step = one action. Multi-step instructions collapse when someone's halfway through and gets interrupted.
- **Never use "you should" or "you might want to."** Direct imperatives only.
- **Access prerequisites go in Prerequisites, not steps.** "Log into Supabase" at step 1 is noise; putting "Access to Supabase with admin role" in Prerequisites is signal.

## Output format

ALWAYS use this exact template:

```markdown
## Purpose
[1 sentence — why this SOP exists]

## When to use this
[1 sentence — the trigger]

## Prerequisites
- Access to X
- Context Y

## Steps
1. [imperative, one action]
2. [imperative, one action]
...

## Edge cases
- If [condition], do [action].
- If [input] is missing, [action].

## Quality check
[how to verify the SOP was followed correctly — 1–2 sentences]
```

## Examples

**Example — strong Edge cases section:**

> - If the Supabase query returns zero rows, check the `status` filter hasn't auto-set to `Archived`.
> - If the export CSV has missing `email` fields, re-run the join with `profiles` — the original query likely missed it.

Names the failure, names the fix. The new hire can self-correct without pinging someone.

## Failure modes

- **Steps are too long** → each step has exactly one verb; split multi-action steps.
- **⚠️ UNCLEAR flags missing** → re-read the notes; there's almost always a gap a new hire would hit. Zero flags is suspicious.
- **Edge cases section is empty** → even one is enough; if you can't think of one, the SOP isn't ready.
