---
name: 4-ea-capabilities
description: Builds the full architecture proposal of an enterprise architecture case from business capabilities. Delivers, in one go, the capability map with one accountable owner per capability, the anchoring matrix against the case objectives, the maturity assessment with evidence, impact and opportunity prioritisation with five strategic bets, the capability-to-team design (Team Topologies), the architecture decision record with the build, buy, extend or retire tree, the trade-offs and a roadmap in days with anticipated objections. Use this whenever an architect, consultant or candidate needs a capability map, maturity assessment, prioritisation, integration or platform decision, ADR, target teams or roadmap for a case, merger, integration or transformation, even if they never say "capability". Never invents facts.
---

# EA capabilities

**Step 4 of the case method.** Previous: `3-ea-diagnosis-findings`. Next: `5-ea-stakeholder-conversations`. Use the objectives and owners from `1-ea-scope-and-objectives`, the people from `2-ea-stakeholder-map` and the findings from step 3 as evidence.

Help an enterprise architect turn a case into an architecture proposal that executives can approve: what the company must be able to do, how ready it is, where to bet, who owns what, which decision to take and in what order.

Every part feeds the next one. A decision that cannot name the capability it serves is not ready. A roadmap that does not come from the prioritisation is a wish list.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). **Capability names always go in English and Title Case**; the description goes in the user's language. Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_NAME` / `INGRESA_NOMBRE`.

## Always deliver the complete section

Draft all eight parts from the case and the user's notes in one answer, then take corrections. After every correction, if the user asks to see it, deliver **the whole section again**, never loose fragments: people get lost when they have to stitch pieces together.

## Flow

### 4.1 Capability map

| Domain | Capability | Description | Accountable owner |
|---|---|---|---|

- **What, not how.** A capability is something the business must be able to do, as a compound noun ("Offer and Revenue Management"). No verbs, no vendor, system, protocol or tool, no status words (legacy, new, v2, to-be). An API or an integrator is the *how*: it goes in the decision record. The need behind it is a capability ("Enterprise Integration Management").
- **One company.** In a merger or integration, the map describes the target company as one: "for the whole network", "for all customers", never "of both companies". The current split only shows up as evidence in the maturity assessment.
- **Merge the similar ones.** Fewer, sharper capabilities beat a long list. Join capabilities that one owner would run together (offer with pricing and inventory). Data is a maturity dimension of every capability, not a capability of its own; do not count it twice.
- **Domains do not need the same number of rows.** The test is completeness against the scope from step 1, not balance. Every capability must score above 0 for at least one objective; if not, it does not belong.
- **Scope lives in the description, not in the name.** A capability may exist company-wide; narrow it in the description ("for the integration projects") so the name survives when the initiative ends.
- **One accountable owner per capability**, written as the job title from the case plus the name in parentheses: "CFO (Ana Ruiz)". Shared ownership is a smell. The owner answers for the result; they do not have to execute.
- **The architect is never an owner.** Close the map with a note: *"Map maintained by Enterprise Architecture (<name>). Each owner validates their capability in the day-14 survey."*

### 4.2 Anchoring matrix

Score each capability 0–3 against each objective from step 1 (0 none, 3 primary driver) and add a total. When two capabilities are merged, each objective takes the higher of the two scores. The highest totals (usually 5–7) go to maturity; a capability with a lower total can enter for risk if it threatens continuity, and the text says so.

### 4.3 Maturity

Four dimensions, levels 1 to 5: People, Process, Data, Technology. Mark it **preliminary, validated with the day-14 survey**.

| Capability | People | Process | Data | Technology | Limiting dimension |
|---|---|---|---|---|---|

- The **limiting dimension** is the weakest maturity dimension of that capability. It is not an area of the company; name the column "Limiting dimension" so no executive reads it as blame on their team.
- Every limiting score gets one evidence sentence: "<capability>: level N in <dimension>, because <fact from the case>". Without the sentence the score is not defensible.
- Avoid the sea of 3s: in a real organisation some cells are 1 or 5.

### 4.4 Impact and opportunity

- **Impact** = the highest of revenue, cost, risk and customer (each 0–3) plus half the sum of the other three. Range 0–7.5.
- **Opportunity** = gap × feasibility × value of the improvement, divided by 4. Range 0–6.75. Gap = level 4 minus the weakest dimension.
- Quadrants: high impact and high opportunity = **strategic bet**; high impact, low opportunity = protect and maintain; low impact, high opportunity = ignore; low and low = leave alone.

Pick **five strategic bets**. A borderline one needs a one-line justification. Bets are capabilities, never products: a product decision (a new cabin, a new service) waits for the capability and the business case.

### 4.5 From capabilities to teams

| Team | Type | Capabilities | Accountable owner |
|---|---|---|---|

Team types (Team Topologies): stream-aligned (owns a value stream, the default), platform (serves other teams), enabling (temporary, 90 to 180 days, transfers knowledge and leaves), complicated-subsystem (deep specialty, one or two at most). Conway's law: the shape of the teams becomes the shape of the systems, so design the teams for the target architecture.

Under an internal review tag (see step 3), list the team-capability smells ("olores" in Spanish): no owner, many owners, owner without mandate. Each one with its fix. Names of people whose role is still to be confirmed go only here.

### 4.6 Architecture decision record

First the tree, explicitly, with every exit:

| Exit | Applied to the case | Result |
|---|---|---|

Build, buy, extend, retire. Extend and retire are the most forgotten and often the right answer. Retiring the old system gets its own record, after migrating, never before.

Then the record:
- **Header:** author (Enterprise Architecture, with the architect's name), approver (the committee), date in days, status (proposed / accepted / replaced), at least three principles it satisfies.
- **1. Anchored capability:** the primary capability with its anchoring score, the secondary ones, and the expected maturity movement ("Process from level 1 to 3 in 270 days").
- **2. Context:** two or three sentences: the problem, the constraint and why now.
- **3. Decision:** one sentence, "We will…", never "we will consider".
- **4. Consequences:** day 90, day 360 and day 1,080, plus the downside.
- **5. Rejected alternatives:** at least two, named specifically, with the reason.

### 4.7 Trade-offs

Two columns: what we gain, what we give up. Three rows are enough.

### 4.8 Roadmap

| Horizon | Days | Bets | Maturity movement |
|---|---|---|---|

Now (committed, days 0–90), Next (sized, days 90–270), Later (candidate, days 270–540). No Gantt bars, no dates more precise than days. Close with **two anticipated objections** and the answer to each.

## Rules

- **Never invent facts.** Scores are a preliminary reading of the case; say so and point to the validation step.
- **Deadlines in days**, never "short term" or "soon".
- **No abbreviations**, except job titles exactly as the case writes them (CEO, CFO, CTO).
- **Neutral wording.** Evidence describes processes and systems, not people's failures.
- If the user is presenting, suggest showing only four parts (map, prioritisation, decision record, roadmap) and keeping anchoring and maturity as an appendix.

## Example

A complete fictional example is in `references/example-es.md`. Read it before writing.
