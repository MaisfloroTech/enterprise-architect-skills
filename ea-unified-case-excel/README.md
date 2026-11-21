[← All skills · Todos los skills](../README.md)

# 📒 ea-unified-case-excel

*Closed case sections → one Excel workbook, one tab per point.*

> ⚠️ **Esta skill solo unifica.** Cada punto del caso se construye y se cierra primero con su propia skill (de `1-ea-scope-and-objectives` en adelante). Si falta un punto, te dice qué skill invocar. · **This skill only unifies.** Build and close each point with its own skill first.

## 🇪🇸 Español

- Une los puntos cerrados del caso en un solo Excel, con una pestaña por punto y en orden.
- Copia la última versión aprobada de cada punto, palabra por palabra, sin reescribir nada.
- Pone fórmulas donde hay cálculos (anclaje, impacto, brecha y oportunidad), para que puedas mover un puntaje y ver cómo cambia la priorización.
- Mantiene las etiquetas de revisión interna y no agrega comentarios.
- En las siguientes ejecuciones, agrega solo las pestañas que faltan.

## 🇺🇸 English

Unifies the closed sections of a case into one Excel workbook, one tab per point, copied word for word from the last approved version. Calculations stay as formulas. Later runs add only the missing tabs. It never drafts content: each point comes from its own numbered skill.

## Script

`scripts/build_workbook.py` builds the workbook from a JSON spec, or adds only the missing tabs with `--append`.
