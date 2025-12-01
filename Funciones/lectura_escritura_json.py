import json

# Creamos una funcion que SOLO lea y retorne los valores de un archivo json cualquiera
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        datos_leidos = json.load(file)
    return datos_leidos

# Sobre un archivo json cualquiera escribimos unos datos en especifico
def escribir_archivo_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as file: 
        json.dump(datos, file, indent=4)