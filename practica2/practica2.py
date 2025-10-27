# ---------------------------------------------------------------------------
# 1) Datos iniciales: horarios de empleados
# ---------------------------------------------------------------------------

# Diccionario que almacena los horarios de entrada y salida de cada empleado.
# La clave es el nombre del empleado y el valor es una tupla (hora_entrada, hora_salida).
horarios = {
    'María':  ('08', '16'),
    'Juan':   ('09', '17'),
    'Lucía':  ('07', '15'),
    'Diego':  ('10', '18'),
    # Ampliación: se agregan más empleados
    'Ana':    ('08', '14'),
    'Raúl':   ('12', '20'),
}

# ---------------------------------------------------------------------------
# 2) Funciones
# ---------------------------------------------------------------------------

def mostrar_registros():
    """
    Recorre el diccionario de horarios y muestra cada empleado con su horario.
    Se enumeran los registros empezando desde 1 para mejor presentación.
    """
    print("\n--- Registros de empleados ---")  # Título
    # enumerate permite obtener un contador automático y los elementos del diccionario
    for i, (nombre, (entrada, salida)) in enumerate(horarios.items(), start=1):
        print(f"{i}. {nombre}: entra a las {entrada} y sale a las {salida}")
    print()  # Línea en blanco para separar visualmente del siguiente contenido


def contar_entradas():
    """
    Pide al usuario una hora y cuenta cuántos empleados ya han llegado
    antes o en esa hora. La hora debe ser un número entero entre 0 y 23.
    """
    while True:  # Bucle hasta que se ingrese un valor válido
        entrada_usuario = input("Introduce una hora (0–23): ").strip()  # Se elimina espacio extra
        try:
            hora = int(entrada_usuario)  # Intentamos convertir a entero
            if 0 <= hora <= 23:  # Comprobamos que esté dentro del rango válido
                break  # Salimos del bucle si todo está correcto
            else:
                print("⚠️ La hora debe estar entre 0 y 23.\n")
        except ValueError:  # Captura el error si no se puede convertir a entero
            print("⚠️ Debes introducir un número entero.\n")

    contador = 0
    # Recorremos los horarios y contamos los empleados cuya hora de entrada <= hora indicada
    for nombre, (entrada, _) in horarios.items():
        if int(entrada) <= hora:
            contador += 1

    # Mostramos el resultado al usuario
    print(f"A las {hora:02d}:00 ya habían llegado {contador} empleado(s).\n")


def menu():
    """
    Menú principal que se repite hasta que el usuario decide salir.
    Permite elegir entre:
      1) Mostrar registros de empleados
      2) Contar cuántos empleados han llegado hasta una hora determinada
      3) Salir del programa
    """
    while True:  # Bucle infinito hasta que se seleccione "Salir"
        print("========== MENÚ ==========")
        print("1) Mostrar registros")
        print("2) Contar entradas")
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()  # Se elimina espacio extra

        if opcion == '1':
            mostrar_registros()  # Llama a la función para mostrar todos los registros
        elif opcion == '2':
            contar_entradas()  # Llama a la función para contar empleados por hora
        elif opcion == '3':
            print("¡Hasta luego!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Intenta de nuevo.\n")  # Manejo de errores de input


# ---------------------------------------------------------------------------
# 3) Punto de entrada
# ---------------------------------------------------------------------------

# Este bloque asegura que el menú solo se ejecute si el script se ejecuta directamente
# y no si se importa como módulo desde otro script.
if __name__ == '__main__':
    menu()
