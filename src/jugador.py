class Jugador:
    # Clase que representa a un jugador en el juego.

    def __init__(self, nombre, ficha):
        # Inicializa un nuevo jugador.
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return f"{self.nombre} ({self.ficha})"
