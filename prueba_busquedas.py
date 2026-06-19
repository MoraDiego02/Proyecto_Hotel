import unittest
from funciones_hotel import *

class TestBusquedas(unittest.TestCase):
    def test_prueba_busquedas(self):
        print("\n--- Pruebas de Búsquedas ---")
        # Buscamos informacion de las habitaciones
        datos = habitaciones_hotel()
        
        # Buscamos en el piso 1, la habitacion 1
        resultado = datos[1][1]["tipo"]
        
        # Comprobamos si tiene el nombre correcto
        if resultado == "Habitación Estandar":
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(resultado, "Habitación Estandar")

if __name__ == '__main__':
    unittest.main()