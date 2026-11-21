---
name: 3-ea-diagnosis-findings
description: Turns what an enterprise architect discovered in a case into a table of key negative findings that is useful and safe. For each finding it states the risk, the hidden opportunity, how sensitive it is, how it is handled (and with whom, privately when needed) and what is done if the risk materialises. Marks the whole section as internal review and keeps sensitive findings out of documents executives read. Use this whenever an architect, consultant or candidate has discovery findings, bad news, hidden problems or uncomfortable truths in a case and needs to decide how to raise them, plan contingencies, or present a diagnosis without exposing anyone, even if they never say "findings". Never invents facts.
---

# EA diagnosis findings

**Step 3 of the case method.** Previous: `2-ea-stakeholder-map`. Use its stakeholders to decide who handles each finding.

Help an enterprise architect turn discovery findings into a plan: what each finding puts at risk, what opportunity it hides, who hears it first and how, and what happens if the risk becomes real.

Bad news handled badly ends careers and kills initiatives: a wrong figure exposed in a group meeting, a director who learns about a problem in front of their peers. Bad news hidden is worse. This step does neither.

## Language

Answer in the language the user writes in (Spanish in, Spanish out). Missing data goes in as UPPERCASE placeholders in the user's language: `ENTER_DATE` / `INGRESA_FECHA`.

## Two audiences

The section has two readers, and the skill must make that explicit:

- **Internal review:** the architecture team (in an interview, the interviewers playing that team). They see every finding.
- **Executives:** they never read sensitive findings in a document. They see only the neutral action ("update the business case", "review the sales status").

Mark the whole section with a tag in the user's language, for example *(Internal review: architecture team)* / *(Revisión interna: equipo de Arquitectura Empresarial)*. If the user is preparing an interview, offer the form *(Revisión interna: <name> y entrevistadores, simulando un equipo de Arquitectura Empresarial)*.

## Flow

Draft the whole table from the case and the user's notes, then take corrections.

### 1. List the findings

Only what the discovery revealed and changes the risk of any option: parallel initiatives without governance, wrong or inconsistent data, bad news nobody has delivered, knowledge about to leave, key people moving. Usually 4–7 findings. Facts only; if the source of a finding is not stated, do not attribute it to anyone ("found while talking to different areas").

### 2. Fill the table

| # | Finding | Risk | Opportunity | Sensitivity | How it is handled | If the risk materialises |
|---|---|---|---|---|---|---|

Column rules:
- **Finding:** the fact, in neutral words. "The data behind the business case shows inconsistencies", not "the CFO's numbers are wrong".
- **Risk:** what can go wrong for the business, not for a person's reputation alone.
- **Opportunity:** almost every finding hides one (a parallel platform can become the integration layer; a person leaving can become the bridge; a sales drop is an argument to act from day 0). Look for it every time.
- **Sensitivity:** high or medium. High means it can expose a person or damage trust if it reaches the wrong audience first.
- **How it is handled:** who hears it, where and in what order. High sensitivity is always a private one-to-one, with that person before anyone else, never in a group meeting. Prefer **asking for the current state** over delivering the bad news: when the person reviews their own figures, they reach the conclusion themselves. Bring your evidence to contrast it together, not to correct them.
- **If the risk materialises:** the contingency, tied to the **risk, not to the person**. Write it as a governance action ("new investment waits for the updated case and the committee decides with the available data"), never as a punishment ("if she does not comply…").

### 3. Write the executive line

Close with one line stating which findings do not appear in executive documents and which neutral actions replace them.

## Wording rules

- **No blame, no exposure, no personal traits.**
- **Soft form, real substance.** The contingency must still exist: soften the words, never the consequence.
- **No abbreviations**, except job titles exactly as the case writes them (CEO, CFO, CTO).
- **Facts, interpretations, assumptions** stay apart; an assumption never becomes a finding.

## Output format

```
## 3. Key negative findings
*(internal review tag)*

<table: # · finding · risk · opportunity · sensitivity · how it is handled · if the risk materialises>

<one line: what executives see instead of the sensitive findings>
```

## Example

A complete fictional example is in `references/example-es.md`. Read it before writing the table.
