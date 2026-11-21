# Ejemplo (datos ficticios)

Mismo caso ficticio que los pasos 1 a 5: Transportes Cóndor compró EnvíoYa para lanzar un servicio de entrega en el mismo día, y el comité ejecutivo no logra acordar cómo integrar ambas operaciones.

---

## 6. Reunión y gobierno de la integración

### 6.1 Primera reunión del Comité de Integración

Se hace el **día 15**, después de todas las conversaciones uno a uno, y dura 90 minutos. El material previo se envía 2 días antes.

| Tiempo | Tema | Quién lo lleva | Resultado esperado |
|---|---|---|---|
| 5 minutos | Apertura y respaldo a la integración | CEO (INGRESA_NOMBRE) | Patrocinio visible |
| 10 minutos | Para qué integramos: objetivo general y objetivos con sus responsables | Gerente de Operaciones (INGRESA_NOMBRE) | Un propósito común |
| 15 minutos | Lo que escuchamos en las conversaciones uno a uno, sin atribuirlo a nadie | Arquitectura Empresarial (INGRESA_NOMBRE) | Que todos se sientan escuchados |
| 20 minutos | Gobierno propuesto: comité, Arquitectura Empresarial, frentes, cadencias, semáforo, reporte semanal y escalada | Arquitectura Empresarial | Entender cómo vamos a trabajar |
| 25 minutos | Primeras decisiones | Preside el Gerente de Operaciones | Decisiones registradas, cada una con dueño |
| 15 minutos | Compromisos con responsable y día, y cierre | Gerente de Operaciones | Que todos salgan con su próximo paso |

**Decisiones que se piden ese día:**
1. Aprobar el gobierno de la integración.
2. Confirmar el responsable de cada frente de trabajo.
3. Acordar que, desde hoy, ningún desarrollo nuevo avanza fuera del gobierno de arquitectura.
4. Confirmar las entregas del día 30.

**Reglas de la reunión:**
1. Cada decisión queda escrita, con responsable y día.
2. Los temas sensibles no se tratan en grupo.
3. Si no hay acuerdo, decide quien preside, o el tema sube por la escalada.
4. Quien no pueda asistir envía a alguien con poder de decisión.

### 6.2 Estructura de gobierno

| Instancia | Quién | Qué hace |
|---|---|---|
| Directorio | INGRESA_NOMBRE | Recibe un informe mensual. Es la última instancia de escalamiento |
| CEO | INGRESA_NOMBRE | Patrocina la integración. Recibe el reporte semanal e interviene solo en las situaciones que él definió |
| Comité de Integración | Lo preside el Gerente de Operaciones. Lo integran la CFO, el Gerente Comercial, el CTO y el Gerente Digital | Decide prioridades, presupuesto de los desarrollos y registros de decisión de arquitectura. Resuelve los temas en rojo |
| Arquitectura Empresarial (Enterprise Architecture) | INGRESA_NOMBRE | Lleva el semáforo semanal, envía el reporte semanal de avance, mantiene el registro de riesgos, prepara el comité y apoya los frentes en amarillo |
| Frentes de trabajo | Un responsable por frente | Ejecutan y reportan su estado cada semana |

### 6.3 Frentes de trabajo

| Frente | Responde por el resultado | Día 14 | Día 30 |
|---|---|---|---|
| Caso de negocio | CFO (INGRESA_NOMBRE) | Supuestos clave revisados | Plan de acción; caso completo al día 60 |
| Operación | Gerente de Operaciones (INGRESA_NOMBRE) | Estado actual del área | Plan de acción |
| Comercial | Gerente Comercial (INGRESA_NOMBRE) | Envíos consolidados por servicio y planes que vienen | Plan de acción |
| Plataformas | Gerente Digital (INGRESA_NOMBRE), con los estándares técnicos del CTO | Estado de la plataforma | Plan de acción y avance del integrador |
| Continuidad y conocimiento | CTO (INGRESA_NOMBRE) | Sistemas críticos y quién los conoce | Plan de transferencia de conocimiento |

### 6.4 Cadencias

| Cadencia | Frecuencia | Quién | Para qué |
|---|---|---|---|
| Semáforo de cada frente | Semanal | Responsables de los frentes, con Arquitectura Empresarial | Estado en verde, amarillo o rojo, más los riesgos nuevos |
| Reporte semanal de avance | Semanal, al día siguiente del semáforo | Arquitectura Empresarial lo envía al CEO, al comité y a los responsables de los frentes | Una página: semáforo, decisiones, riesgos principales y próximos pasos |
| Comité de Integración | Cada 2 semanas durante los primeros 90 días; después, mensual | Comité completo | Decidir y destrabar |
| Reuniones de decisión | Días 30 y 60 | Comité completo | Validar opciones y aprobar el registro de decisión |
| Revisión de registros de decisión de arquitectura | Por escrito, en 5 días | Comité | Lo que cumple los principios se aprueba sin reunión |
| Informe al directorio | Mensual | Gerente de Operaciones, con apoyo de Arquitectura Empresarial | Avance, decisiones y riesgos principales |

El reporte semanal nunca incluye temas sensibles.

### 6.5 Semáforo y escalada

| Estado | Qué significa | Qué pasa |
|---|---|---|
| Verde | Avanza según lo acordado | El frente continúa |
| Amarillo | Riesgo de atraso que el frente puede resolver | Arquitectura Empresarial apoya al responsable |
| Rojo | El frente no lo puede resolver solo | Va al comité |
| Rojo sin resolver en el comité | Se necesita una decisión de más arriba | Va al CEO, en las situaciones que él definió, y al final al directorio |

La escalada se activa por el estado del frente, nunca por la persona.

### 6.6 Registro de riesgos, supuestos, problemas y dependencias

| Tipo | Entrada | Responsable |
|---|---|---|
| Riesgo | Pérdida de conocimiento del sistema de despacho por jubilaciones | CTO |
| Riesgo | Desarrollos en paralelo fuera del gobierno de arquitectura | Gerente Digital |
| Supuesto | Los supuestos del caso de negocio se validan con datos de la operación combinada | CFO |
| Problema | El sistema de Cóndor no permite crear servicios nuevos | Gerente Comercial y CTO |
| Dependencia | Los servicios nuevos dependen del nuevo integrador | Gerente Digital |
