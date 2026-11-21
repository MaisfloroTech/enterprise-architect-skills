# Ejemplo (datos ficticios)

Mismo caso ficticio que los pasos 1 a 3: Transportes Cóndor compró EnvíoYa para lanzar un servicio de entrega en el mismo día, y el comité ejecutivo no logra acordar cómo integrar ambas operaciones.

Objetivos del paso 1: (1) caso de negocio, (2) continuidad y conocimiento, (3) servicio sin interrupciones, (4) nuevo integrador, (5) capacidades comerciales, (6) envíos estándar.

---

## 4. Propuesta de arquitectura

### 4.1 Mapa de capacidades

| Dominio | Capacidad | Descripción | Responde por el resultado |
|---|---|---|---|
| **Commercial** | Service Offer and Pricing Management | Diseño de los servicios de envío, con sus tarifas, para toda la red | Gerente Comercial (INGRESA_NOMBRE) |
| | Sales Channel Management | Venta digital y a clientes empresa, con una sola vista de clientes y envíos | Gerente Comercial (INGRESA_NOMBRE) |
| | Customer Service Management | Una sola atención para todos los clientes | Gerente Comercial (INGRESA_NOMBRE) |
| **Operations** | Route Planning Management | Planificación de una sola red de rutas | Gerente de Operaciones (INGRESA_NOMBRE) |
| | Dispatch Management | Despacho de todos los envíos | Gerente de Operaciones (INGRESA_NOMBRE) |
| | Last-Mile Delivery Management | Entrega final al cliente en toda la red | Gerente de Operaciones (INGRESA_NOMBRE) |
| **Finance** | Revenue Accounting Management | Contabilidad de los ingresos de la compañía | CFO (INGRESA_NOMBRE) |
| | Business Case Management | Elaboración y actualización del caso de negocio de la integración | CFO (INGRESA_NOMBRE) |
| | Investment Portfolio Management | Asignación y seguimiento del presupuesto por proyecto de la integración | CFO (INGRESA_NOMBRE) |
| **Technology** | Enterprise Integration Management | Conexión entre las plataformas para que la compañía opere con información y procesos comunes | Gerente Digital (INGRESA_NOMBRE) |
| | Application Operations Management | Operación y soporte de los sistemas en producción | CTO (INGRESA_NOMBRE) |
| | Systems Knowledge Management | Conservación y transferencia del conocimiento de los sistemas en producción | CTO (INGRESA_NOMBRE) |

*Mapa mantenido por Arquitectura Empresarial (INGRESA_NOMBRE). Cada responsable valida su capacidad en el levantamiento del día 14.*

### 4.2 Matriz de anclaje (escala de 0 a 3)

| Capacidad | 1 | 2 | 3 | 4 | 5 | 6 | Total |
|---|---|---|---|---|---|---|---|
| Service Offer and Pricing Management | 2 | 1 | 1 | 2 | 3 | 3 | **12** |
| Enterprise Integration Management | 0 | 1 | 2 | 3 | 3 | 1 | **10** |
| Sales Channel Management | 1 | 0 | 0 | 2 | 3 | 3 | **9** |
| Investment Portfolio Management | 3 | 1 | 0 | 2 | 2 | 1 | **9** |
| Dispatch Management | 1 | 1 | 3 | 1 | 1 | 1 | **8** |
| Systems Knowledge Management | 0 | 3 | 2 | 2 | 0 | 0 | 7 |
| Application Operations Management | 0 | 3 | 3 | 1 | 0 | 0 | 7 |
| Revenue Accounting Management | 3 | 1 | 0 | 1 | 1 | 1 | 7 |
| Business Case Management | 3 | 0 | 0 | 1 | 1 | 1 | 6 |
| Customer Service Management | 0 | 0 | 0 | 1 | 2 | 2 | 5 |
| Route Planning Management | 0 | 1 | 3 | 1 | 0 | 0 | 5 |
| Last-Mile Delivery Management | 0 | 1 | 3 | 0 | 0 | 0 | 4 |

