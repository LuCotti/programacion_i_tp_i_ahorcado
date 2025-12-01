from Funciones import *

archivo_puntajes =  "scores.json"

menu = '''
---- Menú de opciones ----

1. Jugar. 
2. Puntaje. 
3. Salir.

Ingrese la opcion deseada: '''



def game():
    print ("BIENVENIDO AL JUEGO DEL AHORCADO")
    while True:
        opcion = get_int(menu,"Error, opcion inexistente",1,3,50)


        match opcion:
            case 1:
                print("-" * 40)

                seleccion_idioma = input("Ingrese el lenguage que quiera [ES | EN]: ").upper()
                while seleccion_idioma != "ES" and seleccion_idioma != "EN":
                    print("OPCION INVALIDA!!!")
                    seleccion_idioma = input("Ingrese el luegage que quiera [ES | EN]: ").upper()

                jugar(seleccion_idioma)
                pass
            case 2:
                print("*" * 40)
                if mostrar_mejores_puntajes(archivo_puntajes):
                    pass
                else:
                    print("No hay puntajes registrados")
                print("*" * 40)
            case 3:

                print ("Saliendo del juego.....")
                break

game()