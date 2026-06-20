import unittest
from funciones_hotel import *

class TestBusquedas(unittest.TestCase):
    def test_prueba_busquedas(self):
        print("\n--- Pruebas de Búsquedas ---")
        datos = habitaciones_hotel()
        resultado = datos[1][1]["tipo"]
        if resultado == "Habitación Estandar":
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(resultado, "Habitación Estandar")

if __name__ == '__main__':
    unittest.main()