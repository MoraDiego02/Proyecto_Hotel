import random

def gestion_reserva():
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    GenerarDia = lambda : random.randint(0,6)
    QueDiaEs=GenerarDia()
    Precio_Estandar=250000
    if 0<= QueDiaEs <= 3 :
        PrecioFinal=Precio_Estandar*0.80
        print("Como hoy es",Dias[QueDiaEs],"la reserva tiene un descuento del 20%!")
        print("La reserva del hotel esta:",PrecioFinal)
    else:
        PrecioFinal=Precio_Estandar*1.10
        print("Como hoy es",Dias[QueDiaEs],"la reserva tiene un aumento del 10%")
        print("La reserva del hotel esta:",PrecioFinal)
    print("Con que desea pagar ")
    print("Ingrese 1 para pagar con tarjeta ")
    print("Ingrese 2 para abonar en efectivo ")
    MetodoDePago=int(input("Ingrese el tipo (1 o 2) "))
    while MetodoDePago != 1 and MetodoDePago != 2:
        MetodoDePago=int(input("porfavor ingrese un numero del 1 al 2 "))
    if MetodoDePago == 1:
        print("Se selecciono tarjeta, hay un 5% de recargo para este metodo de pago")
        PrecioFinal=PrecioFinal*1.05
        print("el precio final seria de:",PrecioFinal)
        return PrecioFinal
    else: 
        print("Se selecciono efectivo")
        return PrecioFinal

def tipo_habitaciones():
    print("Tipos de habitaciones disponibles:")
    print("1. Habitación Estandar")
    print("2. Habitación Superior")
    print("3. Habitación Suite")

