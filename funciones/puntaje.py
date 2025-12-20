from .lectura_escritura_json import *

# Definimos una función para ordenar la lista según el puntaje de mayor a menor.
def ordenar_lista(lista: list) -> list:
    for i in range(len(lista)):
        # Valores numéricos
        maximo = lista[i]["puntaje"]
        posicion_maximo = i
        
        # Diccionario completo
        dict_maximo = lista[i]
        
        # Método selection sort adaptado a este caso en especial
        for j in range(i + 1, len(lista)):
            if lista[j]["puntaje"] > maximo:
                maximo = lista[j]["puntaje"]
                posicion_maximo = j
                dict_maximo = lista[j]
        
        auxiliar = lista[i]
        lista[i] = dict_maximo
        lista[posicion_maximo] = auxiliar
        
    return lista

# Definimos una función para imprimir los 5 mejores puntajes de la lista.
def mostrar_mejores_puntajes(nombre_archivo: str, idioma: str) -> bool:
    try:
        # Nos devuelve los datos en forma de lista
        lista = leer_archivo_json(nombre_archivo)

        # Establecemos el diccionario que queremos recorrer (jugaodres)
        contenido = lista["jugador"]

        if idioma == "ES":
            print("*" * 11, "MEJORES PUNTAJES", "*" * 11)
        elif idioma == "EN":
            print("*" * 13, "BEST  SCORES", "*" * 13)
        # Recorremos el diccionario asignando y mostrando por consola los datos de los jugadores
        for i in range(len(contenido)):
            if i <= 4:
                nombre = contenido[i]["nombre"]
                puntaje = contenido[i]["puntaje"]
            
                print(f"{i + 1}. {nombre} - {puntaje} puntos.")
        print("*" * 40)
        return True

    # Si el archivo está vacío, inicializamos la estructura básica para guardar los puntajes
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return False

# Definimos una función para cargar el puntaje en el archivo JSON
def cargar_puntaje(nombre_usuario: str, puntaje: int, nombre_archivo: str) -> None:
    # Intentamos leer el contenido del archivo
    try:
        puntajes = leer_archivo_json(nombre_archivo)

    # Si el archivo está vacío, inicializamos la estructura basica para guardar los puntajes
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        inicializar_puntajes(nombre_archivo)

    # Cargamos una nueva partida de jugador
    nuevo_puntaje = {
        "nombre": nombre_usuario,
        "puntaje": puntaje
    }
    puntajes = leer_archivo_json(nombre_archivo)

    # Añadimos el puntaje nuevo a la lista
    puntajes["jugador"].append(nuevo_puntaje)

    # Ordenamos la lista.
    puntajes["jugador"] = ordenar_lista(puntajes["jugador"])

    # Sobrescribimos el archivo JSON
    escribir_archivo_json(puntajes, nombre_archivo)

# Función auxiliar para inicializar el archivo JSON de puntajes con diccionario
def inicializar_puntajes(nombre_archivo: str) -> None:
    lista_vacia = {
        "jugador": []
    }
    escribir_archivo_json(lista_vacia, nombre_archivo)