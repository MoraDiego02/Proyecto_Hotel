import random
from functools import reduce

def gestion_reserva():
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    GenerarDia = lambda: random.randint(0, 6)
    QueDiaEs = GenerarDia()
    Precio_Estandar = 250000
    factores = []

    if 0 <= QueDiaEs <= 3:
        factores.append(0.80)
        print("Como hoy es", Dias[QueDiaEs], "la reserva tiene un descuento del 20%!")
    else:
        factores.append(1.10)
        print("Como hoy es", Dias[QueDiaEs], "la reserva tiene un aumento del 10%")

    print("Con que desea pagar ")
    print("Ingrese 1 para pagar con tarjeta ")
    print("Ingrese 2 para abonar en efectivo ")
    MetodoDePago = int(input("Ingrese el tipo (1 o 2) "))
    while MetodoDePago != 1 and MetodoDePago != 2:
        MetodoDePago = int(input("porfavor ingrese un numero del 1 al 2 "))

    if MetodoDePago == 1:
        print("Se selecciono tarjeta, hay un 5% de recargo para este metodo de pago")
        factores.append(1.05)
    else:
        print("Se selecciono efectivo")
        factores.append(1.00)

    PrecioFinal = reduce(lambda acumulado, factor: acumulado * factor, factores, Precio_Estandar)
    print("el precio final seria de:", PrecioFinal)
    return PrecioFinal

def tipo_habitaciones():
    print("Tipos de habitaciones disponibles:")
    habitaciones = ["Habitación Estandar", "Habitación Superior", "Habitación Suite"]
    lineas = map(lambda item: f"{item[0]}. {item[1]}", enumerate(habitaciones, start=1))
    for linea in lineas:
        print(linea)

def filtrar_ubicaciones_por_habitacion(habitacion):
    ubicaciones = [
        {"opcion": 1, "nombre": "Vista al Jardin", "habitaciones": [1, 2]},
        {"opcion": 2, "nombre": "Vista a la Ciudad", "habitaciones": [1, 2, 3]},
        {"opcion": 3, "nombre": "Frente al Mar", "habitaciones": [3]}
    ]
    return list(filter(lambda ubicacion: habitacion in ubicacion["habitaciones"], ubicaciones))

