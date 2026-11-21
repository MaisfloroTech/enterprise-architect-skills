---
name: 6-ea-governance
description: Designs the first committee meeting and the governance of an enterprise architecture case, merger, integration or transformation. Delivers the agenda with times, owners and expected results, the decisions requested and the meeting rules, the governance structure (board, CEO, committee, Enterprise Architecture, workstreams), the workstreams with their day-14 and day-30 deliverables, the cadence (weekly status, weekly progress report to every party, committee, decision meetings, written review of architecture decision records, monthly board report), a traffic-light escalation path driven by status and not by person, and a starting register of risks, assumptions, issues and dependencies. Use this whenever someone needs to plan a kickoff or steering committee, set up governance, an integration management office, workstreams, status reporting or escalation rules, even if they never say "governance". Never invents facts.
---

# EA governance

**Step 6 of the case method.** Previous: `5-ea-stakeholder-conversations`. Next: `7-ea-next-steps-and-plan-b`. Use the objectives from `1-ea-scope-and-objectives`, the owners from `4-ea-capabilities`, and what each person delivers by day 14 and the situations in which the CEO wants to be reached from step 5.

Help an enterprise architect turn agreements reached one by one into a group that decides: a first meeting with no surprises, and a governance that keeps working when the architect is not in the room.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_NAME` / `INGRESA_NOMBRE`.

## Always deliver the complete section

Draft all six parts in one answer, then take corrections. After every correction, if the user asks to see it, deliver **the whole section again**.

## Audience

Executives read this section, so it has **no internal review tag** and no sensitive finding. A sensitive topic shows up only as a neutral entry ("the business case assumptions are validated with combined data"), or not at all when it already lives in a workstream plan.

## Flow

### 6.1 First committee meeting

Held right after the one-to-ones (day 15 if they ran from day 0 to 14), 90 minutes, pre-read sent 2 days before.

| Time | Topic | Led by | Expected result |
|---|---|---|---|

A proven order: the CEO opens (sponsorship, 5 minutes) → the leader with the mandate states the purpose and the objectives with their owners → the architect shares **what was heard in the one-to-ones, without attributing anything to anyone** → the architect presents the governance → first decisions, chaired by the leader → commitments with owner and day, and close.

Then two short numbered lists:
- **Decisions requested that day:** approve the governance, confirm workstream owners, agree that nothing new is built outside architecture governance from today, confirm the day-30 deliverables.
- **Meeting rules:** every decision written down with owner and day; sensitive topics are not discussed in the group; with no agreement, the chair decides or it escalates; whoever cannot attend sends someone who can decide.

### 6.2 Governance structure

| Body | Who | What it does |
|---|---|---|

Board (monthly report, last escalation step) · CEO (sponsor, receives the weekly report, steps in only in the situations they defined) · Integration Committee (chaired by the leader with the mandate; decides priorities, development budget and architecture decision records; resolves reds) · **Enterprise Architecture** (runs the weekly status, sends the weekly progress report, keeps the register, prepares the committee, follows up commitments, supports ambers) · Workstreams (one owner each, report weekly).

Name the architecture function in full ("Arquitectura Empresarial (Enterprise Architecture)" the first time, then "Arquitectura Empresarial"). Never as an acronym.

### 6.3 Workstreams

| Workstream | Accountable owner | Day 14 | Day 30 |
|---|---|---|---|

One per objective area, with the same owners as step 4. Day 14 is the current state (from the one-to-ones); day 30 is the action plan.

### 6.4 Cadence

| Cadence | Frequency | Who | Purpose |
|---|---|---|---|

Include: weekly status per workstream · **weekly progress report**, one page, sent by Enterprise Architecture to the CEO, the committee and the workstream owners the day after the status (status per workstream, decisions taken, main risks, next steps) · committee every 2 weeks for the first 90 days, then monthly · decision meetings on the key days, with the leader's presence required · written review of architecture decision records in 5 days (decisions that meet the architecture principles are approved without a meeting) · monthly board report. Add one line: the weekly report never carries sensitive topics; it shows states and actions, not who a problem is attributed to.

### 6.5 Traffic light and escalation

| State | What it means | What happens |
|---|---|---|

Green continues · amber: Enterprise Architecture supports the owner · red goes to the committee · red unresolved goes to the CEO (in the situations they defined) and, as the last step, to the board. Close with: **escalation is triggered by the state of the workstream, never by the person.**

### 6.6 Register of risks, assumptions, issues and dependencies

| Type | Entry | Owner |
|---|---|---|

Start it with 5 to 8 entries taken from the findings and the decision record, in neutral words.

## Rules

- **Never invent facts.** Days and frequencies are proposals; owners come from earlier steps.
- **Deadlines in days.**
- **No abbreviations**, except job titles exactly as the case writes them (CEO, CFO, CTO). Write "register of risks, assumptions, issues and dependencies", not its acronym.
- **No blame, no exposure.**
- Apply the governance the same way to everyone: a red goes to the committee, it does not get "one more week".

## Example

A complete fictional example is in `references/example-es.md`. Read it before writing.
