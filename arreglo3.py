# Matriz de ejemplo para linealizar
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para linealizar por columnas
def linealizar_por_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    arreglo_unidimensional = []
    for col in range(columnas):  # Se recorren primero columnas
        for fil in range(filas): # Luego filas
            arreglo_unidimensional.append(matriz[fil][col])
    return arreglo_unidimensional

# Ejecutar la función
resultado = linealizar_por_columnas(matriz)
print("Arreglo linealizado por columnas:", resultado)
