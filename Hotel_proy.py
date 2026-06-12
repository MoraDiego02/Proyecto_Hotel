
import re
from funciones_hotel import *

def main(historial=[]):
    inicio()
    dnis_ingresados = [r[2] for r in historial]
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

    precio_final, que_dia_es = gestion_reserva(hotel, piso, hab)
    checkin = registrar_checkin(que_dia_es)
    comprobante_reserva(dni, mail, piso, hab, precio_final, nombre, apellido, checkin)
    historial.append((nombre, apellido, dni, mail, telefono, piso, hab, precio_final, checkin))
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
        main(historial)
    else:
        while True:
            try:
                ver_historial = input("¿Desea ver el historial de reservas? (si/no): ")
                if not re.match(r'^(si|no)$', ver_historial, re.IGNORECASE):
                    raise ValueError
            except ValueError:
                print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
            else:
                break

        if re.match(r'^si$', ver_historial, re.IGNORECASE):
            dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
            print("\n" + "=" * 43)
            print()
            print("|     HISTORIAL DE RESERVAS DEL DÍA     |")
            print()
            print("=" * 43)
            for i, r in enumerate(historial, 1):
                print(f"  {i}. {r[0]} {r[1]}")
                print(f"     DNI:      {r[2]}")
                print(f"     Mail:     {r[3]}")
                print(f"     Teléfono: {r[4]}")
                print(f"     Piso:     {r[5]}")
                print(f"     Hab:      {r[6]}")
                print(f"     Precio:   ${r[7]:.2f}")
                print(f"     Fecha de check-in: {r[8][0]}/{r[8][1]}/{r[8][2]} ({dias[r[8][5]]})")
                print(f"     Hora de check-in:  {r[8][3]}:{r[8][4]:02d}")
                print("=" * 43)
                
    print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")
if __name__ == "__main__":
    main()