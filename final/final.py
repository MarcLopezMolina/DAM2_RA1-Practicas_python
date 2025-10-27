import csv
from datetime import datetime, date
import os
import re

# ------------------ CLASES ------------------

class Cliente:
    def __init__(self, cliente_id, nombre, email, fecha_registro):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.email = email
        self.fecha_registro = datetime.strptime(fecha_registro, "%Y-%m-%d").date()

    def antiguedad_dias(self):
        return (date.today() - self.fecha_registro).days

    def __str__(self):
        return f"{self.cliente_id}: {self.nombre} ({self.email}) - Registrado {self.fecha_registro}"

class Evento:
    def __init__(self, evento_id, nombre, fecha, categoria, precio):
        self.evento_id = evento_id
        self.nombre = nombre
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        self.categoria = categoria
        self.precio = float(precio)

    def dias_hasta_evento(self):
        return (self.fecha - date.today()).days

    def __str__(self):
        return f"{self.evento_id}: {self.nombre} [{self.categoria}] - {self.fecha} - ${self.precio:.2f}"

class Venta:
    def __init__(self, venta_id, cliente_id, evento_id, cantidad):
        self.venta_id = venta_id
        self.cliente_id = cliente_id
        self.evento_id = evento_id
        self.cantidad = int(cantidad)

    def __str__(self):
        return f"{self.venta_id}: Cliente {self.cliente_id}, Evento {self.evento_id}, Cantidad {self.cantidad}"

# ------------------ VARIABLES GLOBALES ------------------

clientes = {}
eventos = {}
ventas = {}

# ------------------ FUNCIONES DE CARGA ------------------

def cargar_datos():
    # Cargar clientes
    try:
        with open("data/clientes.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                clientes[row['cliente_id']] = Cliente(row['cliente_id'], row['nombre'], row['email'], row['fecha_registro'])
        print("Clientes cargados.")
    except FileNotFoundError:
        print("Archivo clientes.csv no encontrado.")

    # Cargar eventos
    try:
        with open("data/eventos.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                eventos[row['evento_id']] = Evento(row['evento_id'], row['nombre'], row['fecha'], row['categoria'], row['precio'])
        print("Eventos cargados.")
    except FileNotFoundError:
        print("Archivo eventos.csv no encontrado.")

    # Cargar ventas
    try:
        with open("data/ventas.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ventas[row['venta_id']] = Venta(row['venta_id'], row['cliente_id'], row['evento_id'], row['cantidad'])
        print("Ventas cargadas.")
    except FileNotFoundError:
        print("Archivo ventas.csv no encontrado.")

# ------------------ FUNCIONES DE LISTADO ------------------

def listar(tabla):
    if tabla == "clientes":
        for c in clientes.values():
            print(c)
    elif tabla == "eventos":
        for e in eventos.values():
            print(e)
    elif tabla == "ventas":
        for v in ventas.values():
            print(v)
    else:
        print("Tabla no reconocida.")

# ------------------ FUNCIONES DE ALTA ------------------

def validar_email(email):
    # Validación mínima con regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def alta_cliente():
    cliente_id = str(max([int(k) for k in clientes.keys()] + [0]) + 1)
    nombre = input("Nombre: ")
    email = input("Email: ")
    if not validar_email(email):
        print("Email inválido.")
        return
    fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")
    try:
        datetime.strptime(fecha_registro, "%Y-%m-%d")
    except ValueError:
        print("Fecha inválida.")
        return

    cliente = Cliente(cliente_id, nombre, email, fecha_registro)
    clientes[cliente_id] = cliente

    # Guardar incrementalmente
    archivo = "data/clientes.csv"
    file_exists = os.path.isfile(archivo)
    with open(archivo, 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['cliente_id','nombre','email','fecha_registro'])
        writer.writerow([cliente_id, nombre, email, fecha_registro])
    print("Cliente agregado correctamente.")

# ------------------ FUNCIONES DE FILTRO ------------------

def filtrar_ventas_por_rango():
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    try:
        f_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        f_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    except ValueError:
        print("Fechas inválidas.")
        return

    print("Ventas en rango:")
    for v in ventas.values():
        evento = eventos.get(v.evento_id)
        if evento and f_inicio <= evento.fecha <= f_fin:
            print(v, "->", evento)

# ------------------ FUNCIONES DE ESTADÍSTICAS ------------------

def estadisticas():
    total_ingresos = sum(eventos[v.evento_id].precio * v.cantidad for v in ventas.values())
    ingresos_por_evento = {}
    categorias = set()
    precios_ventas = []

    dias_eventos = [e.dias_hasta_evento() for e in eventos.values() if e.dias_hasta_evento() >= 0]
    dias_hasta_proximo = min(dias_eventos) if dias_eventos else None

    for v in ventas.values():
        e = eventos.get(v.evento_id)
        if e:
            ingresos_por_evento[e.nombre] = ingresos_por_evento.get(e.nombre, 0) + e.precio * v.cantidad
            categorias.add(e.categoria)
            precios_ventas.append(e.precio)

    if precios_ventas:
        tupla_precios = (min(precios_ventas), max(precios_ventas), sum(precios_ventas)/len(precios_ventas))
    else:
        tupla_precios = (0,0,0)

    print("Ingresos totales:", total_ingresos)
    print("Ingresos por evento:", ingresos_por_evento)
    print("Categorías existentes:", categorias)
    print("Días hasta el evento más próximo:", dias_hasta_proximo)
    print("Resumen precios (min, max, media):", tupla_precios)

# ------------------ EXPORTAR INFORME ------------------

def exportar_informe():
    archivo = "data/informe_resumen.csv"
    totales = {}
    for v in ventas.values():
        e = eventos.get(v.evento_id)
        if e:
            totales[e.nombre] = totales.get(e.nombre, 0) + e.precio * v.cantidad

    with open(archivo, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['Evento','Total Ingresos'])
        for nombre, total in totales.items():
            writer.writerow([nombre, total])
    print(f"Informe exportado a {archivo}")

# ------------------ MENÚ ------------------

def menu():
    while True:
        print("\n--- MINI-CRM ---")
        print("1. Cargar CSV")
        print("2. Listar tablas")
        print("3. Alta de cliente")
        print("4. Filtrar ventas por rango de fechas")
        print("5. Estadísticas")
        print("6. Exportar informe")
        print("7. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            tabla = input("Qué tabla listar (clientes/eventos/ventas): ").lower()
            listar(tabla)
        elif opcion == "3":
            alta_cliente()
        elif opcion == "4":
            filtrar_ventas_por_rango()
        elif opcion == "5":
            estadisticas()
        elif opcion == "6":
            exportar_informe()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# ------------------ EJECUCIÓN ------------------

if __name__ == "__main__":
    menu()
