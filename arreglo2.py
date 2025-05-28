# Se define una matriz vacía para almacenar nombres y calificaciones
estudiantes = []

# Ciclo para ingresar información de 5 estudiantes
for i in range(5):
    # Pedir al usuario el nombre del estudiante
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    
    # Lista temporal para almacenar las calificaciones del estudiante actual
    calificaciones = []
    
    # Ciclo para ingresar las 3 calificaciones del estudiante
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        calificaciones.append(calificacion)
    
    # Agrega al estudiante (nombre y sus calificaciones) a la matriz principal
    estudiantes.append([nombre, calificaciones])

# Mostrar promedios por cada estudiante
print("\nPromedios finales de los estudiantes:")
for estudiante in estudiantes:
    # Extraer nombre y calificaciones del estudiante
    nombre = estudiante[0]
    calificaciones = estudiante[1]
    
    # Calcular promedio usando sum y len
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Mostrar el nombre y el promedio final del estudiante
    print(f"{nombre}: {promedio:.2f}")
