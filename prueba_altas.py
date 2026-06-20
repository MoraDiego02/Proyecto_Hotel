import unittest
from funciones_hotel import *

class TestAltas(unittest.TestCase):
    def test_prueba_altas(self):
        print("\n--- Pruebas de Altas ---")
        resultado = cargar_matriz()
        if len(resultado) == 5:
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(len(resultado), 5)

if __name__ == '__main__':
    unittest.main()