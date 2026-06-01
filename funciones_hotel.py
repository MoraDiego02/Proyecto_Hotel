import random
import re
from functools import reduce

def cargar_datos(historial):

    print("- -" * 14)
    nombre = input("|    Ingrese su nombre: ")
    print("- -" * 14)
    while not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
        print()
        print("Nombre inválido. Solo se permiten letras y espacios.")
        print()
        print("- -" * 14)
        nombre = input("|    Ingrese su nombre: ")
        print("- -" * 14)
    
    apellido = input("|    Ingrese su apellido: ")
    print("- -" * 14)
    while not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
        print()
        print("Apellido inválido. Solo se permiten letras y espacios.")
        print()
        print("- -" * 14)
        apellido = input("|    Ingrese su apellido: ")
        print("- -" * 14)

    dnis_ingresados = [r["dni"] for r in historial]
    dni = input("|    Ingrese su DNI: ")
    print("- -" * 14)
    while not re.match(r'^\d{8}$', dni) or dni in dnis_ingresados:
        if dni in dnis_ingresados:
            print()
            print("DNI ya registrado. Ingrese uno diferente.")
        else:
            print()
            print("DNI inválido. Debe tener exactamente 8 dígitos.")
        print()
        print("- -" * 14)
        dni = input("|    Ingrese su DNI: ")
        print("- -" * 14)

    emails_ingresados = [r["mail"] for r in historial]
    mail = input("|    Ingrese su correo electrónico: ")
    print("- -" * 14)
    while not re.match(r'^[\w\.]+\@[\w\.]+\.[a-z]{2,3}$', mail) or mail in emails_ingresados:
        if mail in emails_ingresados:
            print()
            print("Email ya registrado. Ingrese uno diferente.")
        else:
            print()
            print("Correo electrónico inválido. Formato esperado: usuario@dominio.com")
            print()
        print("- -" * 14)
        mail = input("|    Ingrese su correo electrónico: ")
        print("- -" * 14)

    telefono = input("|    Ingrese su número de teléfono: ")
    print("- -" * 14)
    while not re.match(r'^\d{10,11}$',telefono):
        print()
        print("Teléfono inválido. Debe tener entre 10 y 11 dígitos.")
        print()
        print("- -" * 14)
        telefono = input("|    Ingrese su número de teléfono: ")
        print("- -" * 14)
        print()
    
    return nombre, apellido, dni, mail, telefono

def gestion_reserva(hotel, piso, hab):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    generar_dia = lambda: random.randint(0, 6)
    que_dia_es = generar_dia()
    datos_habitaciones = habitaciones_hotel()

    #Se controla que el precio base no sea negativo
    while True:
        try:
            precio_estandar = datos_habitaciones[piso][hab]["precio"]
            if precio_estandar < 0:
                raise ValueError
        except ValueError:
            print("El precio de la habitación no puede ser negativo.")
        else:
            break
    
    if 0 <= que_dia_es <= 3:
        mult_dia = 0.80
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un descuento del 20%!")
        print()
    else:
        mult_dia = 1.10
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un aumento del 10%.")
        print()
    print("=" * 40)
    print("¿Con qué desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")
    print("=" * 40)

    print()
    metodo_pago = input("Ingrese el tipo (1 o 2): ")
    print()
    while not re.match(r'^[12]$', metodo_pago):
        print()
        print("Opción inválida. Por favor, ingrese 1 o 2.")
        print()
        metodo_pago = input("Ingrese el tipo (1 o 2): ")
    metodo_pago = int(metodo_pago)

    mult_pago = 1.05 if metodo_pago == 1 else 1.0

    multiplicadores = [mult_dia, mult_pago]
    precio_final = reduce(lambda acc, m: acc * m, multiplicadores, precio_estandar)

    if metodo_pago == 1:
        
        print("Se seleccionó tarjeta. Se aplica un 5% de recargo.")
    else:
        print("Se seleccionó efectivo. No hay recargos extra.")
    print()
    print(f"El precio final a abonar es de: ${precio_final}")
    return precio_final


