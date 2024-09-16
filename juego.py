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
   #Coloca la ficha del jugador en el tablero.
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


def es_movimiento_valido(tablero, columna):
    #Verifica si una columna no esta llena.
    return tablero[0][columna] == ' '

def siguiente_fila_disponible(tablero, columna):
    #Encuentra la siguiente fila disponible en la columna especificada.
    for fila in range(FILAS - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila

def obtener_columna_valida():
    #Solicita una columna valida al jugador, verificando que sea un numero dentro del rango.
    while True:
        try:
            columna = int(input(f"Elige una columna (0-{COLUMNAS-1}): "))
            if 0 <= columna < COLUMNAS:
                return columna
            else:
                print(f"Por favor, ingresa un numero entre 0 y {COLUMNAS-1}.")
        except ValueError:
            print("Error, porfavor ingresa un numero.")

def main():
    #Función principal que ejecuta el juego 4 en Raya.
    tablero = crear_tablero()
    juego_terminado = False
    turno = 0

    while not juego_terminado:
        imprimir_tablero(tablero)
        jugador = turno % 2 + 1
        ficha = 'X' if jugador == 1 else 'O'
        print(f"Jugador {jugador} ({ficha})")

        # Obtener una columna válida
        columna = obtener_columna_valida()

        # Comprueba si la columna está llena
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
            print("Columna llena. Intenta nuevamente.")

        # Verifica si hay empate
        if turno == FILAS * COLUMNAS:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            juego_terminado = True
# Ejecuta el juego
if __name__ == "__main__":
    main()
