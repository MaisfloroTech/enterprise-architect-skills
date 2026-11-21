---
name: 1-ea-scope-and-objectives
description: Defines the scope and objectives of an enterprise architecture case before any map, diagram or roadmap is drawn. Separates the stated problem from the real one, lists the key negative findings, sets the scope (name, level, what is in and what is out), writes a general objective as a business outcome, breaks it into 4–6 objectives with the executive accountable for each and a deadline in days, and closes with a 90-day commitment with milestones at day 14, 30, 60 and 90. Use this whenever an architect, consultant or candidate needs to frame a case, scope an initiative (merger, integration, migration, new product, transformation), write objectives leadership will accept, or prepare an architecture case for an interview, even if they never say "scope". Keeps a list of open questions instead of assuming. Never invents numbers, dates or facts.
---

# EA scope and objectives

**Step 1 of the case method.** Next: `2-ea-stakeholder-map`.

Help an enterprise architect frame a case **before** drawing anything: what problem we are really solving, what is in and out, what the business must achieve, who answers for each result, and what gets done in the first 90 days.

Most architecture work fails here: the architect jumps to a capability map or a target architecture without agreeing on scope and objectives, and the executives never recognise the problem being solved. Fix that first.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_DATE` / `INGRESA_FECHA`, `ENTER_NUMBER` / `INGRESA_CANTIDAD`, `ENTER_OWNER` / `INGRESA_RESPONSABLE`.

## Always deliver the complete section

Draft the whole section from the case and the user's notes, then take corrections. After every correction, if the user asks to see it, deliver **the whole section again**, never loose fragments: people get lost when they have to stitch pieces together.

## Flow

Work **section by section with the user**. Show each section, take their corrections, and only move on when they close it. The user decides; you propose, explain the trade-off and push back when something is weak.

### 1. Read the case and separate three layers

| Layer | Question |
|---|---|
| **Stated problem** | What does the case say has to be done? |
| **Real problem** | Why hasn't it been done yet? (deadlock, no owner, no shared language, missing data) |
| **Key negative findings** | What did the discovery reveal that changes the risk of any option? (wrong data, knowledge about to leave, parallel initiatives without governance, bad news nobody has delivered) |

For each key negative finding, also note the **opportunity** it may hide (a person leaving can become a bridge between teams).

Separate **facts** (written in the case), **interpretations** (follow from the facts) and **assumptions** (not in the case). Never present an assumption as a fact.

### 2. Set the scope

Answer four things:

1. **Name**: short, recognisable, ideally using the case's own words. Mention it in full once; a short form is fine afterwards.
2. **Level**: whole company, a domain, a subdomain or a single capability. The map will go one or two levels below it, never at the same level or above.
3. **In scope**: the areas the initiative changes or depends on, grouped by domain. When systems or platforms are involved, describe each one in a small table: what it is and its current situation, using only what the case says.
4. **Out of scope**: areas the initiative does not change, with one line on why.

Filter question for every area: *does this initiative change it or depend on it?* If not, it is out.

### 3. Write the general objective

One sentence, written as a **business outcome**: the *why*, not the *how*.

- "Integrate the systems" is a *how*. "Recover market share without compromising operational safety" is a *why*.
- A product, project or platform is a **means**, never the objective. If the case proposes a product, it belongs in the specific objectives or behind a decision gate, not in the general objective.

### 4. Break it into 4–6 objectives

A table with four columns:

| # | Objective | Accountable for the result | Deadline |
|---|---|---|---|

Rules:
- **Results, not tasks.** "Launch product X" is a task; "product X on sale in the unified network by day N" is a result.
- **Accountable, not executor.** Name the executive who answers for the result (job title as the case writes it, plus the name). Execution owners belong to capabilities, later. One objective, one accountable executive: shared accountability means nobody answers. When two areas must work together, name one accountable and say what the other brings ("Director of Innovation, with the CTO's technical standards").
- **Deadlines in days** (day 0 to 90, day 90 to 270, day 270 to 540), never in vague words. An objective that applies all the time says "from day 0 and throughout".
- **Commercial work starts on day 0.** Sales and marketing actions do not wait for technology to be ready; split them if needed ("commercial design from day 0, technology support from day 90").
- **Decisions that unblock others go first and short.** If an open question (a business case, a figure) changes what gets built, give it a quick first checkpoint (day 14) and a complete version later.
- **Neutral wording.** Never write anything that exposes a person in a document everyone will read ("wrong numbers", "unvalidated data", "pause X's project"). Write "update the business case", "prioritise new developments according to it". Sensitive matters are discussed privately, not in the document.
- **People are not objectives.** Do not put a person's name inside an objective; use the role ("an integration lead") until the person has agreed in a one-to-one conversation.
- Six objectives is the limit.

### 5. Write the 90-day commitment

One SMART objective for the first 90 days, starting with "Plan and execute…" / "Planear y ejecutar…", answering what, why, when, where, who and how in 2–4 lines. Then a milestone table:

| Day | Deliverable |
|---|---|
| **14** | Quick checkpoint on the decision that unblocks everything else |
| **30** | Analysis validated with the areas involved (capabilities, maturity, options) |
| **60** | Decision approved and recorded in an architecture decision record |
| **90** | Roadmap approved with one owner per capability; first build step started |

Adapt the deliverables to the case; keep the day structure. Days are a proposal to agree with the executive committee: say so.

### 6. Keep a list of open questions

Anything the case does not state and the plan depends on goes into a table, never into the plan as an assumption:

| # | Question | Ask whom | Why it matters |
|---|---|---|---|

These questions feed the one-to-one conversations later.

## Output format

```
## 1. Scope and objectives

### Scope
Name · Level · In scope (with platform table if relevant) · Out of scope

### General objective
<one sentence>

### Objectives
<table: # · objective · accountable · deadline>

### 90-day commitment
<SMART sentence>
<milestone table: day 14 · 30 · 60 · 90>

### Open questions
<table>
```

## Rules

- **Never invent** numbers, dates, people, systems or facts. Missing data becomes a placeholder or an open question.
- **No abbreviations**, except job titles exactly as the case writes them (CEO, CFO, CTO). Write "architecture decision record", not ADR.
- **Simple over complete.** No filler, no methodology paragraphs, no references to how the document was produced. If a line does not help an executive decide, cut it.
- **Push back** when the user's draft confuses a means with an objective, names a person instead of a role, exposes someone, or uses words instead of days. Explain why in one or two sentences, then offer the corrected version.
- When a choice involves prioritising, remember that not everyone can be kept happy: sequencing a decision behind evidence is not the same as avoiding it.

## Example

A complete fictional example is in `references/example-es.md`. Read it before writing the first section.