Pasan a madurez las 5 capacidades con mayor anclaje, más Systems Knowledge Management por el riesgo que tiene sobre la continuidad.

### 4.3 Madurez (preliminar, se valida con el levantamiento del día 14)

Escala del nivel 1 al 5. La dimensión limitante es la dimensión de madurez más débil de cada capacidad.

| Capacidad | Personas | Proceso | Datos | Tecnología | Dimensión limitante |
|---|---|---|---|---|---|
| Service Offer and Pricing Management | 3 | 2 | 2 | **1** | Tecnología |
| Enterprise Integration Management | 2 | **1** | 2 | 2 | Proceso |
| Sales Channel Management | 3 | 3 | **2** | 3 | Datos |
| Investment Portfolio Management | 3 | **2** | **2** | **2** | Proceso, Datos y Tecnología |
| Dispatch Management | 4 | **3** | **3** | **3** | Proceso, Datos y Tecnología |
| Systems Knowledge Management | **1** | **1** | **1** | 2 | Personas, Proceso y Datos |

- **Service Offer and Pricing Management**: nivel 1 en Tecnología, porque el sistema de despacho de Cóndor no permite crear servicios nuevos.
- **Enterprise Integration Management**: nivel 1 en Proceso, porque no existe una forma definida de integrar las plataformas.
- **Sales Channel Management**: nivel 2 en Datos, porque la información de envíos por servicio está separada por compañía.
- **Investment Portfolio Management**: nivel 2 en Proceso, porque no existe un proceso común para asignar presupuesto a los desarrollos de la integración.
- **Dispatch Management**: nivel 3 en Proceso, porque el despacho es estable pero todavía no considera una sola red.
- **Systems Knowledge Management**: nivel 1 en Personas, porque el equipo que conoce el sistema de despacho está por jubilarse y no hay sucesión definida.

### 4.4 Impacto y oportunidad

| Capacidad | Impacto | Oportunidad | Cuadrante |
|---|---|---|---|
| Service Offer and Pricing Management | 5,0 | 4,5 | **Apuesta estratégica** |
| Enterprise Integration Management | 5,0 | 4,5 | **Apuesta estratégica** |
| Sales Channel Management | 4,5 | 4,5 | **Apuesta estratégica** |
| Systems Knowledge Management | 4,0 | 4,5 | **Apuesta estratégica** (por riesgo) |
| Investment Portfolio Management | 4,5 | 3,0 | **Apuesta estratégica** en el borde: victoria rápida de gobierno |
| Dispatch Management | 4,0 | 0,5 | Proteger y mantener |

Se apuesta por capacidades, no por productos: el servicio en el mismo día se decide cuando Service Offer and Pricing Management y el caso de negocio actualizado lo permitan.

### 4.5 De capacidades a equipos

| Equipo | Tipo | Capacidades | Responde por el resultado |
|---|---|---|---|
| Oferta comercial | Stream-aligned | Service Offer and Pricing, Sales Channel, Customer Service | Gerente Comercial (INGRESA_NOMBRE) |
| Operación integrada | Stream-aligned | Route Planning, Dispatch, Last-Mile Delivery | Gerente de Operaciones (INGRESA_NOMBRE) |
| Finanzas de la integración | Stream-aligned | Revenue Accounting, Business Case, Investment Portfolio | CFO (INGRESA_NOMBRE) |
| Nuevo integrador | Platform | Enterprise Integration | Gerente Digital (INGRESA_NOMBRE) |
| Continuidad y conocimiento | Enabling, entre 90 y 180 días | Systems Knowledge | CTO (INGRESA_NOMBRE), con un líder de integración como puente |
| Sistemas centrales | Complicated-subsystem | Application Operations | CTO (INGRESA_NOMBRE), con apoyo externo para documentar |

