---
name: 2-ea-stakeholder-map
description: Builds the stakeholder map of an enterprise architecture case in political, document-safe language. For each person it states power, stance, what they care about, strength, risk and what to talk about in a one-to-one conversation; adds a general reading of the tensions, the current affinities, a 14-day workload survey for every director and a list of open questions. Use this whenever an architect, consultant or candidate needs to understand who decides what in a case, prepare stakeholder conversations, unblock an executive deadlock, or present stakeholders in a deck without exposing anyone, even if they never say "stakeholder". Works from the case text and the user's notes. Never invents facts and never writes personal traits.
---

# EA stakeholder map

**Step 2 of the case method.** Previous: `1-ea-scope-and-objectives` (use its scope and objectives as input).

Help an enterprise architect turn a case and their notes into a stakeholder map that can be shown to the people in it: what each person needs, what each person risks, and what to talk about with each of them, without judging anyone.

Most stakeholder maps fail in one of two ways: they are a list of names with no use, or they are honest notes that would offend half the room if shared. This one is useful and safe to share.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_NAME` / `INGRESA_NOMBRE`.

## Flow

Work with the user: read their case and notes, draft the whole section, then take corrections. Review the notes line by line before delivering, and say explicitly what you added from them and what you left out on purpose.

### 1. List every stakeholder

Include everyone who can block, push or be affected by the initiative: the CEO, the board or owners, each director involved, and key people below director level when the case names them (a successor, a key engineer). Use job titles exactly as the case writes them (CEO, CFO, CTO) plus the name.

### 2. Write the general reading

Three or four sentences that explain the deadlock without blaming anyone:

- The **legitimate priorities in tension** (for example, commercial speed versus operational stability). Frame both as legitimate.
- **Who should be arbitrating and is not** (a formal owner who stepped back, a CEO who delegates).
- **The governing principle** of the initiative, when there is one (in an acquisition: the integration is governed under the acquiring company's structure, and the acquired company contributes its strengths).
- The **14-day workload survey** (see step 5).

### 3. Fill the table

| Person | Power | Stance | What they care about | Strength | Risk | What to talk about in the one-to-one |
|---|---|---|---|---|---|---|

Column rules:
- **Power:** high, medium or low, with the source of that power in a few words (formal mandate, results, alliances, knowledge).
- **Stance:** their position on the initiative as it stands today (pushes for speed, protects the operation, stepped back, delegated). Facts from the case, not judgments.
- **What they care about:** what measures their success.
- **Strength:** what they bring to the initiative.
- **Risk:** what can go wrong around this person, written as a situation, not as a flaw ("a platform moving in parallel without governance", not "he is a politician").
- **What to talk about in the one-to-one:** the concrete ask or proposal for this person. Lead roles beat vetoes: give an executive with a formal mandate the leadership of their part, and promise them information that arrives in order (what changes, what risk it carries, how it is reverted) so they decide without attending every meeting.
- The board does not get a one-to-one: it receives the governance proposal for approval and is the final escalation.

### 4. Write the current affinities

One or two sentences naming who agrees with whom today (who pushes for speed, who protects stability). Use "affinities", never "blocks" or "sides".

### 5. Add the 14-day workload survey

Every director (not the CEO or the board) validates a one-page template, collected by the architect in the one-to-one so it is not extra homework:

| # | Question |
|---|---|
| 1 | What is your area doing today and what are its commitments this quarter? |
| 2 | Which metrics do you have to meet? |
| 3 | What is taking longer than expected, and why? |
| 4 | What repetitive work could be automated? |
| 5 | Which processes or initiatives could be paused or stopped to make room for the initiative? |

The answers feed a proposal of what to deprioritise to free capacity. Repetitive work that does not free capacity for the initiative is noted for later, so the initiative does not drift.

### 6. Keep the open questions

Anything the plan depends on and the case does not state goes into a table, never into the map as an assumption:

| # | Question | Ask whom | Why it matters |
|---|---|---|---|

## Political wording rules

The map will be read by the people in it. Write accordingly:

- **No personal traits.** Leave out "anxious", "disorganised", "political", "impatient", "nobody knows what she thinks", health conditions and family gossip. Keep interests, strengths and risks.
- **No blame.** A past incident is a risk ("tight deadlines that compromise stability"), never "caused by".
- **No exposure.** Sensitive findings (wrong figures, bad news someone has not heard yet) do not appear in the map. Write the neutral action ("update the business case") and handle the detail privately.
- **Bad news is delivered, not read.** If a stakeholder has not been told something, it goes into their one-to-one, not into a document they will read first.
- **Acquisitions:** never write that the acquired company "must adapt". Write that the initiative is governed under the acquirer's structure and the acquired company contributes its strengths.
- **No abbreviations**, except job titles exactly as the case writes them (CEO, CFO, CTO).
- **Facts, interpretations, assumptions.** Keep them apart. An assumption (for example, two people being related because they share a surname) is never written as fact.

## Output format

```
## 2. Stakeholders

<general reading: 3–4 sentences>

<table: person · power · stance · what they care about · strength · risk · what to talk about in the one-to-one>

### Workload survey (days 0 to 14)
<5-question template + one line on what it feeds>

### Current affinities
<1–2 sentences>

### Open questions for the one-to-ones
<table>
```

## Example

A complete fictional example is in `references/example-es.md`. Read it before writing the map.
