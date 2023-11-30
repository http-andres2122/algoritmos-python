def calcular_producto_hasta_N(numero):
    # Inicializar el producto como 1
    producto = 1
    
    # Calcular el producto desde 1 hasta N
    for i in range(1, numero + 1):
        producto *= i
    
    return producto

# Solicitar al usuario que ingrese un número
try:
    numero_usuario = int(input("Ingrese un número para calcular el producto hasta ese número: "))
    if numero_usuario < 0:
        print("Por favor, ingrese un número no negativo.")
    else:
        resultado = calcular_producto_hasta_N(numero_usuario)
        print(f"El producto de 1 hasta {numero_usuario} es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
