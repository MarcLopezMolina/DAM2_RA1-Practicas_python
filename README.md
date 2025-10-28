# Mini-CRM de Eventos

Aplicación de consola en Python para gestionar **clientes, eventos y ventas** mediante archivos CSV. Integra **POO**, manejo de **fechas (`datetime`)** y operaciones con colecciones, permitiendo generar métricas e informes.

---

## Funcionalidades principales

- **Cargar CSV**: clientes, eventos y ventas.  
- **Listar tablas**: mostrar datos de clientes, eventos o ventas.  
- **Alta de cliente**: registro con validación de email y fecha, guardado incremental.  
- **Filtrar ventas por rango de fechas**.  
- **Estadísticas**: ingresos totales, ingresos por evento, categorías, días hasta el próximo evento, resumen de precios.  
- **Exportar informe**: `informe_resumen.csv` con totales por evento.  

---

## Características

- Clases: `Cliente`, `Evento`, `Venta` con métodos útiles (`antiguedad_dias()`, `dias_hasta_evento()`).  
- Manejo de errores (`FileNotFoundError`) y validaciones básicas.  
- Colecciones: `dict`, `list`, `set`, `tuple`.  
- Menú interactivo en consola.  

---

## Flujo de uso

1. Ejecutar el script principal.  
2. Seleccionar opción del menú: cargar datos, listar, alta, filtrar, estadísticas, exportar o salir.  
3. Interactuar con los datos de manera segura y estructurada.  

---

## Tecnologías

- Python 3.x  
- CSV  
- Programación orientada a objetos (POO)  
- `datetime`  
- Colecciones (`dict`, `list`, `set`, `tuple`)  
