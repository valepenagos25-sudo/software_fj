# excepciones.py
# Archivo que contiene las excepciones
# personalizadas del sistema.


class ClienteError(Exception):
    """
    Error relacionado con clientes.
    """
    pass


class ServicioError(Exception):
    """
    Error relacionado con servicios.
    """
    pass


class ReservaError(Exception):
    """
    Error relacionado con reservas.
    """
    pass