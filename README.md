🛠️ Mini-CRM de Eventos

Esta es una aplicación de consola en Python diseñada para gestionar clientes, eventos y ventas utilizando archivos CSV. El proyecto integra conceptos de programación orientada a objetos, manejo de fechas con datetime, y operaciones con colecciones (list, dict, set, tuple), permitiendo generar informes y métricas de manera sencilla.

🎯 Objetivos del proyecto

📂 Leer y escribir datos desde archivos CSV (clientes.csv, eventos.csv, ventas.csv).

🧑‍💼 Gestionar información de clientes, 🗓️ eventos y 💰 ventas.

🏷️ Implementar clases propias (Cliente, Evento, Venta) con métodos útiles:

Cliente.antiguedad_dias() → días desde el registro del cliente

Evento.dias_hasta_evento() → días restantes hasta el evento

📅 Trabajar con fechas para filtrar eventos o calcular antigüedad.

📊 Generar métricas y resúmenes que pueden exportarse a CSV (informe_resumen.csv).

⚙️ Funcionalidades principales

📥 Cargar CSV

Importa los archivos clientes.csv, eventos.csv y ventas.csv.

Manejo de errores si los archivos no existen (FileNotFoundError).

📋 Listar tablas

Muestra de forma legible los datos de clientes, eventos o ventas.

➕ Alta de cliente

Añadir un nuevo cliente solicitando nombre, email y fecha de registro.

Validación de email y fecha.

Guardado automático e incremental en clientes.csv.

📆 Filtrar ventas por rango de fechas

Permite consultar ventas entre dos fechas específicas de eventos.

Muestra los datos completos de la venta y del evento correspondiente.

📈 Estadísticas y métricas

💵 Ingresos totales de todas las ventas.

💰 Ingresos por evento.

🏷️ Categorías de eventos disponibles.

⏳ Días hasta el evento más próximo.

📊 Resumen de precios de eventos (mínimo, máximo y promedio).

📝 Exportar informe

Genera informe_resumen.csv con totales de ingresos por evento.

Permite análisis posterior o integración con otras herramientas.

🛡️ Validaciones y buenas prácticas

✅ Manejo de errores en lectura de archivos CSV.

✅ Validación mínima de emails.

✅ Evita colisiones de IDs generando automáticamente los IDs de nuevos clientes.

✅ Uso de datetime para garantizar la consistencia de fechas.

🚀 Tecnologías y conceptos utilizados

🐍 Python 3.x

🗃️ Archivos CSV para entrada y salida de datos

🧩 POO: clases, métodos y __str__/__repr__ para legibilidad

📅 datetime para cálculos de fechas y rangos

🏗️ Colecciones: dict, list, set, tuple

📊 Cálculo de métricas y generación de informes

🖼️ Flujo de uso

Ejecutar el script principal.

Elegir una opción del menú:

Cargar datos, listar, dar de alta clientes, filtrar ventas, estadísticas, exportar informe o salir.

Trabajar con los datos de manera interactiva desde consola.
