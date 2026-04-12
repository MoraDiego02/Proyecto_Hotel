from funciones_hotel import tipo_habitaciones, pedir_piso, pedir_habitacion, Mostrar_habitaciones, cargar_matriz, gestion_reserva, comprobante_reserva

def inicio():
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)

def main():
    inicio()
    hotel = cargar_matriz()
    dni = int(input("Ingrese su DNI: "))
    while dni < 10000000 or dni > 99999999:
        print("DNI inválido. Debe tener 8 dígitos.")
        dni = int(input("Ingrese su DNI: "))
    print(f"DNI ingresado: {dni}\n")
    tipo_habitaciones()
    print(" ")
    piso = pedir_piso()
    hab = pedir_habitacion()
    print(f"Has seleccionado la habitación {hab} en el piso {piso}.\n")
    hotel[piso - 1][hab - 1] = 1
    print("Estado actual de las habitaciones:")
    Mostrar_habitaciones(hotel)
    print(" ")
    precio_final = gestion_reserva()
    comprobante_reserva(dni, piso, hab, precio_final)



if __name__ == "__main__":
    main()