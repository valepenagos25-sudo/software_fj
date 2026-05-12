# logger.py
# Archivo encargado del registro de eventos
# y errores del sistema.


from datetime import datetime


def registrar_log(mensaje):

    """
    Guarda mensajes en el archivo logs.txt
    junto con fecha y hora.
    """

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(
            f"{datetime.now()} --> {mensaje}\n"
        )