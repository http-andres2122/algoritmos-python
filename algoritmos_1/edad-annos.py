# Usaremos la libreria datetime para la fecha.
# mas informacion: https://docs.python.org/3/library/datetime.html
from datetime import datetime

def calcular_edad(fecha_nacimiento):
    try:
        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Convertir la fecha de nacimiento a objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

        # Calcular la diferencia entre las fechas
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        print(edad)
        return edad, fecha_actual
    except ValueError:
        print("Error: Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")
        return None, None

# Input fecha
fecha_nacimiento_input = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")

# Calcular la edad y obtener la fecha actual
edad, fecha_actual = calcular_edad(fecha_nacimiento_input)

# Mostrar el resultado si no hay errores
if edad is not None and fecha_actual is not None:
    print(f"Fecha actual: {fecha_actual.strftime('%Y-%m-%d')}")
    print(f"La edad actual es: {edad} años.")
