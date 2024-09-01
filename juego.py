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
    


tablero = crear_tablero()
imprimir_tablero(tablero)
