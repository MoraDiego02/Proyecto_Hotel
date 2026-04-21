import re
from funciones_hotel import *

def main():
    inicio()
    dnis_ingresados = []
    hotel = cargar_matriz()

    nombre, apellido, dni, mail, telefono = cargar_datos()
    
    if dni in dnis_ingresados:                                    
        print("DNI ya registrado. Ingrese uno diferente.")
        nombre, apellido, dni, mail, telefono = cargar_datos()
    else:
        dnis_ingresados.append(dni)

    tipo_habitaciones()
    print(" ")
    piso = pedir_piso()
    hab = pedir_habitacion()
    ubicaciones_disponibles = filtrar_ubicaciones_por_habitacion(hotel, hab)
    if not ubicaciones_disponibles:
        print("No hay ubicaciones disponibles para la habitación seleccionada.")
        return
    print(" ")
    print(" Seleccione la ubicación:")
    for ubicacion in ubicaciones_disponibles:
        print(f"{ubicacion['opcion']}. {ubicacion['nombre']}")
    opcion_ubicacion = input("Seleccione una ubicación (1-3): ")
    while not re.match(r'^[1-3]$', opcion_ubicacion):
        print("Opción inválida. Seleccione una ubicación válida.")
        opcion_ubicacion = input("Seleccione una ubicación (1-3): ")
    opcion_ubicacion = int(opcion_ubicacion)
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