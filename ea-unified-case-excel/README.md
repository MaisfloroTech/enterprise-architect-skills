[← Todas las skills](../README.md)

# 📒 ea-unified-case-excel

*Puntos cerrados del caso → un solo Excel, una pestaña por punto.*

> ⚠️ **Esta skill solo unifica.** Cada punto del caso se construye y se cierra primero con su propia skill, de `1-ea-scope-and-objectives` a `8-ea-glossary`. Si falta un punto, te dice qué skill invocar.

- Une los puntos cerrados del caso en un solo Excel, con una pestaña por punto y en orden.
- Copia la última versión aprobada de cada punto, palabra por palabra, sin reescribir nada.
- Pone fórmulas donde hay cálculos (anclaje, impacto, brecha y oportunidad), para que puedas mover un puntaje y ver cómo cambia la priorización.
- Mantiene las etiquetas de revisión interna y no agrega comentarios.
- En las siguientes ejecuciones, agrega solo las pestañas que faltan.

**Script:** `scripts/build_workbook.py` arma el Excel a partir de un archivo JSON, o agrega solo las pestañas que faltan con `--append`.

---

## English

[← All skills](../README.md#english)

*Closed points of the case → one Excel workbook, one tab per point.*

> ⚠️ **This skill only unifies.** Each point of the case is built and closed first with its own skill, from `1-ea-scope-and-objectives` to `8-ea-glossary`. If a point is missing, it tells you which skill to run.

- Puts the closed points of the case together in one Excel workbook, one tab per point, in order.
- Copies the last approved version of each point word for word, without rewriting anything.
- Uses formulas where there are calculations (anchoring, impact, gap and opportunity), so you can move a score and see the prioritisation change.
- Keeps the internal review tags and adds no comments.
- On later runs, adds only the missing tabs.

**Script:** `scripts/build_workbook.py` builds the workbook from a JSON file, or adds only the missing tabs with `--append`.
