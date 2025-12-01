def validate_number(dato: int) -> bool:
    try:
        int(dato)
        return True
    except ValueError:
        return  False

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    
    # Primero validamos el tipo de dato.
    if validate_number(dato_ingresado):
        dato_convertido = int(dato_ingresado)
        
        # Luego validamos que se encuentre dentro del rango.
        if dato_convertido >= minimo and dato_convertido <= maximo:
            return dato_convertido
        else:
            print(mensaje_error)
            if reintentos > 0:
                return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
            else:
                return None
    else:
        print(mensaje_error)
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
        else:
            return None


def validar_letra (letra, palabra):
    for i in range (len(palabra)):
        if letra == palabra[i]:
            return True
    return False