import csv

# ---------------------------------------------------------------------------
# Clase RegistroHorario: representa un turno de trabajo de un empleado
# ---------------------------------------------------------------------------

class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro."""
        return self.salida - self.entrada


# ---------------------------------------------------------------------------
# Clase Empleado: almacena todos los registros de un trabajador
# ---------------------------------------------------------------------------

class Empleado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.registros = []  # Lista de objetos RegistroHorario

    def agregar_registro(self, registro: RegistroHorario):
        """Agrega un nuevo registro al empleado."""
        self.registros.append(registro)

    def horas_totales(self) -> int:
        """Devuelve el total de horas trabajadas en la semana."""
        return sum(r.duracion() for r in self.registros)

    def dias_trabajados(self) -> int:
        """Devuelve el número de días distintos trabajados."""
        return len({r.dia for r in self.registros})

    def fila_csv(self):
        """Devuelve una fila con los datos del resumen para escribir en CSV."""
        return [self.nombre, self.dias_trabajados(), self.horas_totales()]


# ---------------------------------------------------------------------------
# Clase GestorHorarios: gestiona la lectura, el procesamiento y los informes
# ---------------------------------------------------------------------------

class GestorHorarios:
    def __init__(self, fichero_entrada):
        self.fichero_entrada = fichero_entrada
        self.registros = []  # Lista de RegistroHorario
        self.empleados = {}  # nombre -> objeto Empleado

    # ----------------------- Lectura del CSV -------------------------------
    def leer_csv(self):
        """Lee el archivo de entrada y crea los objetos RegistroHorario y Empleado."""
        with open(self.fichero_entrada, newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=';')
            for fila in lector:
                if len(fila) == 4:
                    nombre, dia, entrada, salida = fila
                    registro = RegistroHorario(nombre, dia, int(entrada), int(salida))
                    self.registros.append(registro)

                    # Añadimos el registro al empleado correspondiente
                    if nombre not in self.empleados:
                        self.empleados[nombre] = Empleado(nombre)
                    self.empleados[nombre].agregar_registro(registro)

        print(f"Registros leídos: {len(self.registros)}")

    # ----------------------- Generar archivos -------------------------------

    def generar_resumen_horarios(self):
        """Genera un CSV con todos los registros detallados."""
        with open('resumen_horarios.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleado', 'Día', 'Entrada', 'Salida', 'Horas'])
            for r in self.registros:
                escritor.writerow([r.empleado, r.dia, r.entrada, r.salida, r.duracion()])
        print("-> Generado resumen_horarios.csv")

    def generar_madrugadores(self, hora_referencia=9):
        """Genera un CSV con empleados que comienzan antes de una hora dada."""
        madrugadores = {r.empleado for r in self.registros if r.entrada < hora_referencia}
        with open('madrugadores.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleado', 'Hora de entrada <', hora_referencia])
            for e in madrugadores:
                escritor.writerow([e])
        print(f"-> Generado madrugadores.csv (hora_referencia={hora_referencia})")

    def generar_en_dos_dias(self, dia1='Lunes', dia2='Viernes'):
        """Genera un CSV con empleados que trabajaron en ambos días."""
        empleados_por_dia = {}
        for r in self.registros:
            empleados_por_dia.setdefault(r.dia, set()).add(r.empleado)

        empleados_en_ambos = empleados_por_dia.get(dia1, set()) & empleados_por_dia.get(dia2, set())

        with open('en_dos_dias.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow([f'Empleados que trabajaron en {dia1} y {dia2}'])
            for e in empleados_en_ambos:
                escritor.writerow([e])
        print(f"-> Generado en_dos_dias.csv ({dia1} & {dia2})")

    def generar_exclusivos(self, dia1='Sábado', dia2='Domingo'):
        """Empleados que trabajaron el sábado pero no el domingo."""
        empleados_por_dia = {}
        for r in self.registros:
            empleados_por_dia.setdefault(r.dia, set()).add(r.empleado)

        exclusivos = empleados_por_dia.get(dia1, set()) - empleados_por_dia.get(dia2, set())

        with open('exclusivos.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow([f'Empleados que trabajaron solo el {dia1}'])
            for e in exclusivos:
                escritor.writerow([e])
        print(f"-> Generado exclusivos.csv ({dia1} - {dia2})")

    def generar_resumen_semanal(self):
        """Genera resumen_semanal.csv con días trabajados y horas totales."""
        with open('resumen_semanal.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleado', 'Días trabajados', 'Horas totales'])
            for emp in self.empleados.values():
                escritor.writerow(emp.fila_csv())
        print("-> Generado resumen_semanal.csv")

    def generar_filtrado_duracion(self, horas_min=6):
        """Empleados que han trabajado al menos X horas en todas sus jornadas."""
        empleados_validos = {
            nombre for nombre, emp in self.empleados.items()
            if all(r.duracion() >= horas_min for r in emp.registros)
        }

        with open('filtrado_duracion.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow([f'Empleados con ≥ {horas_min} h en todas sus jornadas'])
            for e in empleados_validos:
                escritor.writerow([e])
        print(f"-> Generado filtrado_duracion.csv (≥ {horas_min}h por jornada)")

    def generar_resumen_clases(self):
        """Genera resumen_clases.csv con los datos de los objetos Empleado."""
        with open('resumen_clases.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleado', 'Días trabajados', 'Horas totales'])
            for emp in self.empleados.values():
                escritor.writerow(emp.fila_csv())
        print("-> Generado resumen_clases.csv")


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------

def menu():
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Generar resumen de horarios")
    print("2. Generar madrugadores")
    print("3. Generar empleados que trabajan en Lunes y Viernes")
    print("4. Generar empleados exclusivos (Sábado - Domingo)")
    print("5. Generar resumen semanal")
    print("6. Filtrado por duración (≥ 6h)")
    print("7. Generar resumen usando clases (Empleado)")
    print("8. Salir")


def main():
    gestor = GestorHorarios('horarios.csv')
    gestor.leer_csv()

    while True:
        menu()
        opcion = input("Elige una opción (1-8): ")

        if opcion == '1':
            gestor.generar_resumen_horarios()
        elif opcion == '2':
            gestor.generar_madrugadores()
        elif opcion == '3':
            gestor.generar_en_dos_dias()
        elif opcion == '4':
            gestor.generar_exclusivos()
        elif opcion == '5':
            gestor.generar_resumen_semanal()
        elif opcion == '6':
            gestor.generar_filtrado_duracion()
        elif opcion == '7':
            gestor.generar_resumen_clases()
        elif opcion == '8':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# ---------------------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
