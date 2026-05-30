
import re
from funciones_hotel import *

def main():
    inicio()
    dnis_ingresados = []
    hotel = cargar_matriz()

    nombre, apellido, dni, mail, telefono = cargar_datos()
    
    #Se controla que el DNI ingresado sea único para evitar duplicados en el sistema de reservas
    while True:
        try:
            if dni in dnis_ingresados:
                raise ValueError
            dnis_ingresados.append(dni)
        except ValueError:
            print("DNI ya registrado. Ingrese uno diferente.")
            nombre, apellido, dni, mail, telefono = cargar_datos()
        else:
            break

    datos_hotel = habitaciones_hotel()
    print(" ")
    listado_habitaciones(datos_hotel)
    print(" ")
    piso = pedir_piso()
    hab = pedir_habitacion()

    #Se controla que la habitación seleccionada exista en el diccionario
    while True:
        try:
            habitacion_elegida = datos_hotel[piso][hab]
            break
        except KeyError:
            print("Error: la habitación seleccionada no existe en el sistema.")
        else:
            break

    habitacion_elegida = datos_hotel[piso][hab]
    mostrar_detalles_eleccion(habitacion_elegida)
    hotel[piso-1][hab-1] = 1 
    print("Reserva seleccionada:")
    Mostrar_habitaciones(hotel) 
    print(" ")

    precio_final = gestion_reserva(hotel, piso, hab)
    comprobante_reserva(dni, mail, piso, hab, precio_final, nombre, apellido)
    while True:
        try:
            volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
            if not re.match(r'^(si|no)$', volver_a_reservar, re.IGNORECASE):
                raise ValueError
        except ValueError:
            print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
        else:
            break
 
    if re.match(r'^si$', volver_a_reservar, re.IGNORECASE):
        main()
    else:
        print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")
 
if __name__ == "__main__":
    main()