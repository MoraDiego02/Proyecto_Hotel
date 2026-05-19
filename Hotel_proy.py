import re
from funciones_hotel import *

def main():
    inicio()
    dnis_ingresados = []
    hotel = cargar_matriz()
    nombre, apellido, dni, mail, telefono = cargar_datos()
    datos_hotel = habitaciones_hotel()
    print(" ")
    listado_habitaciones(datos_hotel)
    print(" ")
    piso = pedir_piso()
    hab = pedir_habitacion()
    habitacion_elegida = datos_hotel[piso][hab]
    mostrar_detalles_eleccion(habitacion_elegida)
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