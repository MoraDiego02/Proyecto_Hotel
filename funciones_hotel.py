import random
import re
from functools import reduce


def ingresar_dni():
    dni = input("|    Ingrese su DNI: ")
    print("-" * 40)
    while not re.match(r'^\d{8}$', dni):
        print("DNI inválido. Debe tener exactamente 8 dígitos.")
        print()
        dni = input("|    Ingrese su DNI: ")
        print("-" * 40)
    return dni


def solicitar_email():
    mail = input("|    Ingrese su correo electrónico: ")
    print("-" * 40)
    while not re.match(r'^[\w\.]+\@[\w\.]+\.[a-z]{2,3}$', mail):
        print("Correo electrónico inválido. Formato esperado: usuario@dominio.com")
        mail = input("|    Ingrese su correo electrónico: ")
        print("-" * 40)
    return mail

def cargar_datos():
    #Valicacion con try-except para el ingreso de nombre y apellido
    nombre_valido = False
    while not nombre_valido:
        try:
            nombre = input("|    Ingrese su nombre: ")
            print("-" * 40)
            if nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
                raise ValueError("Nombre inválido. Solo se permiten letras y espacios.")
            nombre_valido = True
        except ValueError as e:
            print(e)

    apellido_valido = False
    while not apellido_valido:
        try:
            apellido = input("|    Ingrese su apellido: ")
            print("-" * 40)
            if apellido.strip() == "":
                raise ValueError("El apellido no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
                raise ValueError("Apellido inválido. Solo se permiten letras y espacios.")
            apellido_valido = True
        except ValueError as e:
            print(e) 

    dni = ingresar_dni()
    mail = solicitar_email()

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
    datos_habitaciones = habitaciones_hotel()

    #Se controla que el precio base no sea negativo
    try:
        precio_estandar = datos_habitaciones[piso][hab]["precio"]
        if precio_estandar < 0:
            raise ValueError("El precio de la habitación no puede ser negativo.")
    except ValueError as e:
        print(f"Error en el precio: {e}")
        return 0
    
    if 0 <= que_dia_es <= 3:
        mult_dia = 0.80
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un descuento del 20%!")
    else:
        mult_dia = 1.10
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un aumento del 10%.")

    print("¿Con qué desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")

    #Validacion con try-except para el ingreso del método de pago
    pago_valido = False
    while not pago_valido:
        try:
            metodo_pago_str = input("Ingrese el tipo (1 o 2): ")
            if not re.match(r'^[12]$', metodo_pago_str):
                raise ValueError("Opción inválida. Por favor, ingrese 1 o 2.")
            metodo_pago = int(metodo_pago_str)
            pago_valido = True
        except ValueError as e:
            print(e)

    mult_pago = 1.05 if metodo_pago == 1 else 1.0

    multiplicadores = [mult_dia, mult_pago]
    precio_final = reduce(lambda acc, m: acc * m, multiplicadores, precio_estandar)

    if metodo_pago == 1:
        print("Se seleccionó tarjeta. Se aplica un 5% de recargo.")
    else:
        print("Se seleccionó efectivo. No hay recargos extra.")

    print(f"El precio final a abonar es de: ${precio_final}")
    return precio_final


def pedir_habitacion():
    """Solicita el número de habitación (1-3). Controla letras y valores fuera de rango con try/except."""
    #Validacion con try-except para el ingreso del número de habitación
    ingreso_valido = False
    while not ingreso_valido:
        try:
            hab = int(input("Ingrese el número de la habitación (1-3): "))
            if hab < 1 or hab > 3:
                raise ValueError("El número debe estar entre 1 y 3.")
            ingreso_valido = True
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
    return hab

def pedir_piso():
    """Solicita el número de piso (1-3). Valida con regex antes de convertir a int."""
    piso = input("Ingrese el número del piso (1-3): ")
    while not re.match(r'^[1-3]$', piso):
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        piso = input("Ingrese el número del piso (1-3): ")
    return int(piso)


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

def comprobante_reserva(dni, email, piso, hab, precio_final, nombre, apellido):
    """Muestra un comprobante de reserva con DNI, email, piso, habitación y precio final."""
    print("\n" + "-" * 30)
    print("--- COMPROBANTE DE RESERVA HOTEL BOUTIQUE ---")
    print(f"Nombre y apellido: {nombre} {apellido}")
    print(f"DNI: {dni}")
    print(f"Email: {email}")
    print(f"Piso: {piso}")
    print(f"Habitación: {hab}")
    print(f"Precio final a abonar: ${precio_final}")
    print("-" * 30)

def inicio():
    """La función inicio se encarga de mostrar un mensaje de bienvenida al usuario al iniciar el programa."""
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)
    
def habitaciones_hotel():
    habitaciones = {
        1: { 
            1:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            2:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            3:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            }
        }, 
        2: { 
            1:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            2:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            3:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            }
        }, 
        3: { 
            1:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            2:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            3:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            }
        } 
    } 
    return habitaciones

def mostrar_detalles_eleccion(habitacion_elegida):
    """Muestra por pantalla el tipo, vista y precio de la habitación elegida."""
    print("\n" + "=" * 30)
    print("   DETALLES DE LA ELECCIÓN   ")
    print("=" * 30)
    print(f"Tipo: {habitacion_elegida['tipo']}")
    print(f"Vista: {habitacion_elegida['descripcion']}")
    print(f"Precio Base: ${habitacion_elegida['precio']}")
    print("=" * 30 + "\n")

def listado_habitaciones(datos_hotel):
    print("Listado completo de habitaciones:")
    for piso, habitaciones in datos_hotel.items():
        print(f"\n Piso {piso}")
        for hab, detalles in habitaciones.items():
            print(f"  Habitación {hab}: {detalles['tipo']} - {detalles['descripcion']} - ${detalles['precio']}")
    print("\n" + "=" * 30)
    



