import random

# Generar valores aleatorios para los precios de las camisas en dólares
cantidad_camisas = int(input("Ingrese la cantidad de camisas: "))
precios_camisas = [random.uniform(10, 50) for _ in range(cantidad_camisas)]

# Mostrar los precios generados
print(f'Precios de las camisas en dólares: {precios_camisas}')

# Solicitar al usuario la tasa de cambio
tasa_cambio = float(input("Ingrese la tasa de cambio (USD a COP): "))

# Calcular el total de la venta en pesos colombianos
total_venta_dolares = sum(precios_camisas)
total_venta_pesos = total_venta_dolares * tasa_cambio

# Mostrar resultados
print(f'Total de la venta en dólares: ${total_venta_dolares:.2f}')
print(f'Total de la venta en pesos colombianos: ${total_venta_pesos:.2f}')