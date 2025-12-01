# from .lectura_escritura_json import escribir_archivo_json, leer_archivo_json
from .elegir_palabra import eleccion_aleatoria
from .etapas_monigote import dibujar_monigote
from .puntaje import cargar_puntaje
from .Validate import validar_letra
from .mensajes import efecto_victoria, efecto_derrota

# Establecemos el nombre del archivo
nombre_archivo_puntajes = "scores.json"

# Creamos una función para identificar en qué posición/es de la palabra se encuentra la letra que el jugador escribió
def posicion_letra(letra, palabra):
    posiciones = []
    # Recorremos la palabra
    for i in range (len(palabra)):
        if letra == palabra[i]:
            posiciones.append(i)
    # Retornamos una lista con el/los índice/s en que la/s letra/s fue/ron encontrada/s
    return posiciones

def jugar(idioma):
    # Asignamos variables necesarias
    intentos_max = 6
    intento_actual = 0
    palabra = eleccion_aleatoria(idioma)
    palabra_oculta = "_" * len(palabra)
    letras_usadas = []
    # letras_acertadas = []
    puntaje = 0
    
    #Inciamos el juego
    while intento_actual < intentos_max:
        # Inicializamos el monigote, mostramos los intentos restantes, una lista con las letras usadas y la palabra oculta con los renglones
        dibujar_monigote(intento_actual)
        print("Intentos restantes: ", intentos_max - intento_actual)
        print("Letras usadas:", end=' ')
        for i in range(len(letras_usadas)):
            print(letras_usadas[i], end='|')
        print("\n",palabra_oculta)
        letra = str(input("Ingrese una letra: ")).lower()
        #Validamos que no escriba nada, mas de una letra o algo que no sea una letra
        while len(letra) > 1 or letra == "" or (not letra.isalpha()):
            print("Seleccione UNA LETRA")
            letra = str(input("Ingrese una letra: ")).lower()
        
        #Validamos que ya haya usado la letra
        if letra in letras_usadas:
            print("YA HAS USADO ESA LETRA. INTENTA CON OTRA")
            continue
        else:
            # Sino la agregamos
            letras_usadas.append(letra)

        #Validamos y remplazamos si le atino a la letra
        if validar_letra(letra, palabra):
            print("¡Bien hecho! Adivinaste una letra.")
            puntaje += 1

            posiciones_encontradas = posicion_letra(letra, palabra) #Nos devuelve una lista con los indices
            palabra_oculta = list(palabra_oculta)   #Convertimos la palabra oculta a un lista para poder modificar por idice

            for posicion in posiciones_encontradas: #Por cada indice en la lista de indices encontrados
                palabra_oculta[posicion] = letra    #Reemplazamos por la letra
            palabra_oculta = "".join(palabra_oculta)    #Volvemos a unirlo todo en una str

        #Si no le pega
        else:
            intento_actual += 1
            print("Letra incorrecta papu")
        
        #Validamos si adivino la palabra
        if "_" not in palabra_oculta:
            print(efecto_victoria())
            nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
            # Validamos que el nombre solo incluya letras
            while  not nombre_ingresado.isalpha():
                print("INGRESE SOLO LETRAS!!!")
                nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
            print("Puntaje guardado.")
            break
        
    # Si no le quedan mas intentos
    if intento_actual == intentos_max:
        # Dibuja al monigote ahorcado, el efecto de dorrota y que palabra era
        dibujar_monigote(intento_actual)
        print(efecto_derrota())
        print("La palabra era:", palabra)
        nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
        while  not nombre_ingresado.isalpha():
            print("INGRESE SOLO LETRAS!!!")
            nombre_ingresado = input("Introduzca su nombre de jugador: ").lower()
        print("Puntaje guardado.")
    
    #Cargamos el puntaje en el archivo scores
    cargar_puntaje(nombre_ingresado, puntaje, nombre_archivo_puntajes)
