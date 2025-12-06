import json

def leer_archivo_json(nombre_archivo: str) -> dict:
    with open(nombre_archivo, "r") as file:
        datos_leidos = json.load(file)
    return datos_leidos

def escribir_archivo_json(datos: dict, nombre_archivo: str) -> None:
    with open(nombre_archivo, "w") as file:
        json.dump(datos, file, indent=4)