from funciones_hotel import *

def main():
    inicio()
    hotel = cargar_matriz()
    nombre, apellido, dni, mail, telefono = cargar_datos()
    tipo_habitaciones()
    print(" ")
    piso = pedir_piso()
    hab = pedir_habitacion()
    ubicaciones_disponibles = filtrar_ubicaciones_por_habitacion(hotel, hab)
    if not ubicaciones_disponibles:
        print("No hay ubicaciones disponibles para la habitación seleccionada.")
        return
    print()
    print(" Seleccione la Ubicacion:")
    print()
    for ubicacion in ubicaciones_disponibles:
        print(f"{ubicacion['opcion']}. {ubicacion['nombre']}")
    print()
    opcion_ubicacion = int(input("Seleccione una ubicación (1-2): "))
    print()
    while opcion_ubicacion < 1 or opcion_ubicacion > 2:
        print("Opción inválida. Seleccione una ubicación válida.")
        print()
        opcion_ubicacion = int(input("Seleccione una ubicación (1-2): "))
    hotel[piso-1][hab-1] = 1
    print() 
    print("\nReserva marcada en el mapa:")
    print()
    Mostrar_habitaciones(hotel) 
    print(" ")
    precio_final = gestion_reserva(hotel, piso, hab)
    comprobante_reserva(dni, piso, hab, precio_final)

if __name__ == "__main__":
    main()