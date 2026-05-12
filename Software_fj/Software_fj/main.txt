from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log

# Lista donde se almacenarán todas las reservas
reservas = []

# Ciclo principal del sistema
while True:

    print("\nSISTEMA SOFTWARE FJ")
    print("1. Registrar cliente y reserva")
    print("2. Mostrar reservas")
    print("3. Cancelar reserva")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Opción para registrar cliente y crear reserva
    if opcion == "1":

        try:

            print("\nREGISTRO DE CLIENTE")

            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")

            # Crear objeto cliente
            cliente = Cliente(
                nombre,
                correo,
                telefono
            )

            print("\nSERVICIOS DISPONIBLES")
            print("1. Reserva de Sala")
            print("2. Alquiler de Equipos")
            print("3. Asesoría Especializada")

            servicio_opcion = input(
                "Seleccione servicio: "
            )

            # Crear servicio dependiendo de la opción elegida
            if servicio_opcion == "1":

                horas = int(
                    input("Horas de reserva: ")
                )

                servicio = ReservaSala(horas)

            elif servicio_opcion == "2":

                dias = int(
                    input("Días de alquiler: ")
                )

                servicio = AlquilerEquipo(dias)

            elif servicio_opcion == "3":

                horas = int(
                    input("Horas de asesoría: ")
                )

                servicio = Asesoria(horas)

            else:
                raise Exception(
                    "Servicio no válido."
                )

            # Crear la reserva
            reserva = Reserva(
                cliente,
                servicio
            )

            # Confirmar reserva
            reserva.confirmar()

            # Guardar reserva en la lista
            reservas.append(reserva)

            print(
                "\nReserva creada exitosamente."
            )

            print(
                reserva.mostrar_reserva()
            )

            # Registrar evento en logs
            registrar_log(
                "Reserva creada correctamente."
            )

        # Manejo de errores
        except Exception as error:

            print(
                f"\nERROR: {error}"
            )

            registrar_log(
                f"ERROR: {error}"
            )

        # Se ejecuta si no hubo errores
        else:

            print(
                "Proceso ejecutado correctamente."
            )

        # Se ejecuta siempre
        finally:

            print(
                "Finalización del proceso."
            )

    # Mostrar todas las reservas registradas
    elif opcion == "2":

        if len(reservas) == 0:

            print(
                "\nNo existen reservas registradas."
            )

        else:

            for reserva in reservas:

                print(
                    reserva.mostrar_reserva()
                )

    # Cancelar una reserva
    elif opcion == "3":

        try:

            if len(reservas) == 0:

                raise Exception(
                    "No hay reservas registradas."
                )

            # Mostrar reservas disponibles
            for i, reserva in enumerate(reservas):

                print(
                    f"{i + 1}. "
                    f"{reserva.cliente.get_nombre()}"
                )

            posicion = int(
                input(
                    "Seleccione la reserva a cancelar: "
                )
            ) - 1

            # Cancelar reserva seleccionada
            reservas[posicion].cancelar()

            print(
                "\nReserva cancelada correctamente."
            )

            registrar_log(
                "Reserva cancelada."
            )

        except Exception as error:

            print(
                f"\nERROR: {error}"
            )

            registrar_log(
                f"ERROR: {error}"
            )

    # Salir del sistema
    elif opcion == "4":

        print(
            "\nGracias por utilizar el sistema."
        )

        break

    # Opción inválida
    else:

        print(
            "\nOpción inválida."
        )