def pedir_habitacion():
    """La función pedir_habitacion se encarga de solicitar al usuario que ingrese el numero de habitación que desea, la misma contiene una validación donde si el usuario ingresa un carácter erroneo el sistema le va a informar que es una opción invalida y debe volver a ingresar. Retorna el número de habitación ingresado por el usuario."""
    hab = int(input("Ingrese el número de la habitación (1-3): "))
    while hab < 1 or hab > 3:
        print()
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        print()
        hab = int(input("Ingrese el número de la habitación (1-3): "))
    print()
    return hab

def pedir_piso():
    """Solicita el número de piso (1-3). Valida con regex antes de convertir a int."""
    piso = input("Ingrese el número del piso (1-3): ")
    while not re.match(r'^[1-3]$', piso):
        print()
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        print()
        piso = input("Ingrese el número del piso (1-3): ")
    print()
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
    filas = 5
    columnas = 8
    matriz = [[ "       " for _ in range(columnas)] for _ in range(filas)]
    return matriz

def comprobante_reserva(dni, email, piso, hab, precio_final, nombre, apellido, checkin):
    """Muestra un comprobante de reserva con DNI, email, piso, habitación y precio final."""
    print("\n" + "=" * 43)
    print()
    print("|  COMPROBANTE DE RESERVA HOTEL BOUTIQUE  |")
    print("\n" + "=" * 43)
    print(f"Nombre y apellido: {nombre} {apellido}")
    print(f"DNI: {dni}")
    print(f"Email: {email}")
    print(f"Piso: {piso}")
    print(f"Habitación: {hab}")
    print(f"Precio final a abonar: ${precio_final}")
    print()
    print(f"Fecha de check-in: {checkin[0]}/{checkin[1]}/{checkin[2]}")
    print(f"Hora de check-in:  {checkin[3]}:{checkin[4]:02d}")

    print("=" * 43)

def inicio():
    """La función inicio se encarga de mostrar un mensaje de bienvenida al usuario al iniciar el programa."""
    print("=" * 40)
    print()
    print("|      Bienvenido a Hotel Boutique     |")
    print()
    print("=" * 40)
    
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
            },
            4:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            5:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            6:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            7:{
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            },
            8:{
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
            },
            4:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            5:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            6:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            7:{
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            },
            8:{
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
            },
            4:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            5:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            6:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            7:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            8:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            }
        },
         4: { 
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
            },
            4:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            5:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            6:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            7:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            8:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            }
        },
        5: { 
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
            },
            4:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            5:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            6:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            7:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            },
            8:{
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            }
        } 
    } 
    return habitaciones

def mostrar_detalles_eleccion(habitacion_elegida):
    """Muestra por pantalla el tipo, vista y precio de la habitación elegida."""
    print("\n" + "=" * 40)
    print("   DETALLES DE LA ELECCIÓN   ")
    print("=" * 40)
    print(f"Tipo: {habitacion_elegida['tipo']}")
    print(f"Vista: {habitacion_elegida['descripcion']}")
    print(f"Precio Base: ${habitacion_elegida['precio']}")
    print("=" * 40 + "\n")

def eleccion_habitacion():
    while True:
        try:
            tipo = int(input("Ingrese el tipo de habitación que desea elegir (1-Estándar, 2-Superior, 3-Suite): "))
            if tipo not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Tipo de habitación inválido. Por favor, ingrese 1, 2 o 3.")
        else:
            if tipo == 1:
                print("Estándar")
            elif tipo == 2:
                print("Superior")
            elif tipo == 3:
                print("Suite")
            break
    return tipo

def listado_habitaciones(datos_hotel):
    print("\n" + "=" * 40)
    print()
    print("Listado completo de habitaciones:")
    for piso, habitaciones in datos_hotel.items():
        print(f"\n Piso {piso}")
        for hab, detalles in habitaciones.items():
            print(f"  Habitación {hab}: {detalles['tipo']} - {detalles['descripcion']} - ${detalles['precio']}")
    print("\n" + "=" * 40)

def registrar_checkin():
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = random.randint(1, 12)
    dia = random.randint(1, dias_por_mes[mes-1])
    anio = random.randint(2024, 2026)
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)

    checkin = (dia, mes, anio, hora, minuto)
    return checkin



