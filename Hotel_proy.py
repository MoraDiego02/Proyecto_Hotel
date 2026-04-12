from funciones_hotel import filtrar_ubicaciones_por_habitacion, gestion_reserva, tipo_habitaciones

def inicio():
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)

def main():
    dni = int(input("Ingrese su DNI: "))
    while dni < 10000000 or dni > 99999999:
        print("DNI inválido. Debe tener 8 dígitos.")
        dni = int(input("Ingrese su DNI: "))
    print(f"DNI ingresado: {dni}")
    tipo_habitaciones()
    print("Elija el tipo de habitación que desea reservar:")
    habitacion = int(input("Ingrese el número de la habitación (1-3): "))
    while habitacion < 1 or habitacion > 3:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 3.")
        habitacion = int(input("Ingrese el número de la habitación (1-3): "))
    print(" ")
    print("Usted ha seleccionado la habitación ", habitacion)
    print("Elija la locacion de la habitación:")
    ubicaciones_disponibles = filtrar_ubicaciones_por_habitacion(habitacion)

    for ubicacion in ubicaciones_disponibles:
        print(f"{ubicacion['opcion']}. {ubicacion['nombre']}")

    opcion_ubicacion = int(input("Ingrese el número de la ubicación: "))
    opciones_validas = list(map(lambda u: u["opcion"], ubicaciones_disponibles))

    while opcion_ubicacion not in opciones_validas:
        opcion_ubicacion = int(input("Opción inválida. Ingrese una ubicación disponible: "))

    ubicacion_elegida = next(filter(lambda u: u["opcion"] == opcion_ubicacion, ubicaciones_disponibles))
    print(f"Usted eligió: {ubicacion_elegida['nombre']}")

    total = gestion_reserva()
    print(f"Total de la reserva: {total}")




if __name__ == "__main__":
    inicio()
    main()