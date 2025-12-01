from .lectura_escritura_json import *

# Definimos una función para ordenar la lista según el puntaje de mayor a menor.
def ordenar_lista(lista: list) -> list:
    for i in range(len(lista)):
        # Valores numéricos
        maximo = lista[i]['puntaje']
        posicion_maximo = i
        
        # Diccionario completo
        dict_maximo = lista[i]
        
        # Metodo selection sort adaptado a este caso en especial
        for j in range(i + 1, len(lista)):
            if lista[j]['puntaje'] > maximo:
                maximo = lista[j]['puntaje']
                posicion_maximo = j
                dict_maximo = lista[j]
        
        auxiliar = lista[i]
        lista[i] = dict_maximo
        lista[posicion_maximo] = auxiliar
        
    return lista

# Definimos una función para imprimr los 5 mejores puntajes de la lista.
def mostrar_mejores_puntajes(nombre_archivo):
    try:
        # Nos devuelve en forma de lista los datos
        lista = leer_archivo_json(nombre_archivo)

        #Establecemos el diccionario que queremos recorrer (jugaodres)
        contenido = lista["jugador"]

        #Recorremos el diccionario asignando y mostrando por consola los datos de los jugadores
        for i in range(len(contenido)):
            if i <= 4:
                nombre = contenido[i]['nombre']
                puntaje = contenido[i]['puntaje']
            
            print(f'{i + 1}. {nombre} - {puntaje} puntos.')
        return True

    #Si el archivo esta vacio inicializamos la estructura basica para guardar los puntajes
    except json.decoder.JSONDecodeError:
        return False

# Definimos una función para cargar el puntaje en el archivo JSON.
def cargar_puntaje(nombre_usuario: str, puntaje: int, nombre_archivo: str) -> None:
    #Intentamos leer el contenido del archivo
    try:
        # Intentamos leer los datos del archivo JSON
        puntajes = leer_archivo_json(nombre_archivo)

    #Si el archivo esta vacio inicializamos la estructura basica para guardar los puntajes
    except json.decoder.JSONDecodeError:
        inicializar_puntajes(nombre_archivo)

    # cargamos una nueva partida de jugador
    nuevo_puntaje = {
        'nombre': nombre_usuario,
        'puntaje': puntaje
    }
    puntajes = leer_archivo_json(nombre_archivo)

    # Añadimos el puntaje nuevo a la lista
    puntajes['jugador'].append(nuevo_puntaje)

    # Ordenamos la lista.
    puntajes['jugador'] = ordenar_lista(puntajes['jugador'])

    # Sobrescribimos el archivo JSON
    escribir_archivo_json(puntajes, nombre_archivo)

    # Mostramos los 5 mejores puntajes de la lista.
    print("*" * 40)
    for i in range(len(puntajes["jugador"])):
        if i <= 4:
            nombre = puntajes["jugador"][i]['nombre']
            puntaje = puntajes["jugador"][i]['puntaje']

            print(f'{i + 1}. {nombre} - {puntaje} puntos.')
            print("-" * 40)
    print("*" * 40)


# Función auxiliar para incializar el archivo JSON de puntajes con diccionario.
def inicializar_puntajes(nombre_archivo):
    lista_vacia = {
        "jugador": [
        ]
    }
    escribir_archivo_json(lista_vacia, nombre_archivo)
