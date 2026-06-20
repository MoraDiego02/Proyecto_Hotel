import random
import re
from functools import reduce

def validar_dni(dni):
    """Devuelve True si el DNI es válido (8 dígitos), False en caso contrario."""
    if re.match(r'^\d{8}$', dni):
        return True
    return False

def calcular_precio(precio_estandar, dia_actual, metodo_pago):
    """Calcula matemáticamente el precio utilizando los parámetros fijos (sin inputs)."""
    dias_semana_laboral = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"}
    dias_fin_semana = {"Sabado", "Domingo"}
    todos_los_dias = dias_semana_laboral.union(dias_fin_semana)
    dias_descuento = {"Lunes", "Martes", "Miercoles", "Jueves"}
    
    if dia_actual in dias_descuento:
        mult_dia = 0.80
    else:
        mult_dia = 1.10
        
    mult_pago = 1.05 if metodo_pago == 1 else 1.0
    multiplicadores = [mult_dia, mult_pago]
    
    precio_final = reduce(lambda acc, m: acc * m, multiplicadores, precio_estandar)
    return precio_final

def cargar_datos():
    while True:
        try:
            nombre = input("|    Ingrese su nombre: ")
            print("-" * 40)
            if nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
                raise ValueError
        except ValueError:
            print("Nombre inválido. Solo se permiten letras y espacios.")
        else:
            break
    
    while True:
        try:
            apellido = input("|    Ingrese su apellido: ")
            print("-" * 40)
            if apellido.strip() == "":
                raise ValueError("El apellido no puede estar vacío.")
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
                raise ValueError
        except ValueError:
            print("Apellido inválido. Solo se permiten letras y espacios.") 
        else:
            break

    while True:
        try:
            dni = input("|    Ingrese su DNI: ")
            print("-" * 40)
            if not validar_dni(dni):
                raise ValueError
        except ValueError:
            print("DNI inválido. Debe tener exactamente 8 dígitos.")
        else:
            break
        
    while True:
        try:
            mail = input("|    Ingrese su correo electrónico: ")
            print("-" * 40)
            if not re.match(r'^[\w\.]+\@[\w\.]+\.[a-z]{2,3}$', mail):
                raise ValueError
        except ValueError:
            print("Correo electrónico inválido. Formato esperado: usuario@dominio.com")
        else:
            break

    while True:
        try:
            telefono = input("|    Ingrese su número de teléfono: ")
            print("-" * 40)
            if not re.match(r'^\d{10,11}$',telefono):
                raise ValueError
        except ValueError:
            print("Teléfono inválido. Debe tener entre 10 y 11 dígitos.")
        else:
            break
            
    return nombre, apellido, dni, mail, telefono    

def gestion_reserva(hotel, piso, hab):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    generar_dia = lambda: random.randint(0, 6)
    que_dia_es = generar_dia()
    datos_habitaciones = habitaciones_hotel()

    while True:
        try:
            precio_estandar = datos_habitaciones[piso][hab]["precio"]
            if precio_estandar < 0:
                raise ValueError
        except ValueError:
            print("El precio de la habitación no puede ser negativo.")
        else:
            break
    
    dias_semana_laboral = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"}
    dias_fin_semana = {"Sabado", "Domingo"}
    todos_los_dias = dias_semana_laboral.union(dias_fin_semana)
    dias_descuento = {"Lunes", "Martes", "Miercoles", "Jueves"}
    dias_aumento = todos_los_dias.difference(dias_descuento)
    dias_aumento_laboral = dias_semana_laboral.intersection(dias_aumento)
    dia_actual = dias[que_dia_es]

    if dia_actual in dias_descuento:
        mult_dia = 0.80
        print(f"Como hoy es {dia_actual}, la reserva tiene un descuento del 20%!")
    else:
        mult_dia = 1.10
        if dia_actual in dias_aumento_laboral:
            print(f"Como hoy es {dia_actual} (día laboral de alta demanda), la reserva tiene un aumento del 10%.")
        else:
            print(f"Como hoy es {dia_actual} (fin de semana), la reserva tiene un aumento del 10%.")

    print("¿Con qué desea pagar?")
    print("1 - Tarjeta (5% de recargo)")
    print("2 - Efectivo (Sin recargo)")

    while True:
        try:
            metodo_pago_str = input("Ingrese el tipo (1 o 2): ")
            if not re.match(r'^[12]$', metodo_pago_str):
                raise ValueError
            metodo_pago = int(metodo_pago_str)
        except ValueError:
            print("Opción inválida. Por favor, ingrese 1 o 2.")
        else:
            break

    precio_final = calcular_precio(precio_estandar, dia_actual, metodo_pago)

    if metodo_pago == 1:
        print("Se seleccionó tarjeta. Se aplica un 5% de recargo.")
    else:
        print("Se seleccionó efectivo. No hay recargos extra.")

    print(f"El precio final a abonar es de: ${precio_final:.2f}")
    return precio_final, que_dia_es


