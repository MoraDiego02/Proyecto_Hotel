import random
from functools import reduce

def gestion_reserva(hotel, piso, hab):
    # Nota: Agregué hotel, piso y hab como parámetros para que coincida con el main
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
    print("¿Con qué desea pagar?")
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
    print()
    print("Tipos de habitaciones disponibles:")
<<<<<<< HEAD
    print()
=======
>>>>>>> c00a892e686c9d553cfdcb160c8ae4200435eb8b
    habitaciones = ["Habitación Estandar", "Habitación Superior", "Habitación Suite"]
    lineas = map(lambda item: f"{item[0]}. {item[1]}", enumerate(habitaciones, start=1))
    for linea in lineas:
        print(linea)

def filtrar_ubicaciones_por_habitacion(hotel, habitacion):
    # Agregué 'hotel' como parámetro porque tu main lo envía
    ubicaciones = [
        {"opcion": 1, "nombre": "Vista al Jardin", "habitaciones": [1, 2]},
        {"opcion": 2, "nombre": "Vista a la Ciudad", "habitaciones": [1, 2, 3]},
        {"opcion": 3, "nombre": "Frente al Mar", "habitaciones": [3]}
    ]
    return list(filter(lambda ubicacion: habitacion in ubicacion["habitaciones"], ubicaciones))

def pedir_piso():
    piso = int(input("Ingrese el número del piso (1-3): "))
    while piso < 1 or piso > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        piso = int(input("Ingrese el número del piso (1-3): "))
    return piso

def pedir_habitacion():
<<<<<<< HEAD
    print()
=======
>>>>>>> c00a892e686c9d553cfdcb160c8ae4200435eb8b
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
                print("         ", end="") 
        print()
    return matriz

def cargar_matriz():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return matriz

def comprobante_reserva(dni, piso, hab, precio_final):
    print("\n" + "-" * 30)
    print("--- COMPROBANTE DE RESERVA ---")
    print(f"DNI: {dni}")
    print(f"Piso reservado: {piso}")
    print(f"Habitación reservada: {hab}")
    print(f"Precio final a abonar: ${precio_final}")
    print("-" * 30)

def inicio():
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)

<<<<<<< HEAD
def cargar_datos():
    nombre = input("|    Ingrese su nombre: ")
    print("-" * 40)
    while nombre == "":
        print("El nombre no puede estar vacío. Por favor, ingrese su nombre.")
        nombre = input("|   Ingrese su nombre: ")  
        print("-" * 40) 
    
    apellido = input("|    Ingrese su apellido: ")
    print("-" * 40) 
    while apellido == "":
        print("El apellido no puede estar vacío. Por favor, ingrese su apellido.")
        apellido = input("|    Ingrese su apellido: ")
        print("-" * 40) 

    dni = int(input("|    Ingrese su DNI: "))
    print("-" * 40) 
    while dni < 10000000 or dni > 99999999:
        print("DNI inválido. Debe tener exactamente 8 dígitos.")
        dni = int(input("|    Ingrese su DNI: "))
        print("-" * 40) 

    mail = input("|    Ingrese su correo electrónico: ")
    print("-" * 40) 
    while "@" not in mail or "." not in mail or  "gmail" not in mail:
        print("Correo electrónico inválido. Formato esperado: usuario@gmail.com")
        mail = input("|    Ingrese su correo electrónico: ")
        print("-" * 40)

    telefono = int(input("|    Ingrese su número de teléfono: "))
    print("-" * 40)
    while telefono < 1000000000 or telefono > 99999999999:
        print("Teléfono inválido. Debe tener entre 10 y 11 dígitos.")
        telefono = int(input("|    Ingrese su número de teléfono: "))
        print("-" * 40)
        print()
    return nombre, apellido, dni, mail, telefono
=======
>>>>>>> c00a892e686c9d553cfdcb160c8ae4200435eb8b




