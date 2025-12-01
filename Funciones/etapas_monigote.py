def dibujar_monigote(intento_actual):
    etapa = [
        """
          -----
          |   |
              |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
          |   |
          |   |
              |
              |
        """,
        """
          -----
          |   |
          O   |
         /|   |
          |   |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
         /    |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
         / \  |
              |
        """
    ]
    # Dependiendo de qué intento esté el jugador, se imprimirá un monigote en específico
    print(etapa[intento_actual])