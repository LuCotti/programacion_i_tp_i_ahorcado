# Juego del Ahorcado

Juego de consola desarrollado en Python que implementa el clásico Ahorcado, permitiendo adivinar palabras en español o inglés mediante una interfaz de texto.

## Descripción

El juego selecciona aleatoriamente una palabra desde un archivo JSON y desafía al jugador a adivinarla letra por letra antes de agotar los intentos disponibles.  
A medida que el jugador falla, el monigote del ahorcado se construye progresivamente en consola.

## Funcionalidades
- Selección de idioma (español o inglés)
- Selección aleatoria de palabras desde un archivo JSON
- Representación visual del monigote en consola mediante texto
- Sistema de intentos limitados (6 fallos)
- Visualización de letras utilizadas
- Sistema de puntaje:
  - Puntos por letras correctas
  - Puntos adicionales al descubrir la palabra
- Guardado de puntajes en archivo JSON
- Visualización de los cinco mejores puntajes
- Menú interactivo en consola:
  - Jugar
  - Mostrar mejores puntajes
  - Salir

## Tecnologías

- Python
- Archivos JSON para persistencia de datos

## Estructura de archivos

- `data.json`: contiene las palabras disponibles en español e inglés
- `scores.json`: almacena los puntajes de los jugadores (generado automáticamente al finalizar las partidas)

## Ejecución
1. Clonar el repositorio
2. Ejecutar el archivo principal del juego:
```bash
python ahorcado.py
```
3. Seguir las instrucciones del menú en consola