import math

def tiempo_para_doblar_capital(capital, tasa_interes_anual, frecuencia_composicion):
    # Convertir la tasa de interés a decimal
    r = tasa_interes_anual / 100.0
    
    # Mapear la frecuencia de composición a su equivalente anual
    frecuencia_mensual = {1: 1, 2: 2, 3: 4, 4: 12}
    n = frecuencia_mensual.get(frecuencia_composicion, 1)
    
    # Calcular el tiempo para duplicar el capital
    tiempo = (math.log(2) / (n * math.log(1 + r/n)))
    
    return tiempo

# Pedir al usuario que introduzca los datos
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
frecuencia_composicion = int(input("Ingrese la frecuencia de composición (1: anual, 2: semestral, 3: trimestral, 4: mensual): "))

# Calcular el tiempo para duplicar el capital
tiempo_duplicacion = tiempo_para_doblar_capital(capital_inicial, tasa_interes_anual, frecuencia_composicion)

# Mostrar el resultado
print(f"\nEl tiempo necesario para duplicar el capital es de aproximadamente {tiempo_duplicacion:.2f} años.")

