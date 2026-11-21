# Ejemplo (datos ficticios)

Mismo caso ficticio que `1-ea-scope-and-objectives`: Transportes Cóndor compró EnvíoYa para lanzar un servicio de entrega en el mismo día, y el comité ejecutivo no logra acordar cómo integrar ambas operaciones.

---

## 2. Stakeholders

**Lectura general:** hoy hay dos prioridades legítimas en tensión, la **velocidad comercial** y la **continuidad del servicio**. El Gerente de Operaciones, a quien el directorio encargó la integración, dejó de asistir a las reuniones, y el CEO delega en sus gerentes, así que nadie está arbitrando entre ambas. La integración se gobierna bajo la estructura de Cóndor, y EnvíoYa aporta su experiencia digital. En los primeros 14 días, cada área comparte su carga actual para decidir qué despriorizar y así liberar capacidad para la integración.

| Persona | Poder | Postura | Qué le importa | Fortaleza | Riesgo | Qué conversar en la 1:1 |
|---|---|---|---|---|---|---|
| **CEO** (INGRESA_NOMBRE) | Alto en lo formal; delega en sus gerentes | Delegó la integración | La continuidad de la empresa | Legitimidad para respaldar la decisión final | Sin su arbitraje, las diferencias entre gerentes no se resuelven | Pedir su respaldo formal a la decisión del comité y a los derechos de decisión |
| **Directorio** | Alto | Exigió la integración, con Operaciones a cargo | El retorno de la compra | Puede destrabar el punto muerto | Perder confianza si la integración no avanza | No hay 1:1: recibe el gobierno de la integración para aprobación y es la instancia final de escalamiento |
| **CFO** (INGRESA_NOMBRE) | Alto: controla la inversión | Impulsa avanzar rápido; autora del plan de entrega en el mismo día | Justificar la compra y ver retorno pronto | Hizo la evaluación de la compra | Que se tomen decisiones de inversión antes de actualizar el caso de negocio | Actualizar el caso de negocio: revisión de supuestos clave al día 14 y caso completo al día 60 |
| **Gerente de Operaciones** (INGRESA_NOMBRE) | Alto: mandato del directorio y respeto de los equipos | Dejó de asistir a las reuniones sobre la integración | Un servicio de despacho sin interrupciones | Credibilidad en toda la empresa | Sin su participación, la integración no tiene un dueño efectivo | Liderar la integración de ambas operaciones, como lo pidió el directorio; Tecnología ejecuta la parte tecnológica y le rinde cuentas. Todo cambio que toque el despacho le llega ordenado (qué cambia, qué riesgo tiene y cómo se revierte) para su decisión |
| **Gerente Comercial** (INGRESA_NOMBRE) | Alto: resultados reconocidos | Impulsa avanzar rápido; el sistema actual no le permite crear servicios nuevos | Los indicadores de venta | Visión comercial | Percibe a Tecnología como un freno | Compartir la evolución de los envíos estándar; iniciar el diseño comercial desde el día 0 y lanzar por etapas |
| **Gerente Digital** (INGRESA_NOMBRE, ex fundador de EnvíoYa) | Medio-alto: influencia y afinidad con la CFO y Comercial | Impulsa una plataforma nueva, que su equipo ya empezó | Construir rápido | Experiencia digital; atrae talento | Una plataforma que avanza en paralelo, sin gobierno | La integración se gobierna bajo la estructura de Cóndor, y EnvíoYa aporta su experiencia digital. Reorientar su plataforma como el nuevo integrador; confirmar quién opera hoy los sistemas de EnvíoYa |
| **CTO** (INGRESA_NOMBRE) | Medio: conoce el sistema, pero está bajo presión | Prefiere no asumir riesgos; pidió apoyo a Arquitectura Empresarial | La estabilidad del despacho | Desarrolló el sistema actual | Su equipo clave está por jubilarse | Liderar la continuidad operativa y del conocimiento; abrir el sistema a través del integrador |

### Levantamiento de cada área (días 0 a 14)

En las conversaciones con cada gerente (no con el CEO ni con el directorio) se recoge esta información en una plantilla de una página, que el gerente solo valida:

| # | Pregunta |
|---|---|
| 1 | ¿Qué está haciendo hoy tu área y qué compromisos tiene este trimestre? |
| 2 | ¿Qué métricas tienes que cumplir? |
| 3 | ¿Qué está tomando más tiempo de lo esperado y por qué? |
| 4 | ¿Qué trabajo repetitivo se podría automatizar? |
| 5 | ¿Qué procesos o iniciativas podrían pausarse o dejar de hacerse para darle espacio a la integración? |

Con las respuestas se arma una propuesta de qué despriorizar para liberar capacidad para la integración.

### Afinidades actuales

La CFO, el Gerente Comercial y el Gerente Digital coinciden en avanzar rápido. El Gerente de Operaciones y el CTO coinciden en proteger la continuidad del servicio.

### Preguntas abiertas para las 1:1

| # | Pregunta | A quién | Por qué importa |
|---|---|---|---|
| 1 | ¿Quién opera hoy los sistemas de EnvíoYa? | Gerente Digital | Define quién responde por su continuidad |
