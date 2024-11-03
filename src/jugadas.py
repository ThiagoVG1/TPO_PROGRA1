import random
from src.tablero import FILAS, COLUMNAS

def es_jugada_ganadora(tablero, fila, columna, ficha):
    # Comprueba si colocar una ficha en una posición dada resulta en una victoria.

    # Comprobar victoria horizontal (--).
    for col in range(max(0, columna - 3), min(COLUMNAS - 3, columna) + 1):
        if all(tablero[fila][col + i] == ficha for i in range(4)):
            return True

    # Comprobar victoria vertical (|).
    for fil in range(max(0, fila - 3), min(FILAS - 3, fila) + 1):
        if all(tablero[fil + i][columna] == ficha for i in range(4)):
            return True

    # Comprobar victoria diagonal ascendente (\).
    for offset in range(-3, 1):
        if (
            0 <= fila + offset < FILAS - 3 and
            0 <= columna + offset < COLUMNAS - 3 and
            all(tablero[fila + offset + i][columna + offset + i] == ficha for i in range(4))
        ):
            return True

    # Comprobar victoria diagonal descendente (/).
    for offset in range(-3, 1):
        if (
            0 <= fila - offset < FILAS - 3 and
            0 <= columna + offset < COLUMNAS - 3 and
            all(tablero[fila - offset - i][columna + offset + i] == ficha for i in range(4))
        ):
            return True

    return False

def obtener_jugadas_validas(tablero):
    # Genera una lista de columnas donde es posible realizar una jugada.
    return [col for col in range(COLUMNAS) if tablero[0][col] == ' ']

def siguiente_fila_disponible(tablero, columna):
    # Encuentra la siguiente fila disponible en una columna.
    for fila in range(FILAS - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila
    return None  # Cambié el retorno a None para indicar que la columna está llena

def sugerir_jugada(tablero, ficha):
    # Sugiere una jugada para el jugador, priorizando jugadas ganadoras.
    # Primero, verifica si alguna jugada es ganadora para el jugador
    for col in obtener_jugadas_validas(tablero):
        fila = siguiente_fila_disponible(tablero, col)
        if fila is not None and es_jugada_ganadora(tablero, fila, col, ficha):
            return col
    
    # Si no hay jugadas ganadoras, selecciona una jugada válida al azar
    jugadas_validas = obtener_jugadas_validas(tablero)
    if jugadas_validas:
        return random.choice(jugadas_validas)
    return None  # Retorna None si no hay jugadas válidas
