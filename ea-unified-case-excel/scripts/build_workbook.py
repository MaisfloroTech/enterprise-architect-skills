"""Build or extend the case workbook from a JSON spec.

Usage:
  python build_workbook.py spec.json output.xlsx            # new workbook
  python build_workbook.py spec.json output.xlsx --append   # keep existing tabs, add only missing ones

Spec:
{"sheets": [{"name": "1 Alcance y objetivos", "widths": [16, 60, 40, 34],
  "blocks": [
    {"type": "title", "text": "1. Alcance y objetivos"},
    {"type": "heading", "text": "Alcance"},
    {"type": "paragraph", "text": "..."},
    {"type": "note", "text": "(Revisión interna: ...)"},
    {"type": "table", "header": ["#", "Objetivo"], "rows": [[1, "..."]],
     "bold_first": false, "merge_last_to": null},
    {"type": "gap"}]}]}

Cells starting with "=" are written as formulas. Use {row} inside a formula to
refer to the current row and {first} for the first data row of the same table.
"""
import json, sys, os
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

FONT = "Arial"
HDR = PatternFill("solid", fgColor="1F3864")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def write_sheet(wb, spec):
    ws = wb.create_sheet(spec["name"][:31])
    ws.sheet_view.showGridLines = False
    widths = spec.get("widths", [30, 40, 40, 40, 40, 40, 40, 40])
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + i)].width = w
    span = max(len(widths), 2)
    r = 1
    for b in spec["blocks"]:
        t = b["type"]
        if t == "gap":
            r += 1
        elif t in ("title", "heading"):
            c = ws.cell(r, 1, b["text"])
            c.font = Font(name=FONT, size=14 if t == "title" else 11, bold=True, color="1F3864")
            r += 2 if t == "title" else 1
        elif t in ("paragraph", "note"):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=span)
            c = ws.cell(r, 1, b["text"])
            c.font = Font(name=FONT, size=10, italic=(t == "note"), bold=b.get("bold", False))
            c.alignment = Alignment(wrap_text=True, vertical="top")
            ws.row_dimensions[r].height = max(15, 15 * (len(b["text"]) // 150 + 1))
            r += 1
        elif t == "table":
            head, rows = b["header"], b["rows"]
            m = b.get("merge_last_to")
            for j, h in enumerate(head, 1):
                c = ws.cell(r, j, h)
                c.font = Font(name=FONT, size=10, bold=True, color="FFFFFF")
                c.fill = HDR; c.border = BOX
                c.alignment = Alignment(wrap_text=True, vertical="center")
            if m:
                ws.merge_cells(start_row=r, start_column=len(head), end_row=r, end_column=m)
            r += 1
            first = r
            for row in rows:
                for j, v in enumerate(row, 1):
                    if isinstance(v, str) and v.startswith("="):
                        v = v.replace("{row}", str(r)).replace("{first}", str(first))
                    c = ws.cell(r, j, v)
                    c.font = Font(name=FONT, size=10, bold=(b.get("bold_first") and j == 1))
                    c.alignment = Alignment(wrap_text=True, vertical="top")
                    c.border = BOX
                    if isinstance(v, str) and v.startswith("=") and "/" in v or (isinstance(v, str) and "0.5*" in v):
                        c.number_format = "0.0"
                if m:
                    ws.merge_cells(start_row=r, start_column=len(row), end_row=r, end_column=m)
                    ws.row_dimensions[r].height = max(15, 14 * (len(str(row[-1])) // 110 + 1))
                r += 1
            r += 1
    ws.page_setup.orientation = "landscape"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    append = "--append" in sys.argv
    if append and os.path.exists(out):
        wb = load_workbook(out)
        existing = set(wb.sheetnames)
    else:
        wb = Workbook(); wb.remove(wb.active); existing = set()
    added = []
    for s in spec["sheets"]:
        if s["name"][:31] in existing:
            continue
        write_sheet(wb, s); added.append(s["name"])
    wb._sheets.sort(key=lambda w: w.title)
    wb.save(out)
    print(json.dumps({"added": added, "kept": sorted(existing)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
