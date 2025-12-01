Objetivo:
Desarrollar el clásico juego del Ahorcado en una versión de consola en Python. Los
estudiantes deberán implementar todas las funcionalidades necesarias para que el juego
sea jugable en modo texto.

Detalles del Ejercicio:
El juego del Ahorcado consiste en adivinar una palabra letra por letra antes de que el
monigote del ahorcado se complete. Los datos de las palabras estarán almacenados en un
archivo JSON.

Datos iniciales en archivo JSON (data.json):
● ID
● Palabra en español
● Palabra en inglés

Requerimientos:
A. Cargar el archivo data.json.
● Cargar un archivo JSON con palabras en español e inglés.
● Permitir que el juego seleccione aleatoriamente una palabra para adivinar.

B. Selección de idioma.
● Agregar la opción para seleccionar el idioma de las palabras en español o en inglés
al inicio del juego.

C. Representación del Monigote en Consola.
● Representar el monigote en la consola con texto. La figura debe mostrarse
progresivamente a medida que el jugador falla intentos. El monigote se debe
construir de la siguiente manera:
○ Cabeza
○ Tórax
○ Brazo izquierdo
○ Brazo derecho
○ Pierna izquierda
○ Pierna derecha

D. Lógica del Juego.
● El jugador tendrá seis (6) intentos para adivinar la palabra.
● Por cada intento fallido, se añadirá una parte al monigote.
● Si el jugador adivina una letra correctamente, se descubrirá esa letra en la palabra
oculta.
● Mostrar las letras usadas y la palabra con las letras descubiertas después de cada
intento.

E. Sistema de Puntaje.
● Por cada letra correcta adivinada, el jugador recibirá un punto.
● Al descubrir la palabra, el jugador suma puntos en base a la cantidad de letras de la
palabra.

F. Guardado de Puntaje en Archivo JSON.
● Al finalizar el juego, pedir el nombre del jugador y almacenar el puntaje en un archivo
scores.json.
● Mostrar los cinco (5) mejores puntajes al final de cada partida.

G. Interfaz del Menú en Consola.
● Incluir un menú inicial en consola con las siguientes opciones:
1. Jugar
2. Puntajes
3. Salir

H. Mostrar los Mejores Puntajes
● La opción "Puntajes" del menú debe mostrar los cinco mejores puntajes junto con el
nombre del jugador, en orden descendente.

Opcional:

1. Efectos Visuales:
○ Añadir una animación de texto o símbolos para hacer el juego más visual y
entretenido.

2. Mensajes Personalizados:
○ Agregar mensajes personalizados cada vez que se adivine una letra o
cuando el jugador pierda.