def tabla_multiplicar_decreciente(numero):
    if 1 <= numero <= 10:
        print(f"Tabla de multiplicar decreciente del {numero}:")
        for i in range(10, 0, -1):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("Por favor, ingrese un número entre 1 y 10.")

# Solicitar al usuario que ingrese un número
try:
    numero = int(input("Ingrese un número entre 1 y 10: "))
    tabla_multiplicar_decreciente(numero)
except ValueError:
    print("Por favor, ingrese un número válido.")
