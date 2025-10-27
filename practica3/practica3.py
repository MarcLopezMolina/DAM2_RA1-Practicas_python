import csv  # Módulo para manejar archivos CSV

# ---------------------------------------------------------------------------
# Clase para gestionar los horarios de empleados desde un CSV
# ---------------------------------------------------------------------------

class GestorHorarios:
    def __init__(self, fichero_entrada):
        """
        Inicializa el gestor con el nombre del archivo CSV de entrada.
        """
        self.fichero_entrada = fichero_entrada
        self.datos = []  # Lista que almacenará diccionarios con los registros de empleados

    def leer_csv(self):
        """
        Lee el archivo CSV de entrada y guarda los registros en memoria.
        Se espera un CSV con columnas: nombre;dia;entrada;salida
        """
        with open(self.fichero_entrada, newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=';')  # Separa por ';'
            for fila in lector:
                if len(fila) == 4:  # Aseguramos que haya 4 columnas
                    nombre, dia, entrada, salida = fila
                    # Convertimos entrada y salida a enteros y guardamos en un diccionario
                    self.datos.append({
                        'nombre': nombre,
                        'dia': dia,
                        'entrada': int(entrada),
                        'salida': int(salida)
                    })
        print(f"Registros leídos: {len(self.datos)}")  # Información de cuántos registros se leyeron

    def generar_resumen_horarios(self):
        """
        Genera un CSV con todos los registros y calcula las horas trabajadas.
        """
        with open('resumen_horarios.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            # Cabecera del CSV
            escritor.writerow(['Nombre', 'Día', 'Entrada', 'Salida', 'Horas'])
            # Escribimos cada registro con el cálculo de horas trabajadas
            for r in self.datos:
                horas = r['salida'] - r['entrada']
                escritor.writerow([r['nombre'], r['dia'], r['entrada'], r['salida'], horas])
        print("-> Generado resumen_horarios.csv")

    def generar_madrugadores(self, hora_referencia=9):
        """
        Genera un CSV con empleados que entran antes de la hora de referencia.
        """
        # Filtramos los empleados que entran antes de la hora de referencia
        madrugadores = [r for r in self.datos if r['entrada'] < hora_referencia]
        with open('madrugadores.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Nombre', 'Día', 'Entrada', 'Salida'])
            for r in madrugadores:
                escritor.writerow([r['nombre'], r['dia'], r['entrada'], r['salida']])
        print(f"-> Generado madrugadores.csv (hora_referencia={hora_referencia})")

    def generar_en_dos_dias(self, dia1='Lunes', dia2='Viernes'):
        """
        Genera un CSV con empleados que trabajan en ambos días especificados.
        """
        empleados_por_dia = {}  # Diccionario con sets de empleados por día
        for r in self.datos:
            empleados_por_dia.setdefault(r['dia'], set()).add(r['nombre'])

        # Intersección de empleados que trabajan en ambos días
        empleados_en_ambos = empleados_por_dia.get(dia1, set()) & empleados_por_dia.get(dia2, set())

        with open('en_dos_dias.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleados que trabajan en', dia1, 'y', dia2])
            for e in empleados_en_ambos:
                escritor.writerow([e])
        print(f"-> Generado en_dos_dias.csv ({dia1} & {dia2})")

    def generar_resumen_semanal(self):
        """
        Genera un CSV con el total de horas trabajadas por empleado en la semana.
        """
        resumen = {}  # Diccionario: clave=nombre, valor=horas totales
        for r in self.datos:
            nombre = r['nombre']
            horas = r['salida'] - r['entrada']
            resumen[nombre] = resumen.get(nombre, 0) + horas  # Sumamos horas por empleado

        with open('resumen_semanal.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Nombre', 'Total Horas'])
            for nombre, horas in resumen.items():
                escritor.writerow([nombre, horas])
        print("-> Generado resumen_semanal.csv")


# ---------------------------------------------------------------------------
# Funciones de menú y flujo principal
# ---------------------------------------------------------------------------

def menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Generar resumen de horarios (todos los registros)")
    print("2. Generar madrugadores (entrada antes de 9)")
    print("3. Generar empleados que trabajan en Lunes y Viernes")
    print("4. Generar resumen semanal de horas")
    print("5. Salir")


def main():
    """
    Función principal que crea el gestor y ejecuta el bucle del menú.
    """
    gestor = GestorHorarios('horarios.csv')  # Se indica el CSV de entrada
    gestor.leer_csv()  # Carga los registros en memoria

    while True:
        menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            gestor.generar_resumen_horarios()
        elif opcion == '2':
            gestor.generar_madrugadores()
        elif opcion == '3':
            gestor.generar_en_dos_dias()
        elif opcion == '4':
            gestor.generar_resumen_semanal()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# ---------------------------------------------------------------------------
# Punto de entrada del programa
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
