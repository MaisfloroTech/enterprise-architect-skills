# Ejemplo (datos ficticios)

Mismo caso ficticio que `1-ea-scope-and-objectives` y `2-ea-stakeholder-map`: Transportes Cóndor compró EnvíoYa para lanzar un servicio de entrega en el mismo día, y el comité ejecutivo no logra acordar cómo integrar ambas operaciones.

---

## 3. Hallazgos negativos clave
*(Revisión interna: equipo de Arquitectura Empresarial)*

| # | Hallazgo | Riesgo | Oportunidad | Sensibilidad | Cómo se maneja | Si el riesgo se materializa |
|---|---|---|---|---|---|---|
| 1 | El equipo digital ya está construyendo una nueva plataforma, sin una decisión formal | Una arquitectura paralela que duplica esfuerzos y queda fuera de gobierno | Reorientarla como el nuevo integrador entre ambas plataformas | Media | En la 1:1 con el Gerente Digital: se le pide el estado actual de la plataforma; después se lleva al comité | Los desarrollos nuevos pasan a revisión del comité y el presupuesto se asigna a través del gobierno de arquitectura |
| 2 | Los datos que respaldaron el caso de negocio de la compra presentan inconsistencias, y no se sabe si la CFO lo sabe | Decisiones de inversión tomadas sobre supuestos poco confiables; riesgo de credibilidad ante el directorio | Que la CFO lidere la actualización del caso de negocio (supuestos clave al día 14 y caso completo al día 60) | **Alta** | Solo en una 1:1 privada con la CFO, antes que con nadie más. Nunca en una reunión grupal | Las inversiones nuevas esperan el caso actualizado; el comité avanza con los datos disponibles y se informa al directorio |
| 3 | Los envíos estándar vienen cayendo, y nadie se lo ha dicho al Gerente Comercial | Decisiones comerciales sin la información completa; que se entere en público | Un argumento para actuar desde el día 0 y para aprovechar la experiencia digital de EnvíoYa | **Alta** | En la 1:1 con el Gerente Comercial: se le pide el estado actual de los envíos por servicio y se contrasta con lo encontrado en el relevamiento | El comité explora otras alternativas comerciales, como potenciar la oferta digital de EnvíoYa |
| 4 | La mayor parte del equipo que conoce el sistema de despacho está por jubilarse | Pérdida del conocimiento y riesgo para la continuidad del servicio | Documentar el conocimiento y usarlo como base del nuevo integrador | Media | En la 1:1 con el CTO: se le pide el estado actual del conocimiento (qué está documentado y quién lo sabe) | Se suma apoyo externo para documentar el sistema, priorizando el conocimiento crítico |

**En el documento que ven los ejecutivos,** los hallazgos 2 y 3 no aparecen. Solo aparece la acción neutra: "actualizar el caso de negocio" y "revisar el estado de los envíos".
