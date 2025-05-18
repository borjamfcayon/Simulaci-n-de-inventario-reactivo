### 1. Ventajas de GraphQL sobre REST en este contexto

GraphQL realiza consultas más específicas y eficientes, solicitando solo los datos necesarios y reduciendo el número de peticiones HTTP. Además, facilita la evolución de la API sin romper clientes y maneja consultas y mutaciones en un solo endpoint, simplificando el desarrollo.

---

### 2. Definición de tipos y resolvers en GraphQL

Los tipos describen la estructura de los datos (por ejemplo, ProductType con campos como id, nombre y stock). Los resolvers son funciones que obtienen o modifican los datos según la consulta o mutación solicitada, separando claramente la lógica de acceso y la definición de datos.

---

### 3. Importancia de que el backend actualice available

El backend debe controlar la actualización de la disponibilidad para garantizar la consistencia, seguridad y una única fuente de verdad, evitando que clientes manipulen datos y asegurando que todos accedan a un estado coherente del inventario.

---

### 4. Garantía de coherencia en actualización de stock y disponibilidad

La lógica se implementa de forma centralizada y atómica en la mutación del backend, que ajusta el stock, actualiza la disponibilidad según reglas claras y evita estados inválidos como stock negativo. Esto mantiene la integridad y consistencia del sistema.
