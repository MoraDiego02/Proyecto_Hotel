<<<<<<< HEAD
from funciones_hotel import tipo_habitaciones, pedir_piso, pedir_habitacion, Mostrar_habitaciones, cargar_matriz, gestion_reserva, comprobante_reserva
=======
from funciones_hotel import filtrar_ubicaciones_por_habitacion, gestion_reserva, tipo_habitaciones
>>>>>>> f4bcc39de617450c8b297e522f0097f55b0fdde8

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
<<<<<<< HEAD
    piso = pedir_piso()
    hab = pedir_habitacion()
    print(f"Has seleccionado la habitación {hab} en el piso {piso}.\n")
    hotel[piso - 1][hab - 1] = 1
    print("Estado actual de las habitaciones:")
    Mostrar_habitaciones(hotel)
    print(" ")
    precio_final = gestion_reserva()
    comprobante_reserva(dni, piso, hab, precio_final)
=======
    print("Usted ha seleccionado la habitación ", habitacion)
    print("Elija la locacion de la habitación:")
    ubicaciones_disponibles = filtrar_ubicaciones_por_habitacion(habitacion)

    for ubicacion in ubicaciones_disponibles:
        print(f"{ubicacion['opcion']}. {ubicacion['nombre']}")

    opcion_ubicacion = int(input("Ingrese el número de la ubicación: "))
    opciones_validas = list(map(lambda u: u["opcion"], ubicaciones_disponibles))

    while opcion_ubicacion not in opciones_validas:
        opcion_ubicacion = int(input("Opción inválida. Ingrese una ubicación disponible: "))

    ubicacion_elegida = next(filter(lambda u: u["opcion"] == opcion_ubicacion, ubicaciones_disponibles))
    print(f"Usted eligió: {ubicacion_elegida['nombre']}")

    total = gestion_reserva()
    print(f"Total de la reserva: {total}")

>>>>>>> f4bcc39de617450c8b297e522f0097f55b0fdde8



if __name__ == "__main__":
<<<<<<< HEAD
=======
    inicio()
>>>>>>> f4bcc39de617450c8b297e522f0097f55b0fdde8
    main()