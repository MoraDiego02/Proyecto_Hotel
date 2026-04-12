import random

def gestion_reserva():
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    generar_dia = lambda: random.randint(0, 6)
    que_dia_es = generar_dia() 
    precio_estandar = 250000
    if 0 <= que_dia_es <= 3:
        precio_final = precio_estandar * 0.80
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un descuento del 20%!")
    else:
        precio_final = precio_estandar * 1.10
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un aumento del 10%.")
        
    print(f"El precio base de la reserva es: ${precio_final}")
    print(" ")
    print("Con que desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")
    
    metodo_pago = int(input("Ingrese el tipo (1 o 2): "))
    
    while metodo_pago != 1 and metodo_pago != 2:
        metodo_pago = int(input("Por favor, ingrese un número válido (1 o 2): "))
    
    if metodo_pago == 1:
        precio_final = precio_final * 1.05
        print("Se seleccionó tarjeta. Se aplica un 5% de recargo.")
    else: 
        print("Se seleccionó efectivo. No hay recargos extra.")
        
    print(f"El precio final a abonar es de: ${precio_final}")
    return precio_final

def tipo_habitaciones():
    print("Tipos de habitaciones disponibles:")
    print("1. Habitación Estandar")
    print("2. Habitación Superior")
    print("3. Habitación Suite")

def pedir_piso():
    piso = int(input("Ingrese el número del piso (1-3): "))
    while piso < 1 or piso > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        piso = int(input("Ingrese el número del piso (1-3): "))
    return piso

def pedir_habitacion():
    hab = int(input("Ingrese el número de la habitación (1-3): "))
    while hab < 1 or hab > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        hab = int(input("Ingrese el número de la habitación (1-3): "))
    return hab

def Mostrar_habitaciones(matriz):
    columnas = len(matriz[0])
    print("        ", end="")
    
    for i in range(columnas):
        print(f"Hab {i+1}    ", end="")
    print() 

    for i in range(len(matriz)):
        print(f"Piso {i+1}  ", end="")
        for j in range(columnas):
            if matriz[i][j] == 1:
                print("  x      ", end="")
            else:
                print("        ", end="") 
        print()
    return matriz

def cargar_matriz():
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return matriz

def comprobante_reserva(dni, piso, hab, precio_final):
    print("\n--- COMPROBANTE DE RESERVA ---")
    print(f"DNI: {dni}")
    print(f"Piso reservado: {piso}")
    print(f"Habitación reservada: {hab}")
    print(f"Precio final a abonar: ${precio_final}")






