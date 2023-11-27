# Función para convertir grados Celsius a grados Fahrenheit
def celsius_a_fahrenheit(grados_celsius):
    grados_fahrenheit = (9/5) * grados_celsius + 32
    return grados_fahrenheit

# Solicitar al usuario que introduzca la temperatura en grados Celsius
temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convierte la temperatura a grados Fahrenheit utilizando la función
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Imprime el resultado
print(f"{temperatura_celsius} grados Celsius es igual a {temperatura_fahrenheit:.2f} grados Fahrenheit")