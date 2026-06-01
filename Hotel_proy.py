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
        "telefono": telefono
    })

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
            print("=" * 38)
    print()
    print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")
 
if __name__ == "__main__":
    main()