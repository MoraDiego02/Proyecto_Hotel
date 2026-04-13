from funciones_hotel import *

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
    ubicaciones_disponibles = filtrar_ubicaciones_por_habitacion(hotel, hab)
    if not ubicaciones_disponibles:
        print("No hay ubicaciones disponibles para la habitación seleccionada.")
        return
    print(" Seleccione la Ubicacion:")
    for ubicacion in ubicaciones_disponibles:
        print(f"{ubicacion['opcion']}. {ubicacion['nombre']}")
    opcion_ubicacion = pedir_ubicacion(ubicaciones_disponibles)
    ubicacion_seleccionada = next(
        ubicacion for ubicacion in ubicaciones_disponibles if ubicacion["opcion"] == opcion_ubicacion
    )
    print(f"Ubicación seleccionada: {ubicacion_seleccionada['nombre']}")

    hotel[piso-1][hab-1] = 1 
    print("\nReserva marcada en el mapa:")
    Mostrar_habitaciones(hotel) 
    print(" ")
    precio_final = gestion_reserva(hotel, piso, hab)
    comprobante_reserva(dni, piso, hab, precio_final)

if __name__ == "__main__":
    main()