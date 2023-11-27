# Datos dados
tiempo_total_horas = 2
tiempo_total_minutos = 25
distancia_total_km = 42.195

# Convierte el tiempo total a minutos
tiempo_total_en_minutos = (tiempo_total_horas * 60) + tiempo_total_minutos

# Calcula el tiempo medio por kilómetro
tiempo_medio_por_kilometro = tiempo_total_en_minutos / distancia_total_km

# resultado
print("El tiempo medio por kilómetro es: {:.2f} minutos por kilómetro".format(tiempo_medio_por_kilometro))