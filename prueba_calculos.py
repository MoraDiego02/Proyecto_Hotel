import unittest
from funciones_hotel import *

class TestCalculos(unittest.TestCase):
    def test_prueba_calculos(self):
        print("\n--- Pruebas de Cálculos ---")
        resultado = calcular_precio(250000, "Lunes", 2)
        
        if resultado == 200000.0:
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(resultado, 200000.0)

if __name__ == '__main__':
    unittest.main()