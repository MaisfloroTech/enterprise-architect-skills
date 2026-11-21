---
name: ea-unified-case-excel
description: Unifies the closed sections of an enterprise architecture case into one Excel workbook, one tab per section, and later adds only the tabs that are missing. It does not create or rewrite content; the sections come from the numbered case skills (1-ea-scope-and-objectives, 2-ea-stakeholder-map, 3-ea-diagnosis-findings, 4-ea-capabilities, 5-ea-stakeholder-conversations, 6-ea-governance and the ones that follow). Use this whenever someone wants to put the case together, consolidate, export or deliver the points of a case in a spreadsheet or Excel file, or add a new point to an existing case workbook.
---

# EA unified case Excel

> **This skill only unifies.** It does not solve any part of the case. Each section must be built and closed first with its own skill (`1-ea-scope-and-objectives`, `2-ea-stakeholder-map`, `3-ea-diagnosis-findings`, `4-ea-capabilities`, `5-ea-stakeholder-conversations`, `6-ea-governance`, and the next numbered steps). If a section is missing or not closed, say which skill to invoke and stop for that section; never draft it here.

## What it delivers

One `.xlsx` workbook with one tab per closed section, named with its number ("1 Alcance y objetivos", "2 Stakeholders"…), in order. Later runs add only the tabs that are missing and keep every existing tab as it is.

## Flow

1. **Collect the closed sections** from the conversation (or from files the user gives). Use the **last version the user approved** of each one, word for word. Do not shorten, reword or "improve" it.
2. **Apply only the corrections the user already made** that affect earlier sections (a job title that changed, an owner that moved). Tell the user in one line which ones were applied.
3. **Read the `xlsx` skill** before building, and follow its rules (Arial, zero formula errors, recalculation).
4. **Write a JSON spec** and run `scripts/build_workbook.py` (see its docstring for the format):
   - New workbook: `python scripts/build_workbook.py spec.json "<Case name>.xlsx"`
   - Existing workbook: `python scripts/build_workbook.py spec.json "<Case name>.xlsx" --append` adds only the tabs that are not there yet.
5. **Recalculate and check** with the `xlsx` skill's `recalc.py`, then look at the rendered pages before delivering.
6. **Deliver** where the user asks. Upload only when they say so.

## Content rules

- **Each section keeps its own structure:** titles, short paragraphs and tables, exactly as approved. One table per block, with a dark header row.
- **Internal review tags stay** as italic notes on the sections that carry them. Nothing else is added: no comments, no explanations of how the workbook was made, no references to tools or assistants.
- **Formulas where the section has calculations,** so the user can change a score and see the result move:
  - Anchoring total: `=SUM(B{row}:G{row})`.
  - Impact: `=MAX(B{row}:E{row})+0.5*(SUM(B{row}:E{row})-MAX(B{row}:E{row}))`.
  - Gap: `=4-MIN(<maturity row>)`, pointing to the row of the same capability in the maturity table.
  - Opportunity: `=gap*feasibility*value/4`.
  - Check after recalculation that every formula gives the number the approved section shows.
- **No abbreviations** beyond what the approved sections already use, and deadlines in days.
- **Long text columns** get wide columns or a merged cell, so rows stay readable.

## Updating a workbook in a cloud drive

Some drive connections can upload a new file but cannot replace the contents of an existing one. In that case, upload the updated workbook as a new file with the same name, then **ask the user** before moving the previous version to the trash, so only one version remains.
