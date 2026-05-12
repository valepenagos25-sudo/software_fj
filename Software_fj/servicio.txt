# servicio.py
# Clases de servicios del sistema.


from abc import ABC, abstractmethod
from excepciones import ServicioError


# CLASE ABSTRACTA

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# SERVICIO 1
# RESERVA DE SALAS

class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__(
            "Reserva de Sala",
            50000
        )

        if horas <= 0:
            raise ServicioError(
                "Las horas deben ser mayores a cero."
            )

        self.horas = horas

    def calcular_costo(self):

        return self.precio_base * self.horas

    def descripcion(self):

        return (
            f"Reserva de sala por "
            f"{self.horas} horas"
        )


# SERVICIO 2
# ALQUILER DE EQUIPOS

class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__(
            "Alquiler de Equipos",
            30000
        )

        if dias <= 0:
            raise ServicioError(
                "Los días deben ser válidos."
            )

        self.dias = dias

    def calcular_costo(self):

        return self.precio_base * self.dias

    def descripcion(self):

        return (
            f"Alquiler de equipos "
            f"por {self.dias} días"
        )


# SERVICIO 3
# ASESORÍAS

class Asesoria(Servicio):

    def __init__(self, horas):

        super().__init__(
            "Asesoría Especializada",
            80000
        )

        if horas <= 0:
            raise ServicioError(
                "Las horas no son válidas."
            )

        self.horas = horas

    def calcular_costo(self):

        return self.precio_base * self.horas

    def descripcion(self):

        return (
            f"Asesoría especializada "
            f"por {self.horas} horas"
        )