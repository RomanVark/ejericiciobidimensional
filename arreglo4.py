# Ingresar dimensiones
n = int(input("Ingrese número de filas (menor que 10): "))
m = int(input("Ingrese número de columnas (menor que 10): "))

# Crear matriz vacía
matriz = []

# Ingreso de valores de la matriz
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Ingrese valor para posición [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

# Suma por fila
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i+1}: {suma_fila}")

# Promedio por columna
for j in range(m):
    suma_columna = sum(matriz[i][j] for i in range(n))
    promedio = suma_columna / n
    print(f"Promedio de la columna {j+1}: {promedio:.2f}")

# Valor mayor y su ubicación
max_valor = matriz[0][0]
posicion = (0, 0)

for i in range(n):
    for j in range(m):
        if matriz[i][j] > max_valor:
            max_valor = matriz[i][j]
            posicion = (i, j)

print(f"El valor mayor es {max_valor}, ubicado en la fila {posicion[0]+1}, columna {posicion[1]+1}.")
