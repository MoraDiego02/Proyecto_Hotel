import re
from funciones_hotel import *

def main():
    inicio()
    dnis_ingresados = []
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
    opcion_ubicacion = pedir_ubicacion(ubicaciones_disponibles)
    ubicacion_seleccionada = next(
        ubicacion for ubicacion in ubicaciones_disponibles if ubicacion["opcion"] == opcion_ubicacion
    )
    print(f"Ubicación seleccionada: {ubicacion_seleccionada['nombre']}")

    hotel[piso-1][hab-1] = 1 
    print("Reserva seleccionada:")
    Mostrar_habitaciones(hotel) 
    print(" ")
    precio_final = gestion_reserva(hotel, piso, hab)
    comprobante_reserva(dni, mail, piso, hab, precio_final, nombre, apellido)
    volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
    while not re.match(r'^(si|no)$', volver_a_reservar, re.IGNORECASE):
        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
        volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
 
    if re.match(r'^si$', volver_a_reservar, re.IGNORECASE):
        main()
    else:
        print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")
 
if __name__ == "__main__":
    main()