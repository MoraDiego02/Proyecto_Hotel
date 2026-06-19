import unittest
from funciones_hotel import *

class TestAltas(unittest.TestCase):
    def test_prueba_altas(self):
        print("\n--- Pruebas de Altas ---")
        # Creamos la matriz
        resultado = cargar_matriz()
        
        # Comprobamos que el alto de la matriz creada sea 5 pisos
        if len(resultado) == 5:
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(len(resultado), 5)

if __name__ == '__main__':
    unittest.main()