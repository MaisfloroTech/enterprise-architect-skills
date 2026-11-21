# Ejemplo (datos ficticios)

**Caso:** Transportes Cóndor, una empresa de encomiendas tradicional, compró EnvíoYa, una startup de última milla con app propia, para lanzar un servicio de entrega en el mismo día. El comité ejecutivo no logra acordar cómo integrar ambas operaciones. El Gerente de Operaciones pidió apoyo a Arquitectura Empresarial.

**Hallazgos del relevamiento:** el sistema de despacho de Cóndor no permite crear servicios nuevos; el equipo que lo conoce está por jubilarse; el equipo digital de EnvíoYa ya empezó a construir una plataforma propia; el volumen de envíos estándar viene cayendo y aún no se ha informado a Comercial.

---

## 1. Alcance y objetivos

### Alcance

**Nombre:** Integración de la nueva operación de última milla: Transportes Cóndor y EnvíoYa

**Nivel:** estrategia de la empresa, acotada a la integración. El mapa baja a dominios y subdominios, y solo llega al nivel de capacidad en lo que se prioriza.

**Entra:**
- **Comercial:** tarifas, venta digital, atención de clientes empresa
- **Operaciones:** planificación de rutas y despacho (solo sus puntos de conexión con lo comercial)
- **Plataformas tecnológicas:**

| Plataforma | Qué es | Situación |
|---|---|---|
| Cóndor | Sistema de despacho construido dentro de la empresa | Estable, pero no permite crear servicios nuevos; el equipo que lo conoce está por jubilarse |
| EnvíoYa | App y sistemas de la startup | Por confirmar quién los opera hoy |
| Nuevo integrador | La plataforma que construye el equipo digital, reorientada como capa de integración | Avanza sin una decisión formal |

**Queda fuera:** flota y mantenimiento de vehículos, recursos humanos y compras, porque la integración no los cambia.

### Objetivo general

Integrar las operaciones de Cóndor y EnvíoYa para recuperar participación en el mercado de encomiendas, sin afectar la continuidad del servicio actual.

### Objetivos

| # | Objetivo | Responde por el resultado | Plazo |
|---|---|---|---|
| 1 | Actualizar el caso de negocio de la adquisición: revisión de supuestos clave al día 14 y caso completo al día 60 | CFO (INGRESA_NOMBRE) | Día 0 a 60 |
| 2 | Asegurar la continuidad operativa y del conocimiento de los sistemas en producción de ambas compañías | CTO (INGRESA_NOMBRE) | Día 0 a 90 |
| 3 | Integrar sin interrupciones del servicio de despacho | Gerente de Operaciones (INGRESA_NOMBRE) | Desde el día 0 y durante toda la integración |
| 4 | Conectar las plataformas de Cóndor y EnvíoYa a través de un nuevo integrador | Gerente Digital (INGRESA_NOMBRE), con los estándares técnicos del CTO | Día 0 a 270 |
| 5 | Habilitar las capacidades comerciales para lanzar nuevos servicios: diseño comercial desde el día 0 y soporte tecnológico desde el día 90 | Gerente Comercial (INGRESA_NOMBRE) | Día 0 a 270 |
| 6 | Detener la caída de envíos estándar | Gerente Comercial (INGRESA_NOMBRE) | Día 0 a 540 |

### Compromiso de los primeros 90 días

Planear y ejecutar la estrategia de integración entre Cóndor y EnvíoYa, junto con Operaciones, Comercial, Finanzas, Tecnología y el equipo Digital, logrando la aprobación del comité ejecutivo en 60 días y el inicio del nuevo integrador al día 90, para habilitar nuevos servicios sobre un caso de negocio actualizado y sin afectar la operación.

| Día | Entregable |
|---|---|
| **14** | Supuestos clave del caso de negocio revisados por Finanzas; decisión preliminar sobre el servicio en el mismo día |
| **30** | Mapa de capacidades, evaluación de madurez y opciones de integración validados por las áreas; plan de transferencia de conocimiento con un líder de integración como puente entre ambos equipos |
| **60** | Estrategia de integración aprobada en un registro de decisión de arquitectura; caso de negocio completo actualizado; desarrollos nuevos priorizados según ese caso |
| **90** | Hoja de ruta aprobada con un dueño por capacidad; diseño del nuevo integrador aprobado; sistemas críticos documentados |

### Preguntas abiertas

| # | Pregunta | A quién | Por qué importa |
|---|---|---|---|
| 1 | ¿Quién opera hoy los sistemas de EnvíoYa? | Gerente Digital | Define quién responde por su continuidad (objetivo 2) |
