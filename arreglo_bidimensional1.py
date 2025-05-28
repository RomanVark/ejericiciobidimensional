# Definición de la matriz (lista bidimensional) con las ventas mensuales
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# Función para calcular la venta total por todas las tiendas
def venta_total_todas_tiendas(ventas):
    total = 0  # Acumulador para ventas totales
    for tienda in ventas:  # Itera por cada tienda (fila de la matriz)
        total += sum(tienda)  # Suma todas las ventas de cada tienda y acumula
    return total  # Retorna el total acumulado

# Función para calcular la venta total por tienda
def venta_total_por_tienda(ventas):
    totales = []  # Lista para almacenar los totales de cada tienda
    for tienda in ventas:  # Itera por cada tienda
        totales.append(sum(tienda))  # Suma ventas de cada tienda y agrega a la lista
    return totales  # Retorna la lista de totales por tienda

# Función para encontrar la tienda que más vendió
def tienda_que_mas_vendio(totales):
    indice_max = totales.index(max(totales))  # Encuentra índice del mayor valor
    return indice_max + 1  # Retorna el número de tienda (índice + 1)

# Función para encontrar la tienda que menos vendió
def tienda_que_menos_vendio(totales):
    indice_min = totales.index(min(totales))  # Encuentra índice del menor valor
    return indice_min + 1  # Retorna el número de tienda (índice + 1)

# Ejecución de funciones y presentación de resultados
total_general = venta_total_todas_tiendas(ventas)  # Total ventas todas las tiendas
print("Venta total por todas las tiendas:", total_general)

totales_tiendas = venta_total_por_tienda(ventas)  # Total ventas por tienda
for i, total in enumerate(totales_tiendas):  # Muestra ventas por tienda
    print(f"Venta total de ABSA {i+1}:", total)

# Muestra tienda con más ventas
tienda_max = tienda_que_mas_vendio(totales_tiendas)
print(f"La tienda que más vendió es ABSA {tienda_max}")

# Muestra tienda con menos ventas
tienda_min = tienda_que_menos_vendio(totales_tiendas)
print(f"La tienda que menos vendió es ABSA {tienda_min}")