def pedir_habitacion():
    """Solicita el número de habitación (1-3). Controla letras y valores fuera de rango con try/except."""
    while True:
        try:
            hab = int(input("Ingrese el número de la habitación (1-8): "))
            if hab < 1 or hab > 8:
                raise ValueError
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
        else:
            break
    return hab

def pedir_piso():
    """Solicita el número de piso (1-8). Valida con regex antes de convertir a int."""
    while True:
        piso = input("Ingrese el número del piso (1-5): ")
        if not re.match(r'^[1-5]$', piso):
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        else:
            break
    return int(piso)


def Mostrar_habitaciones(matriz):
    columnas = len(matriz[0])
    print("        ", end="")
    for i in range(columnas):
        print(f"Hab {i+1}    ", end="")
    print() 
    for i in range(len(matriz)):
        print(f"Piso {i+1}  ", end="")
        for j in range(columnas):
            if matriz[i][j] == 1:
                print("  x      ", end="")
            else:
                print("         ", end="") 
        print()
    return matriz

def cargar_matriz():
    """La funcion cargar_matriz se encarga de crear una matriz de 3x3 con valores iniciales de 0, donde cada fila representa un piso y cada columna representa una habitación. Retorna la matriz creada."""
    filas = 5
    columnas = 8
    matriz = [[ "       " for _ in range(columnas)] for _ in range(filas)]
    return matriz

def comprobante_reserva(dni, email, piso, hab, precio_final, nombre, apellido, checkin):
    """Muestra un comprobante de reserva con DNI, email, piso, habitación, precio final y check-in."""
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    print("\n" + "-" * 30)
    print("--- COMPROBANTE DE RESERVA HOTEL BOUTIQUE ---")
    print(f"Nombre y apellido: {nombre} {apellido}")
    print(f"DNI: {dni}")
    print(f"Email: {email}")
    print(f"Piso: {piso}")
    print(f"Habitación: {hab}")
    print(f"Precio final a abonar: ${precio_final:.2f}")
    print()
    print(f"Fecha de check-in: {checkin[0]}/{checkin[1]}/{checkin[2]} ({dias[checkin[5]]})")
    print(f"Hora de check-in:  {checkin[3]}:{checkin[4]:02d}")
    print("-" * 30)

def inicio():
    """La función inicio se encarga de mostrar un mensaje de bienvenida al usuario al iniciar el programa."""
    print("-" * 40)
    print("|      Bienvenido a Hotel Boutique     |")
    print("-" * 40)
    
def habitaciones_hotel():
    """Devuelve un diccionario con la información de las habitaciones del hotel, organizado por piso y número de habitación."""
    habitaciones = {}
    for piso in range(1, 6):
        if piso == 1:
            info = {
                "precio": 250000,
                "tipo": "Habitación Estandar",
                "descripcion": "Habitación con vista al jardín"
            }
        elif piso == 2:
            info = {
                "precio": 300000,
                "tipo": "Habitación Superior",
                "descripcion": "Habitación con vista a la ciudad"
            }
        else:
            info = {
                "precio": 350000,
                "tipo": "Habitación Suite",
                "descripcion": "Habitación con vista al mar"
            }
        habitaciones[piso] = {hab: info.copy() for hab in range(1, 9)}
    return habitaciones

