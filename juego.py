# Definición de constantes 
FILAS = 6
COLUMNAS = 7

def crear_tablero():
    #Crea un tablero vacío de 6 filas y 7 columnas.
    return [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]

def imprimir_tablero(tablero):
    #Imprime el tablero de juego.
    for fila in tablero:
        print('|' + '|'.join(fila) + '|')
    print(' ' + ' '.join([str(i) for i in range(COLUMNAS)]))

def hacer_movimiento(tablero, fila, columna, ficha):
    #Coloca la ficha del jugador en el tablero
    tablero[fila][columna] = ficha

def comprobar_victoria(tablero, ficha):
    # Comprobar victoria horizontal(--)
    for fila in range(FILAS):
        for col in range(COLUMNAS - 3):
            if tablero[fila][col] == ficha and tablero[fila][col + 1] == ficha and tablero[fila][col + 2] == ficha and tablero[fila][col + 3] == ficha:
                return True
    # Comprobar victoria vertical(I)
    for fila in range(FILAS - 3):
        for col in range(COLUMNAS):
            if tablero[fila][col] == ficha and tablero[fila + 1][col] == ficha and tablero[fila + 2][col] == ficha and tablero[fila + 3][col] == ficha:
                return True

    return False


def es_movimiento_valido(tablero, columna):
    # Verifica si una columna no está llena.
    return tablero[0][columna] == ' '

def siguiente_fila_disponible(tablero, columna):
    # Encuentra la siguiente fila disponible en la columna especificada.
    for fila in range(FILAS - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila

def main():
    tablero=crear_tablero()
    juego_terminado = False
    turno = 0
    while not juego_terminado:
        imprimir_tablero(tablero)
        jugador = turno % 2 + 1
        ficha = 'X' if jugador == 1 else 'O'
        # Pide al jugador que elija una columna
        columna = int(input(f"Jugador  ({ficha}), elige una columna (0-{COLUMNAS-1}): "))
        # Comprueba si la columna esta llena
        if es_movimiento_valido(tablero, columna):
            fila = siguiente_fila_disponible(tablero, columna)
            hacer_movimiento(tablero, fila, columna, ficha)
            
            # Verifica si el jugador ha ganado
            if comprobar_victoria(tablero, ficha):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador} ({ficha}) ha ganado!")               
                juego_terminado = True
            else:
                turno += 1
        else:
            print("Movimiento inválido. Intenta nuevamente.")
        # Verifica si hay empate
        if turno == FILAS * COLUMNAS:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            juego_terminado = True
# Ejecuta el juego
if __name__ == "__main__":
    main()