# ---------------------------------------------------------------------------
# Variables iniciales y entrada de datos
# ---------------------------------------------------------------------------

# Pregunta al usuario cuántos empleados se van a introducir y convierte a entero
num_trabajadores = int(input("¿Cuántos empleados se van a introducir? "))
print(f"Se van a introducir: {num_trabajadores} trabajadores")

# Pregunta al usuario la hora de referencia para contar entradas tempranas
hora_referencia = int(input("¿Cuál es la hora de referencia (0-23)? "))
print(f"La hora de referencia es: {hora_referencia}:00 horas")

# ---------------------------------------------------------------------------
# Inicialización de contadores y variables auxiliares
# ---------------------------------------------------------------------------

# Contador de empleados que llegan antes o a la hora de referencia
contador_entrada_temprana = 0

# Variable para almacenar la hora de salida más temprana
# Se inicializa en 24 para que cualquier hora real sea menor
salida_primera = 24

# Variable para almacenar el nombre del empleado que sale primero
empleado_salida_primera = ""

# ---------------------------------------------------------------------------
# Iteración para ingresar datos de cada empleado
# ---------------------------------------------------------------------------

for _ in range(num_trabajadores):  # Se repite tantas veces como empleados
    print("\nIntroduce la información del empleado:")
    
    # Se solicita el nombre del empleado
    nombre_empleado = input("Nombre del empleado: ")

    # Bucle para validar las horas de entrada y salida
    while True:
        hora_entrada = int(input("Hora de entrada (0-23): "))
        hora_salida = int(input("Hora de salida (0-23): "))
        # Comprobamos que las horas estén en rango y que la salida sea mayor que la entrada
        if 0 <= hora_entrada <= 23 and 0 <= hora_salida <= 23 and hora_salida > hora_entrada:
            break  # Datos correctos, salimos del bucle
        else:
            print("Hora incorrecta. La hora de salida debe ser mayor que la de entrada y entre 0 y 23.")

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

# ---------------------------------------------------------------------------
# Mostrar resultados finales
# ---------------------------------------------------------------------------

print("\nResultados:")
print(f"Número de empleados que entraron antes o a la hora de referencia: {contador_entrada_temprana}")
print(f"Empleado con la salida más temprana: {empleado_salida_primera} a las {salida_primera}:00 horas")
