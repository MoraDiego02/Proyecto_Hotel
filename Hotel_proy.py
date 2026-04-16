from funciones_hotel import *

def main():
    inicio()
    hotel = cargar_matriz()
    dni = ingresar_dni()
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
    opcion_ubicacion = int(input("Seleccione una ubicación (1-2): "))
    while opcion_ubicacion < 1 or opcion_ubicacion > 2:
        print("Opción inválida. Seleccione una ubicación válida.")
        opcion_ubicacion = int(input("Seleccione una ubicación (1-2): "))
    hotel[piso-1][hab-1] = 1 
    print("\nReserva marcada en el mapa:")
    Mostrar_habitaciones(hotel) 
    print(" ")
    precio_final = gestion_reserva(hotel, piso, hab)
    comprobante_reserva(dni, piso, hab, precio_final)

if __name__ == "__main__":
    main()