def mostrar_detalles_eleccion(habitacion_elegida):
    """Muestra por pantalla el tipo, vista y precio de la habitación elegida."""
    print("\n" + "=" * 30)
    print("   DETALLES DE LA ELECCIÓN   ")
    print("=" * 30)
    print(f"Tipo: {habitacion_elegida['tipo']}")
    print(f"Vista: {habitacion_elegida['descripcion']}")
    print(f"Precio Base: ${habitacion_elegida['precio']}")
    print("=" * 30 + "\n")

def eleccion_habitacion():
    """Solicita al usuario que elija un tipo de habitación (1-Estándar, 2-Superior, 3-Suite) y devuelve el número correspondiente. Controla entradas inválidas con try/except."""
    while True:
        try:
            tipo = int(input("Ingrese el tipo de habitación que desea elegir (1-Estándar, 2-Superior, 3-Suite): "))
            if tipo not in {1, 2, 3}:
                raise ValueError
        except ValueError:
            print("Tipo de habitación inválido. Por favor, ingrese 1, 2 o 3.")
        else:
            if tipo == 1:
                print("Estándar")
            elif tipo == 2:
                print("Superior")
            elif tipo == 3:
                print("Suite")
            break
    return tipo

def listado_habitaciones(datos_hotel):
    """Muestra un listado completo de las habitaciones del hotel, organizadas por piso, con su tipo y precio base. Controla que el diccionario tenga la estructura esperada."""
    print("Listado completo de habitaciones:")
    for piso, habitaciones in datos_hotel.items():
        primer_habitacion = habitaciones[1]
        print(f"\nPiso {piso} - {primer_habitacion['tipo']} - ${primer_habitacion['precio']}")
        print("Habitaciones: ", end="")
        for hab, detalles in habitaciones.items():
            print(f"{hab}  ", end="")
        print()
    print("\n" + "=" * 30)

