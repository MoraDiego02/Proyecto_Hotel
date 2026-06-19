import unittest
from funciones_hotel import *

class TestCalculos(unittest.TestCase):
    def test_prueba_calculos(self):
        print("\n--- Pruebas de Cálculos ---")
        # Pasamos datos fijos: Precio base(250000), dia (Lunes), pago (2:Efectivo)
        resultado = calcular_precio(250000, "Lunes", 2)
        
        # Sabemos que debe dar 200000 porque el lunes da 20% descuento
        if resultado == 200000.0:
            print("Prueba correcta")
        else:
            print("Error en la prueba")
            
        self.assertEqual(resultado, 200000.0)

if __name__ == '__main__':
    unittest.main()