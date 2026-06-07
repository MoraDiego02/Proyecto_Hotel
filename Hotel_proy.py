
import re
from funciones_hotel import *

def main(historial = []):
    inicio()
    hotel = cargar_matriz()
    nombre, apellido, dni, mail, telefono = cargar_datos(historial)

    historial.append({
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "mail": mail,
        "telefono": telefono,
        "checkin": checkin 
    })

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
    checkin = registrar_checkin()
    comprobante_reserva(dni, mail, piso, hab, precio_final, nombre, apellido, checkin)

    print() 
    volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
    while not re.match(r'^(si|no)$', volver_a_reservar, re.IGNORECASE):
        print()
        print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
        print()
        volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
 
    if re.match(r'^si$', volver_a_reservar, re.IGNORECASE):
        main(historial)
    
    else:
        print()
        ver_historial = input("¿Desea ver el historial de reservas? (si/no): ")
        while not re.match(r'^(si|no)$', ver_historial, re.IGNORECASE):
            print()
            print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
            print()
            ver_historial = input("¿Desea ver el historial de reservas? (si/no): ")

    if re.match(r'^si$', ver_historial, re.IGNORECASE):
        print("\n" + "=" * 38)
        print()
        print("|     HISTORIAL DE RESERVAS DEL DÍA     |")
        print()
        print("=" * 38)
        for i, r in enumerate(historial, 1):
            print(f"  {i}. {r['nombre']} {r['apellido']}")
            print(f"     DNI: {r['dni']}")
            print(f"     Mail: {r['mail']}")
            print(f"     Teléfono: {r['telefono']}")
            print(f"     Fecha de check-in: {r['checkin'][0]}/{r['checkin'][1]}/{r['checkin'][2]}")
            print(f"     Hora de check-in:  {r['checkin'][3]}:{r['checkin'][4]:02d}")
            print("=" * 38)
    print()
    print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")
 
if __name__ == "__main__":
    main()