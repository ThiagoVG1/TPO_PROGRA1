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

class TestJugador(unittest.TestCase):

    def test_jugador_init(self):
        jugador = Jugador("Jugador 1", 'X')
        # Verificamos la inicialización correcta del jugador
        self.assertEqual(jugador.nombre, "Jugador 1")
        self.assertEqual(jugador.ficha, 'X')


class TestEstrategias(unittest.TestCase):

    def test_es_jugada_ganadora_horizontal(self):
        tablero = crear_tablero()
        fila, columna = 5, 0
        for col in range(columna, columna + 4):
            hacer_movimiento(tablero, fila, col, 'X')
        # Verificamos que detecta una jugada ganadora horizontal
        self.assertTrue(es_jugada_ganadora(tablero, fila, columna, 'X'))

    def test_obtener_jugadas_validas(self):
        tablero = crear_tablero()
        # Todas las columnas deben estar disponibles inicialmente
        jugadas_validas = obtener_jugadas_validas(tablero)
        self.assertEqual(jugadas_validas, list(range(7)))

    def test_sugerir_jugada(self):
        tablero = crear_tablero()
        # En un tablero vacío, sugerir_jugada debería devolver una jugada válida
        jugada = sugerir_jugada(tablero, 'X')
        self.assertIn(jugada, obtener_jugadas_validas(tablero))

if __name__ == '__main__':
    unittest.main()