def registrar_checkin(que_dia_es):
    """Genera una fecha y hora de check-in aleatoria, con el formato (día, mes, año, hora, minuto, día de la semana). El día de la semana se recibe como parámetro para que coincida con el día generado en gestion_reserva()."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = random.randint(1, 12)
    dia = random.randint(1, dias_por_mes[mes - 1])
    anio = random.randint(2024, 2026)
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    checkin = (dia, mes, anio, hora, minuto, que_dia_es)
    return checkin

def guardarReservaHistorial(reserva):
    """
    Agrega una línea nueva al archivo HotelHistorialReservas.csv con los
    datos de la reserva, sin pisar las reservas ya guardadas.
    "reserva" es la tupla (nombre, apellido, dni, mail, telefono, piso, hab, precio_final, checkin)
    """
    try:
        nombre, apellido, dni, mail, telefono, piso, hab, precio_final, checkin = reserva
        dia, mes, anio, hora, minuto, dia_semana = checkin
        with open("archivosDeTexto/HotelHistorialReservas.csv", "a") as archivo:
            archivo.write(
                f"{nombre};{apellido};{dni};{mail};{telefono};{piso};{hab};"
                f"{precio_final:.2f};{dia};{mes};{anio};{hora};{minuto};{dia_semana}\n"
            )
        print("Reserva guardada correctamente en el historial.")
    except (IOError, OSError):
        print("Error al abrir el archivo del historial.")


def leerHistorial():
    """
    Lee HotelHistorialReservas.csv línea por línea y devuelve la lista de
    reservas en el mismo formato de tupla que se usa en memoria:
    (nombre, apellido, dni, mail, telefono, piso, hab, precio_final, checkin)
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    """
    historial = []
    try:
        with open("archivosDeTexto/HotelHistorialReservas.csv", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    nombre, apellido, dni, mail, telefono, piso, hab, precio_final, dia, mes, anio, hora, minuto, dia_semana = linea.split(";")
                    checkin = (int(dia), int(mes), int(anio), int(hora), int(minuto), int(dia_semana))
                    reserva = (nombre, apellido, dni, mail, telefono, int(piso), int(hab), float(precio_final), checkin)
                    historial.append(reserva)
                except ValueError:
                    continue
    except (IOError, OSError):
        print("Error al abrir el archivo del historial.")
    return historial


def guardarEstadoHabitaciones(hotel):
    """
    Reescribe por completo HotelEstadoHabitaciones.csv con el estado actual
    de la matriz del hotel (una línea por habitación: id;piso;hab;ocupada).
    El id es "piso-hab" para identificar cada habitación de forma única.
    """
    try:
        with open("archivosDeTexto/HotelEstadoHabitaciones.csv", "w") as archivo:
            for i, fila_piso in enumerate(hotel, start=1):
                for j, celda in enumerate(fila_piso, start=1):
                    ocupada = 1 if celda == 1 else 0
                    id_hab = f"{i}-{j}"
                    archivo.write(f"{id_hab};{i};{j};{ocupada}\n")
        print("Estado de habitaciones guardado correctamente.")
    except (IOError, OSError):
        print("Error al abrir el archivo de habitaciones.")


def actualizarEstadoHabitacion(piso, hab):
    """
    Marca una única habitación como ocupada dentro de HotelEstadoHabitaciones.csv,
    primero se copia el archivo viejo a uno temporal, luego se reescribe el
    archivo original línea por línea aplicando el cambio, y por último se
    vacía el temporal.
    """
    id_hab = f"{piso}-{hab}"
    try:
        with open("archivosDeTexto/HotelEstadoHabitacionesTemp.csv", "w") as archTemporal:
            with open("archivosDeTexto/HotelEstadoHabitaciones.csv", "r") as archViejo:
                for linea in archViejo:
                    archTemporal.write(linea)
        with open("archivosDeTexto/HotelEstadoHabitacionesTemp.csv", "r") as archTemporal:
            with open("archivosDeTexto/HotelEstadoHabitaciones.csv", "w") as archActualizado:
                for linea in archTemporal:
                    if linea.split(";")[0] == id_hab:
                        _id, p, h, ocupada = linea.strip().split(";")
                        archActualizado.write(f"{_id};{p};{h};1\n")
                    else:
                        archActualizado.write(linea)
        with open("archivosDeTexto/HotelEstadoHabitacionesTemp.csv", "w"):
            pass
        print("Actualización de habitación exitosa.")
    except (IOError, OSError):
        print("Error al abrir el archivo de habitaciones.")


def leerEstadoHabitaciones():
    """
    Lee HotelEstadoHabitaciones.csv y reconstruye la matriz del hotel
    (1 = ocupada, "       " = libre, igual que cargar_matriz()).
    Si el archivo existe pero está vacío (recién creado a mano), se lo
    completa con todas las habitaciones libres antes de devolver la matriz,
    ya que actualizarEstadoHabitacion() necesita encontrar cada línea para
    poder modificarla.
    """
    filas_por_piso = {}
    try:
        with open("archivosDeTexto/HotelEstadoHabitaciones.csv", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    _id, piso, hab, ocupada = linea.split(";")
                    piso = int(piso)
                    hab = int(hab)
                    ocupada = int(ocupada)
                except ValueError:
                    continue
                filas_por_piso.setdefault(piso, {})[hab] = ocupada
    except (IOError, OSError):
        print("Error al abrir el archivo de habitaciones.")
        return cargar_matriz()

    if len(filas_por_piso) == 0:
        matriz = cargar_matriz()
        guardarEstadoHabitaciones(matriz)
        return matriz

    cant_pisos = max(filas_por_piso.keys())
    cant_habs = max(h for habs in filas_por_piso.values() for h in habs.keys())

    matriz = []
    for i in range(1, cant_pisos + 1):
        fila = []
        for j in range(1, cant_habs + 1):
            ocupada = filas_por_piso.get(i, {}).get(j, 0)
            fila.append(1 if ocupada == 1 else "       ")
        matriz.append(fila)
    return matriz
