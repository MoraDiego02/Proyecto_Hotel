import random
import re
from functools import reduce


def cargar_datos():
    #Valicacion con try-except para el ingreso de nombre y apellido
    while True:
        try:
            nombre = input("|    Ingrese su nombre: ")
            print("-" * 40)
            if nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
                raise ValueError
        except ValueError:
            print("Nombre inválido. Solo se permiten letras y espacios.")
        else:
            break
    
    while True:
        try:
            apellido = input("|    Ingrese su apellido: ")
            print("-" * 40)
            if apellido.strip() == "":
                raise ValueError("El apellido no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
                raise ValueError
        except ValueError:
            print("Apellido inválido. Solo se permiten letras y espacios.") 
        else:
            break

    while True:
        try:
            dni = input("|    Ingrese su DNI: ")
            print("-" * 40)
            if not re.match(r'^\d{8}$', dni):
                raise ValueError
        except ValueError:
            print("DNI inválido. Debe tener exactamente 8 dígitos.")
        else:
            break
        
    while True:
        try:
            mail = input("|    Ingrese su correo electrónico: ")
            print("-" * 40)
            if not re.match(r'^[\w\.]+\@[\w\.]+\.[a-z]{2,3}$', mail):
                raise ValueError
        except ValueError:
            print("Correo electrónico inválido. Formato esperado: usuario@dominio.com")
        else:
            break

    # Validacion con try-except para el ingreso del numero de telefono
    while True:
        try:
            telefono = input("|    Ingrese su número de teléfono: ")
            print("-" * 40)
            if not re.match(r'^\d{10,11}$',telefono):
                raise ValueError
        except ValueError:
            print("Teléfono inválido. Debe tener entre 10 y 11 dígitos.")
        else:
            break
            
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
    else:
        mult_dia = 1.10
        print(f"Como hoy es {dias[que_dia_es]}, la reserva tiene un aumento del 10%.")

    print("¿Con qué desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")

    #Validacion con try-except para el ingreso del método de pago
    while True:
        try:
            metodo_pago_str = input("Ingrese el tipo (1 o 2): ")
            if not re.match(r'^[12]$', metodo_pago_str):
                raise ValueError
            metodo_pago = int(metodo_pago_str)
        except ValueError:
            print("Opción inválida. Por favor, ingrese 1 o 2.")
        else:
            break

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
    while True:
        try:
            hab = int(input("Ingrese el número de la habitación (1-8): "))
            if hab < 1 or hab > 8:
                raise ValueError
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
        else:
            break
    return hab

def pedir_piso():
    """Solicita el número de piso (1-8). Valida con regex antes de convertir a int."""
    while True:
        piso = input("Ingrese el número del piso (1-5): ")
        if not re.match(r'^[1-5]$', piso):
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        else:
            break
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
    print("\n" + "=" * 30)
    print("   DETALLES DE LA ELECCIÓN   ")
    print("=" * 30)
    print(f"Tipo: {habitacion_elegida['tipo']}")
    print(f"Vista: {habitacion_elegida['descripcion']}")
    print(f"Precio Base: ${habitacion_elegida['precio']}")
    print("=" * 30 + "\n")

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
    print("Listado completo de habitaciones:")
    for piso, habitaciones in datos_hotel.items():
        print(f"\n Piso {piso}")
        for hab, detalles in habitaciones.items():
            print(f"  Habitación {hab}: {detalles['tipo']} - {detalles['descripcion']} - ${detalles['precio']}")
    print("\n" + "=" * 30)
    