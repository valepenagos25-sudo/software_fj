# utilidades.py
# Funciones auxiliares para validaciones.


import re


def validar_correo(correo):

    """
    Valida que el correo tenga
    una estructura correcta.
    """

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(patron, correo)


def validar_telefono(telefono):

    """
    Verifica que el teléfono
    tenga solo números.
    """

    return telefono.isdigit()