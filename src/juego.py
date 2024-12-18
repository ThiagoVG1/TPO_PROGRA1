from src.tablero import crear_tablero, imprimir_tablero, hacer_movimiento, comprobar_victoria, tablero_lleno,color_ficha
from src.validar import obtener_columna_valida
from src.jugador import Jugador
from src.jugadas import sugerir_jugada
from colorama import Fore, Style  

def es_movimiento_valido(tablero, columna):
    # Verifica si una columna no está llena.
    return tablero[0][columna] == ' '

def siguiente_fila_disponible(tablero, columna):
    # Encuentra la siguiente fila disponible en una columna especificada.
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            return fila
    return None  # Si la columna está llena

def preguntar_jugar_de_nuevo():
    # Pregunta al usuario si quiere jugar de nuevo y valida la respuesta.
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if respuesta == 's':
            print("\n--- Nueva Partida ---\n")
            return True  # Indica que el jugador quiere otra partida
        elif respuesta == 'n':
            print("¡Gracias por jugar!")
            return False  # Indica que el jugador no quiere jugar de nuevo
        else:
            print("Error. Por favor, ingresa 's' para sí o 'n' para no.")

def iniciar_juego():
    # Función principal que ejecuta el juego.
    jugar = True
    while jugar:
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
            
            # Mostrar el turno con el color de la ficha
            ficha_coloreada = color_ficha(jugador_actual.ficha)
            print(f"Turno de {ficha_coloreada} {jugador_actual.nombre}{Style.RESET_ALL}")

            # Obtener sugerencia de jugada
            sugerencia = sugerir_jugada(tablero, jugador_actual.ficha)
            print(f"Sugerencia de jugada para {Fore.YELLOW}{jugador_actual.nombre}{Style.RESET_ALL}: Columna {sugerencia}")

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
                        jugador_perdedor = jugadores[(turno + 1) % 2]  # Determinar el perdedor
                        print(
                            f"¡{Fore.GREEN}{jugador_actual.nombre} ({jugador_actual.ficha}) ha ganado!{Style.RESET_ALL} "
                            f"{Fore.RED}({jugador_perdedor.nombre} pierde){Style.RESET_ALL}"
                        )
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
        jugar = preguntar_jugar_de_nuevo()
