from colorama import init, Fore,Style

init(autoreset=True)

FILAS = 6
COLUMNAS = 7

def crear_tablero():
    # Crea un tablero vacío de 6 filas y 7 columnas.
    return [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]

def color_ficha(ficha):
    if ficha=='X':
        return Fore.RED + 'X'
    elif ficha=='O':
        return Fore.GREEN + 'O'
    else:
        return Fore.WHITE + ' '
    

def imprimir_tablero(tablero):
# Imprime el tablero de juego.
    for fila in tablero:
        print('|' + '|'.join([color_ficha(c) for c in fila]) + '|')
    print(' ' + ' '.join([str(i) for i in range(COLUMNAS)]))

def hacer_movimiento(tablero, fila, columna, ficha):
    # Coloca la ficha del jugador en el tablero.
    tablero[fila][columna] = ficha

def comprobar_victoria(tablero, ficha):
    # Comprobar victoria horizontal (--)
    for fila in range(FILAS):
        for col in range(COLUMNAS - 3):
            if (tablero[fila][col] == ficha and
                tablero[fila][col + 1] == ficha and
                tablero[fila][col + 2] == ficha and
                tablero[fila][col + 3] == ficha):
                return True

    # Comprobar victoria vertical (|)
    for fila in range(FILAS - 3):
        for col in range(COLUMNAS):
            if (tablero[fila][col] == ficha and
                tablero[fila + 1][col] == ficha and
                tablero[fila + 2][col] == ficha and
                tablero[fila + 3][col] == ficha):
                return True

    # Comprobar victoria diagonal ascendente (\)
    for fila in range(FILAS - 3):
        for col in range(COLUMNAS - 3):
            if (tablero[fila][col] == ficha and
                tablero[fila + 1][col + 1] == ficha and
                tablero[fila + 2][col + 2] == ficha and
                tablero[fila + 3][col + 3] == ficha):
                return True

    # Comprobar victoria diagonal descendente (/)
    for fila in range(3, FILAS):
        for col in range(COLUMNAS - 3):
            if (tablero[fila][col] == ficha and
                tablero[fila - 1][col + 1] == ficha and
                tablero[fila - 2][col + 2] == ficha and
                tablero[fila - 3][col + 3] == ficha):
                return True

    return False

def tablero_lleno(tablero):
    # Verifica si el tablero está lleno.
    for col in range(COLUMNAS):
        if tablero[0][col] == ' ':
            return False
    return True