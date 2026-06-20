import re
from funciones_hotel import *

def main():
    inicio()

    # Se recupera el estado persistido en los archivos de texto una sola
    # vez al iniciar el programa, para que los datos no se pierdan aunque
    # el programa se cierre y se vuelva a ejecutar.
    historial = leerHistorial()
    dnis_ingresados = []
    mails_ingresados = []
    for reserva in historial:
        dnis_ingresados.append(reserva[2])
        mails_ingresados.append(reserva[3])
    hotel = leerEstadoHabitaciones()

    # El sistema permite cargar varias reservas en la misma ejecución
    # repitiendo este bloque con un while en vez de volver a llamar a main().
    while True:
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

        #Se avisa si el mail ya fue registrado antes, pero no bloquea la reserva
        if mail in mails_ingresados:
            print("Aviso: este correo electrónico ya fue utilizado en otra reserva.")
        mails_ingresados.append(mail)

        datos_hotel = habitaciones_hotel()
        print(" ")
        listado_habitaciones(datos_hotel)
        print(" ")

        #Se controla que la habitación elegida no esté ya ocupada (según el archivo guardado)
        while True:
            piso = pedir_piso()
            hab = pedir_habitacion()
            try:
                if hotel[piso-1][hab-1] == 1:
                    raise ValueError
            except ValueError:
                print(f"La habitación {hab} del piso {piso} ya está ocupada. Elija otra.")
            else:
                break

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

        nueva_reserva = (nombre, apellido, dni, mail, telefono, piso, hab, precio_final, checkin)
        historial.append(nueva_reserva)

        # Persistencia automática en archivos de texto: se guarda apenas se
        # concreta la reserva, sin esperar a que el usuario lo pida explícitamente.
        guardarReservaHistorial(nueva_reserva)
        actualizarEstadoHabitacion(piso, hab)

        while True:
            try:
                volver_a_reservar = input("¿Desea realizar otra reserva? (si/no): ")
                if not re.match(r'^(si|no)$', volver_a_reservar, re.IGNORECASE):
                    raise ValueError
            except ValueError:
                print("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
            else:
                break

        if re.match(r'^no$', volver_a_reservar, re.IGNORECASE):
            break

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
        for i, reserva in enumerate(historial, 1):
            print(f"  {i}. {reserva[0]} {reserva[1]}")
            print(f"     DNI:      {reserva[2]}")
            print(f"     Mail:     {reserva[3]}")
            print(f"     Teléfono: {reserva[4]}")
            print(f"     Piso:     {reserva[5]}")
            print(f"     Hab:      {reserva[6]}")
            print(f"     Precio:   ${reserva[7]:.2f}")
            print(f"     Fecha de check-in: {reserva[8][0]}/{reserva[8][1]}/{reserva[8][2]} ({dias[reserva[8][5]]})")
            print(f"     Hora de check-in:  {reserva[8][3]}:{reserva[8][4]:02d}")
            print("=" * 43)

    print("Gracias por utilizar nuestro sistema de reservas. ¡Hasta luego!")

if __name__ == "__main__":
    main()