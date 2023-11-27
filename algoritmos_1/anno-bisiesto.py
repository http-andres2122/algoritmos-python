def es_bisiesto(anno):
    # Validacion del input: asegurarse de que sea un número.
    # Usaremos isinstance() Function: para validar y el año y que si sea un entero,
    # nos retorna true de ser correcta la informacion.
    # Mas informacion: https://www.w3schools.com/python/ref_func_isinstance.asp
    if not isinstance(anno, int):
        print("Error: El año debe ser un número entero.")
        return False
    
    # validación adicional: asegurarse de que el año no esté vacio.
    if not anno:
        print("Error: El año no puede estar vacío.")
        return False

    # logica para determinar si el año es bisiesto
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        return True
    else:
        return False

# Ejemplo de uso
anno_input = input("Ingrese un año: ")

# Validar que la entrada sea un número
try:
    anno = int(anno_input)
    resultado = es_bisiesto(anno)
    if resultado:
        print(f"{anno} es un año bisiesto.")
    else:
        print(f"{anno} no es un año bisiesto.")
except ValueError:
    print("Error: Ingrese un número entero válido.")