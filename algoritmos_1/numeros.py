# usando random de python
import random
# Inicializar una lista para almacenar los números
numeros = []

# Generando numeros aleatoriamente 
for i in range(20):
 nrandom = int(random.uniform(0,100))
 numeros.append(nrandom)
# Mostrando lista generada
print(f'la lista de numeros generada es {numeros}')

#Mostrar los números menores o iguales a 25
print("Números menores o iguales a 25:")
for numero in numeros:
     if numero <= 25:
         print(numero)
