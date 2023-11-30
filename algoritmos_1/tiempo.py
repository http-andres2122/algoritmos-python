# obtenemos timepo usuario
def obtener_tiempo_usuario():
    while True:
        try:
            # registro inputs
            hora = int(input("Ingrese la hora (0-23): "))
            minutos = int(input("Ingrese los minutos (0-59): "))
            segundos = int(input("Ingrese los segundos (0-59): "))
            if 0 <= hora <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
                return hora, minutos, segundos
            else:
                print("Error: Ingrese valores dentro de los rangos permitidos.")
        except ValueError:
            print("Error: Ingrese valores numéricos.")

# calcular tiempo
def calcular_siguiente_segundo(hora, minutos, segundos):
    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        hora += 1

    if hora == 24:
        hora = 0

    return hora, minutos, segundos

# Mostrar tiempo
def mostrar_tiempo(hora, minutos, segundos):
    print(f"La hora en el siguiente segundo es: {hora:02d}:{minutos:02d}:{segundos:02d}")

# main
def main():
    hora, minutos, segundos = obtener_tiempo_usuario()
    nueva_hora, nuevos_minutos, nuevos_segundos = calcular_siguiente_segundo(hora, minutos, segundos)
    mostrar_tiempo(nueva_hora, nuevos_minutos, nuevos_segundos)

if __name__ == "__main__":
    main()
