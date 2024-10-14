from src.tablero import crear_tablero, imprimir_tablero, hacer_movimiento, comprobar_victoria, tablero_lleno
from src.validar import obtener_columna_valida
from src.jugador import Jugador

def es_movimiento_valido(tablero, columna):
    #Verifica si una columna no esta llena.
    return tablero[0][columna] == ' '

def siguiente_fila_disponible(tablero, columna):
    #Encuentra la siguiente fila disponible en la columna especificada.
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila
    return None  # Si la columna está llena

def iniciar_juego():
    #Función principal que ejecuta el juego
    while True:
        tablero = crear_tablero()
        juego_terminado = False
        turno = 0

        # Inicializar jugadores
        jugador1 = Jugador("Jugador 1", 'X')
        jugador2 = Jugador("Jugador 2", 'O')
        jugadores = [jugador1, jugador2]

        while not juego_terminado:
            imprimir_tablero(tablero)
            jugador_actual = jugadores[turno % 2]
            print(f"Turno de {jugador_actual}")

            # Obtener una columna válida
            columna = obtener_columna_valida()

            # Comprueba si la columna está llena
            if es_movimiento_valido(tablero, columna):
                fila = siguiente_fila_disponible(tablero, columna)
                if fila is not None:
                    hacer_movimiento(tablero, fila, columna, jugador_actual.ficha)

                    # Verifica si el jugador ha ganado
                    if comprobar_victoria(tablero, jugador_actual.ficha):
                        imprimir_tablero(tablero)
                        print(f"¡{jugador_actual.nombre} ({jugador_actual.ficha}) ha ganado!")
                        juego_terminado = True
                    else:
                        turno += 1
                else:
                    print("Columna llena. Intenta nuevamente.")
            else:
                print("Columna llena. Intenta nuevamente.")

            # Verifica si hay empate
            if tablero_lleno(tablero) and not juego_terminado:
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                juego_terminado = True

        # Preguntar si quieren jugar de nuevo
        jugar_de_nuevo = input("Queres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar!")
            break
        else:
            print("\n--- Nueva Partida ---\n")
