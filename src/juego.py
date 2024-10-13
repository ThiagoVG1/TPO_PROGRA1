# src/juego.py

from src.tablero import crear_tablero, imprimir_tablero, hacer_movimiento, comprobar_victoria
from src.validar import obtener_columna_valida

def es_movimiento_valido(tablero, columna):
    #Verifica si una columna no esta llena.
    return tablero[0][columna] == ' '

def siguiente_fila_disponible(tablero, columna):
    #Encuentra la siguiente fila disponible en la columna especificada.
    for fila in range(5, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila
    return None  # Si la columna está llena

def iniciar_juego():
    #Función principal que ejecuta el juego 4 en Raya
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
            if fila is not None:
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
        else:
            print("Columna llena. Intenta nuevamente.")

        # Verifica si hay empate
        if turno == 42 and not juego_terminado:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            juego_terminado = True
