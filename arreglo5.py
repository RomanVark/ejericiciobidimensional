# Datos de ventas (puedes personalizarlos o ingresar por teclado)
ventas = [
    [10, 20, 15, 30],  # Vendedor 1
    [25, 18, 20, 22],  # Vendedor 2
    [14, 28, 17, 19]   # Vendedor 3
]

# Zona con más ventas
ventas_por_zona = [sum(ventas[vendedor][zona] for vendedor in range(3)) for zona in range(4)]
zona_max = ventas_por_zona.index(max(ventas_por_zona)) + 1
print(f"La zona con más ventas es la zona {zona_max}.")

# Vendedor con menos ventas
ventas_por_vendedor = [sum(vendedor) for vendedor in ventas]
vendedor_min = ventas_por_vendedor.index(min(ventas_por_vendedor)) + 1
print(f"El vendedor que menos vendió es el vendedor {vendedor_min}.")

# Total de ventas
total_ventas = sum(sum(vendedor) for vendedor in ventas)
print(f"La cantidad total de computadores vendidos es: {total_ventas}.")
