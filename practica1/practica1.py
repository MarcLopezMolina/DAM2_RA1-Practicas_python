# ---------------------------------------------------------------------------
# Variables iniciales y entrada de datos
# ---------------------------------------------------------------------------

# Solicita el número de empleados y valida que sea un entero positivo
while True:
    try:
        num_trabajadores = int(input("¿Cuántos empleados se van a introducir? "))
        if num_trabajadores > 0:
            break
        else:
            print("Debe introducir un número positivo de empleados.")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

print(f"Se van a introducir: {num_trabajadores} trabajadores")

# Solicita la hora de referencia y valida que esté entre 0 y 23
while True:
    try:
        hora_referencia = int(input("¿Cuál es la hora de referencia (0-23)? "))
        if 0 <= hora_referencia <= 23:
            break
        else:
            print("La hora de referencia debe estar entre 0 y 23.")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

print(f"La hora de referencia es: {hora_referencia}:00 horas")

# ---------------------------------------------------------------------------
# Inicialización de contadores y variables auxiliares
# ---------------------------------------------------------------------------

# Contador de empleados que llegan antes o a la hora de referencia
contador_entrada_temprana = 0

# Variable para almacenar la hora de salida más temprana (inicializada a 24)
salida_primera = 24

# Variable para almacenar el nombre del empleado que sale primero
empleado_salida_primera = ""

# ---------------------------------------------------------------------------
# Iteración para ingresar datos de cada empleado (usando bucle while)
# ---------------------------------------------------------------------------

contador = 0
while contador < num_trabajadores:
    print(f"\nIntroduce la información del empleado {contador + 1}:")
    nombre_empleado = input("Nombre del empleado: ")

    # Bucle para validar las horas de entrada y salida
    while True:
        try:
            hora_entrada = int(input("Hora de entrada (0-23): "))
            hora_salida = int(input("Hora de salida (0-23): "))
            # Validación de rango y orden
            if 0 <= hora_entrada <= 23 and 0 <= hora_salida <= 23 and hora_salida > hora_entrada:
                break
            else:
                print("Hora incorrecta. La hora de salida debe ser mayor que la de entrada y ambas entre 0 y 23.")
        except ValueError:
            print("Entrada no válida. Debe ser un número entero.")

    # -----------------------------------------------------------------------
    # Procesamiento de información
    # -----------------------------------------------------------------------

    # Contamos si el empleado entró antes o justo a la hora de referencia
    if hora_entrada <= hora_referencia:
        contador_entrada_temprana += 1

    # Verificamos si este empleado tiene la salida más temprana
    if hora_salida < salida_primera:
        salida_primera = hora_salida
        empleado_salida_primera = nombre_empleado

    # Incrementamos el contador del bucle principal
    contador += 1

# ---------------------------------------------------------------------------
# Mostrar resultados finales
# ---------------------------------------------------------------------------

print("\nResultados:")
print(f"Número de empleados que entraron antes o a la hora de referencia: {contador_entrada_temprana}")

if empleado_salida_primera != "":
    print(f"Empleado con la salida más temprana: {empleado_salida_primera} a las {salida_primera}:00 horas")
else:
    print("No se registraron empleados con datos válidos.")