*(Revisión interna: equipo de Arquitectura Empresarial)*
- **Olor "sin dueño":** nadie tiene asignado Systems Knowledge Management. Solución: queda asignada al CTO.
- **Olor "dueño sin mandato":** la plataforma del equipo digital avanza sin decisión formal. Solución: queda formalizada como equipo Platform, con un solo responsable, y su presupuesto pasa por Investment Portfolio Management.

### 4.6 Registro de decisión de arquitectura

| Salida | Aplicada al caso | Resultado |
|---|---|---|
| Construir | Una plataforma de integración nueva desde cero | Se descarta: plazo y riesgo mayores |
| Comprar | Una solución de integración de mercado | Alternativa seria; costo por dimensionar con el CTO |
| **Extender** | **La plataforma del equipo digital como capa de integración** | **Elegida** |
| Retirar | Los módulos comerciales del sistema de Cóndor | En un registro aparte, después de migrar |

**Registro 001: Capa de integración de la compañía**

- **Encabezado:** autora: Arquitectura Empresarial (INGRESA_NOMBRE) · aprueba: Comité de Integración · fecha: día 60 · estado: propuesto · principios: anclar cada decisión a una capacidad; preferir extender antes que reemplazar; integrar por contratos y no por acoplamiento; planear el retiro del legado.
- **1. Capacidad anclada:** Enterprise Integration Management (anclaje 10). Secundarias: Service Offer and Pricing Management y Sales Channel Management. Movimiento esperado: Proceso del nivel 1 al 3 en Enterprise Integration y Tecnología del nivel 1 al 3 en Service Offer and Pricing, en 270 días.
- **2. Contexto:** hoy las dos compañías operan en plataformas que no se comunican. El sistema de Cóndor no permite crear servicios nuevos y su equipo está por jubilarse. La compañía necesita competir ya, sin interrumpir el despacho.
- **3. Decisión:** extenderemos la plataforma del equipo digital como capa de integración de la compañía, conectada por contratos de servicio, para habilitar servicios nuevos sin modificar el sistema de despacho.
- **4. Consecuencias:** día 90: integrador diseñado y sistemas críticos documentados · día 360: primeras capacidades comerciales operando sobre la compañía integrada · día 1.080: módulos comerciales de Cóndor retirados · desventaja: dos plataformas conviven durante la transición.
- **5. Alternativas rechazadas:** todo al sistema de Cóndor, porque no permite servicios nuevos; todo a EnvíoYa, porque su escala está por validar; construir desde cero, por plazo y riesgo; comprar, que queda como alternativa si el integrador no cumple al día 90.

### 4.7 Trade-offs

| Ganamos | Cedemos |
|---|---|
| Continuidad del despacho | Dos plataformas conviviendo más tiempo |
| Avance comercial desde el día 90 | Costo doble temporal |
| Aprovechar la inversión del equipo digital | Complejidad de operar el integrador |

### 4.8 Hoja de ruta

| Horizonte | Días | Apuestas | Movimiento de madurez |
|---|---|---|---|
| **Ahora** (comprometido) | 0–90 | Systems Knowledge; Investment Portfolio con su proceso definido al día 60; diseño de Enterprise Integration | Personas del nivel 1 al 3 en Systems Knowledge |
| **Siguiente** (dimensionado) | 90–270 | Enterprise Integration conectando las plataformas; Service Offer and Pricing; Sales Channel | Proceso del nivel 1 al 3 en Enterprise Integration; Tecnología del nivel 1 al 3 en Service Offer and Pricing |
| **Después** (candidato) | 270–540 | Customer Service; retiro de los módulos comerciales de Cóndor; servicio en el mismo día según el caso de negocio | Proceso del nivel 2 al 4 en las capacidades comerciales |

**Objeciones anticipadas**
1. *"¿Por qué no lanzamos ya el servicio en el mismo día?"* Porque hoy el sistema no lo soporta y el caso de negocio se está actualizando. Primero habilitamos la capacidad.
2. *"¿Por qué mantener dos plataformas si cuesta el doble?"* Porque migrar todo de una vez pone en riesgo el despacho. El costo doble es temporal y tiene fecha de retiro.
