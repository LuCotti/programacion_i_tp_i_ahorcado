from .elegir_palabra import eleccion_aleatoria
from .etapas_monigote import dibujar_monigote
from .puntaje import cargar_puntaje, mostrar_mejores_puntajes
from .Validate import validar_letra
from .mensajes import efecto_victoria, efecto_derrota
import os

# Establecemos el nombre del archivo
nombre_archivo_puntajes = "scores.json"

# Creamos una función para identificar en qué posición/es de la palabra se encuentra la letra que el jugador escribió
def posicion_letra(letra: str, palabra: str) -> list[int]:
    posiciones = []
    # Recorremos la palabra
    for i in range(len(palabra)):
        if letra == palabra[i]:
            posiciones.append(i)
    # Retornamos una lista con los índices en los que la letra fue encontrada
    return posiciones

def jugar(idioma: str) -> None:
    # Asignamos variables necesarias
    intentos_max = 6
    intento_actual = 0
    palabra = eleccion_aleatoria(idioma)
    palabra_oculta = "_" * len(palabra)
    letras_usadas = []
    puntaje = 0
    
    # Inciamos el juego
    while intento_actual < intentos_max:
        # Inicializamos el monigote, mostramos los intentos restantes, una lista con las letras usadas y la palabra oculta con los renglones
        dibujar_monigote(intento_actual)
        print("Intentos restantes:", intentos_max - intento_actual)
        print("Letras usadas:", end=" ")
        for i in range(len(letras_usadas)):
            print(letras_usadas[i], end=" | ")
        print("\n", palabra_oculta)
        letra = input("Ingrese una letra: ").lower()
        
        # Validamos que no escriba nada, más de una letra o algo que no sea una letra
        while len(letra) > 1 or letra == "" or (not letra.isalpha()):
            print("Seleccione UNA LETRA")
            letra = input("Ingrese una letra: ").lower()
        
        # Validamos que ya haya usado la letra
        if letra in letras_usadas:
            os.system("clear")
            print("Ya has usado esa letra. Intenta con otra.")
            continue
        else:
            # Sino la agregamos
            letras_usadas.append(letra)

        # Validamos y reemplazamos si acertó
        if validar_letra(letra, palabra):
            os.system("clear")
            print("¡Bien hecho! Adivinaste una letra.")
            puntaje += 1

            posiciones_encontradas = posicion_letra(letra, palabra) # Nos devuelve una lista con los índices
            palabra_oculta = list(palabra_oculta) # Convertimos la palabra oculta a una lista para poder modificar por índice

            for posicion in posiciones_encontradas: # Por cada índice en la lista de índices encontrados
                palabra_oculta[posicion] = letra # Reemplazamos por la letra
            palabra_oculta = "".join(palabra_oculta) # Volvemos a unirlo todo en una cadena

        # Si no acierta
        else:
            intento_actual += 1
            os.system("clear")
            print("Letra incorrecta.")
        
        # Validamos si adivinó la palabra
        if "_" not in palabra_oculta:
            efecto_victoria(idioma)
            print("Puntaje final:", puntaje)
            nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
            # Validamos que el nombre solo incluya letras
            while not nombre_ingresado.isalpha():
                print("Ingrese solo letras.")
                nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
            break
    
    # Si no le quedan más intentos
    if intento_actual == intentos_max:
        # Dibuja al monigote ahorcado, el efecto de derrota y qué palabra era
        dibujar_monigote(intento_actual)
        efecto_derrota(idioma)
        print("La palabra era:", palabra)
        print("Puntaje final:", puntaje)
        nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
        while not nombre_ingresado.isalpha():
            print("Ingrese solo letras.")
            nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
    
    # Cargamos el puntaje en el archivo de puntajes
    cargar_puntaje(nombre_ingresado, puntaje, nombre_archivo_puntajes)
    print("¡Puntaje guardado exitosamente!")
    mostrar_mejores_puntajes(nombre_archivo_puntajes, idioma)