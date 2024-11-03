from src.tablero import COLUMNAS

def obtener_columna_valida():
 # Solicita una columna valida al jugador, verificando que sea un numero dentro del rango.
    while True:
        try:
            columna = int(input(f"Elige una columna (0-{COLUMNAS-1}): "))
            if 0 <= columna < COLUMNAS:
                return columna
            else:
                print(f"Por favor, ingresa un numero entre 0 y {COLUMNAS-1}.")
        except ValueError:
            print("Error, porfavor ingresa un numero")