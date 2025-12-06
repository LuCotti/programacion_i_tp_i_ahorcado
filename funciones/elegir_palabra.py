import random 
from .variables import nombre_archivo_datos
from .lectura_escritura_json import * 

# Utilizando un diccionario generamos los contenidos
datos = {
    "ahorcado": [
        {
            "id": 1,
            "ES": "elefante",
            "EN": "elephant"
        },
        {
            "id": 2,
            "ES": "departamento",
            "EN": "department"
        },
        {
            "id": 3,
            "ES": "medicina",
            "EN": "medicine"
        },
        {
            "id": 4,
            "ES": "ingenieria",
            "EN": "engineering"
        },
        {
            "id": 5,
            "ES": "computadora",
            "EN": "computer"
        },
        {
            "id": 6,
            "ES": "dispositivo",
            "EN": "device"
        },
        {
            "id": 7,
            "ES": "software",
            "EN": "software"
        },
        {
            "id": 8,
            "ES": "hardware",
            "EN": "hardware"
        },
        {
            "id": 9,
            "ES": "idioma",
            "EN": "language"
        },
        {
            "id": 10,
            "ES": "ciudadano",
            "EN": "citizen"
        }
    ]
}

#Punto A/B
def eleccion_aleatoria(idioma: str) -> str:
    # Cargamos el archivo con los datos
    escribir_archivo_json(datos, nombre_archivo_datos)
    # Guardamos en una variable todo el contenido
    informacion = leer_archivo_json(nombre_archivo_datos)

    # Utilizando el random selecciona una palabra dependiendo del idioma
    eleccion_aleatoria = random.choice(informacion["ahorcado"])
    return eleccion_aleatoria[idioma]