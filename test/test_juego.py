import unittest
from src.tablero import crear_tablero, hacer_movimiento, comprobar_victoria, tablero_lleno
from src.jugador import Jugador
from src.jugadas import es_jugada_ganadora, obtener_jugadas_validas, sugerir_jugada

class TestTablero(unittest.TestCase):

    def test_crear_tablero(self):
        tablero = crear_tablero()
        # Verificamos que el tablero tenga la dimensión correcta
        self.assertEqual(len(tablero), 6)
        self.assertEqual(len(tablero[0]), 7)
        # Verificamos que el tablero esté vacío
        self.assertTrue(all(cell == ' ' for row in tablero for cell in row))

    def test_hacer_movimiento(self):
        tablero = crear_tablero()
        hacer_movimiento(tablero, 5, 0, 'X')
        # Verificamos que la ficha se haya colocado en la posición correcta
        self.assertEqual(tablero[5][0], 'X')

    def test_comprobar_victoria_horizontal(self):
        tablero = crear_tablero()
        for col in range(4):
            hacer_movimiento(tablero, 5, col, 'X')
        # Verificamos que detecta una victoria horizontal
        self.assertTrue(comprobar_victoria(tablero, 'X'))

    def test_tablero_lleno(self):
        tablero = crear_tablero()
        # Llenamos el tablero
        for fila in range(6):
            for col in range(7):
                hacer_movimiento(tablero, fila, col, 'X' if (fila + col) % 2 == 0 else 'O')
        # Verificamos que detecta el tablero lleno
        self.assertTrue(tablero_lleno(tablero))

if __name__ == '__main__':
    unittest.main()