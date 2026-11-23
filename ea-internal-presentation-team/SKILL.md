---
name: ea-internal-presentation-team
description: Turns a closed enterprise architecture case into a short internal presentation for the Enterprise Architecture team - how you studied the case and how you would lead it. Delivers a deck of about 14 slides in a fixed story (cover, scenario, facts, stakeholders as one team, risks per conversation, scope and objectives, plan for days 0-30 and 30-90, capabilities with owners, the architecture decision, traffic-light escalation with plan B, questions and resources), with few words per slide, facts only and speaker notes with the message and timing of each slide. Use this whenever someone needs to present an architecture case, a merger or integration proposal, an interview case or a review to an architecture team or panel, or asks to turn the case deliverables into slides, even if they never say "deck". Never invents facts.
---

# EA internal presentation to the team

**After the case method.** Use it once steps 1 to 8 are closed (last one: `8-ea-glossary`). Use what was closed in steps 1 to 8. If `ea-unified-case-excel` already built the workbook, the presentation points to it as the artifact delivered at the end.

Help an enterprise architect present the case to the **Enterprise Architecture team** (peers, leaders or an interview panel) in about 30 minutes: what they studied and how they would lead it. The slides tell the story; the detail lives in the artifact and in the speaker notes.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_NAME` / `INGRESA_NOMBRE`.

## Two layers

- **The slides** are read by the room. Facts of the case only, neutral wording, no judgments about people. Sensitive findings are named neutrally ("the data behind the acquisition requires review").
- **The speaker notes** are for the presenter. They can hold the internal reasoning (why this order of conversations, objections and answers, what is in each tab of the artifact), always with the same respect for the people of the case.

## Flow

### 1. Draft the outline first

Before building anything, deliver the slide-by-slide outline in one table and take corrections:

| # | Title (the message) | What goes on the slide | Visual | Notes: message and time |
|---|---|---|---|---|

After every correction, if the user asks to see it, deliver **the whole outline again**.

### 2. The story (about 14 slides)

| # | Slide | Source | What it shows |
|---|---|---|---|
| 1 | Cover | Step 1 | Name of the initiative, "Enterprise Architecture case", the presenter's name and "Internal presentation to the Enterprise Architecture team" |
| 2 | Today's scenario | Step 1 | The companies or areas involved, one line each. One line saying the full artifact is delivered at the end |
| 3 | Current facts | Steps 1 and 3 | Context facts on one side (market, acquisition, mandate, current system, history, today) and what the survey showed on the other. Facts only |
| 4 | One team, one objective | Step 2 | Every stakeholder around the shared objective, with name and job title. No sides, no power scores on the slide |
| 5 | What can put the initiative at stake | Steps 2, 3 and 5 | Table: conversation order, name, role, risk for the initiative. Footer: each risk is discussed first in private, in a one-to-one |
| 6 | Scope and objectives | Step 1 | Subtitle with the general objective. In / out of scope. Numbered objectives, each with a deadline in days |
| 7 | Days 0 to 30: understand and organise | Steps 5, 6 and 7 | Table: day, deliverable, owner. Footer with the cadence |
| 8 | Days 30 to 90: decide and start executing | Steps 4 and 7 | Same table. The longer horizon goes in the notes |
| 9-10 | Capabilities | Step 4 | One slide per pair of domains: capability (English Title Case), what it includes, who answers for the result |
| 11 | The decision | Step 4 | The architecture decision in one sentence, situation → opportunity, what we gain and what we give up |
| 12 | If something gets complicated, we decide with data | Steps 6 and 7 | Traffic light: green, yellow, red, each with who acts and what happens; plan B as 4 numbered steps; cadence in the footer |
| 13 | Questions | — | One word |
| 14 | Resources | Steps 1 to 8 | The artifact and what it contains, the presenter's contact |

Adapt the number of slides to the case (merge or split 9-10, drop 2 if the scenario is simple), but keep the order: **context → people → what we want → how we get there → what we decide → how we govern it**.

### 3. Speaker notes on every slide

Each slide's notes carry:
- **Message:** the one idea the room must keep.
- **Detail:** what is not on the slide (full names and titles, the reasoning, the tab of the artifact where it lives).
- **Objections and answers** where a question is likely (scope, the decision, cost, timing).
- **Time:** in minutes. The total must fit the slot (about 30 minutes, leaving time for questions).

### 4. Build the deck

Once the outline is approved, build it with the presentation tool available in the session (a slides artifact type, or a .pptx if the user asks for one). Use the user's brand colours and fonts if they give them; otherwise one dark colour for cover, facts and closing slides, a light background for content, and a single accent.

## Rules

- **Few words per slide.** If a slide needs more than about 40 words, move the rest to the notes or split it.
- **The title is the message**, not the topic: "Days 30 to 90: decide and start executing", not "Plan".
- **Facts, never bias.** No adjectives about people, no sides. Sensitive findings only in neutral wording; who hears them first goes in the notes.
- **No method jargon on the slides.** Words like "strategic bet" or "anchoring" stay in the artifact; on the slide say "priority" or explain it in plain words.
- **Firm, not consensual.** Governance is presented as decisions made with data and escalation by status, never as "deciding together" or "keeping everyone happy".
- **Never invent facts.** Every name, day and number comes from steps 1 to 8.
- **No abbreviations.** Every acronym appears with its full name: "CEO (Chief Executive Officer)". Capability names stay in English Title Case, as the method requires.
- **Deadlines in days**, as in the rest of the method.

## Example

A complete fictional outline is in `references/example-es.md`. Read it before writing.
