import unittest
from funciones_hotel import *

class TestValidaciones(unittest.TestCase):
    def test_prueba_validaciones(self):
        print("\n--- Pruebas de Validaciones ---")
        resultado = validar_dni("12345678")

        if resultado == True:
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()