
# cliente.py
# Clase Cliente del sistema.

from excepciones import ClienteError
from utilidades import validar_correo
from utilidades import validar_telefono


class Cliente:

    def __init__(self, nombre, correo, telefono):

        """
        Constructor de la clase Cliente.
        """

        # Validación del nombre
        if not nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacío."
            )

        # Validación del correo
        if not validar_correo(correo):
            raise ClienteError(
                "Correo electrónico inválido."
            )

        # Validación del teléfono
        if not validar_telefono(telefono):
            raise ClienteError(
                "El teléfono solo debe contener números."
            )

        if len(telefono) < 7:
            raise ClienteError(
                "El teléfono es demasiado corto."
            )

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    
    # MÉTODOS GETTERS
   

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

  
    # REPRESENTACIÓN DEL CLIENTE
   

    def mostrar_info(self):

        return (
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )