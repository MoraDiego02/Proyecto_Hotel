import random
import re
from functools import reduce

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

    dni = input("|    Ingrese su DNI: ")
    print("-" * 40) 
    while not re.match(r'^\d{8}$',dni):
        print("DNI inválido. Debe tener exactamente 8 dígitos.")
        print()
        dni = input("|    Ingrese su DNI: ")
        print("-" * 40) 

    mail = input("|    Ingrese su correo electrónico: ")
    print("-" * 40) 
    while "@" not in mail or "." not in mail or  "gmail" not in mail:
        print("Correo electrónico inválido. Formato esperado: usuario@gmail.com")
        mail = input("|    Ingrese su correo electrónico: ")
        print("-" * 40)

    telefono = input("|    Ingrese su número de teléfono: ")
    print("-" * 40)
    while not re.match(r'^\d{10,11}$',telefono):
        print("Teléfono inválido. Debe tener entre 10 y 11 dígitos.")
        print()
        telefono = input("|    Ingrese su número de teléfono: ")
        print("-" * 40)
        print()
    
    return nombre, apellido, dni, mail, telefono

def gestion_reserva(hotel, piso, hab):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    generar_dia = lambda: random.randint(0, 6)
    que_dia_es = generar_dia()
    precio_estandar = 250000

    if 0 <= que_dia_es <= 3:
        mult_dia = 0.80
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un descuento del 20%!")
    else:
        mult_dia = 1.10
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un aumento del 10%.")

    print("¿Con qué desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")

    metodo_pago = int(input("Ingrese el tipo (1 o 2): "))
    while metodo_pago not in [1, 2]:
        metodo_pago = int(input("Por favor, ingrese un número válido (1 o 2): "))

    mult_pago = 1.05 if metodo_pago == 1 else 1.0

    multiplicadores = [mult_dia, mult_pago]
    precio_final = reduce(lambda acc, m: acc * m, multiplicadores, precio_estandar)

    if metodo_pago == 1:
        print("Se seleccionó tarjeta. Se aplica un 5% de recargo.")
    else:
        print("Se seleccionó efectivo. No hay recargos extra.")

    print(f"El precio final a abonar es de: ${precio_final}")
    return precio_final

def tipo_habitaciones():
    print()
    print("Tipos de habitaciones disponibles:")
    habitaciones = ["Habitación Estandar", "Habitación Superior", "Habitación Suite"]
    lineas = map(lambda i, h: f"{i}. {h}", range(1, len(habitaciones) + 1), habitaciones)
    for linea in lineas:
        print(linea)

def filtrar_ubicaciones_por_habitacion(hotel, habitacion):
    ubicaciones = [
        {"opcion": 1, "nombre": "Vista al Jardin", "habitaciones": [1, 2]},
        {"opcion": 2, "nombre": "Vista a la Ciudad", "habitaciones": [1, 2, 3]},
        {"opcion": 3, "nombre": "Frente al Mar", "habitaciones": [3]}
    ]
    return list(filter(lambda ubicacion: habitacion in ubicacion["habitaciones"], ubicaciones))

def pedir_piso():
    """La función pedir_piso se encarga de solicitar al usuario que ingrese el número de piso que desea de la reserva, la misma contiene una validación donde si el usuario ingres aun numero erroneo u otra cosa el sistema le va a informar que es una opción invalida y debe volver a ingresar el número de piso. Retorna el número de piso ingresado por el usuario."""
    piso = int(input("Ingrese el número del piso (1-3): "))
    while piso < 1 or piso > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        piso = int(input("Ingrese el número del piso (1-3): "))
    return piso

def pedir_habitacion():
    """La función pedir_habitacion se encarga de solicitar al usuario que ingrese el numero de habitación que desea, la misma contiene una validación donde si el usuario ingresa un carácter erroneo el sistema le va a informar que es una opción invalida y debe volver a ingresar. Retorna el número de habitación ingresado por el usuario."""
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
    """La funcion cargar_matriz se encarga de crear una matriz de 3x3 con valores iniciales de 0, donde cada fila representa un piso y cada columna representa una habitación. Retorna la matriz creada."""
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return matriz

def comprobante_reserva(dni, piso, hab, precio_final):
    """La función comprobante_reserva se encarga de mostrar un comprobante de reserva con el DNI del cliente, el piso reservado, la habitación reservada y el precio final. Recibe como parámetros el DNI, el piso, la habitación y el precio final."""
    print("\n" + "-" * 30)
    print("--- COMPROBANTE DE RESERVA HOTEL BOUTIQUE ---")
    print(f"DNI: {dni}")
    print(f"Piso: {piso}")
    print(f"Habitación: {hab}")
    print(f"Precio final a abonar: ${precio_final}")
    print("-" * 30)

def inicio():
    """La función inicio se encarga de mostrar un mensaje de bienvenida al usuario al iniciar el programa."""
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)





