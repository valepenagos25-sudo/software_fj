# reserva.py
# Clase Reserva del sistema.


from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ReservaError(
                "El cliente no existe."
            )

        if servicio is None:
            raise ReservaError(
                "El servicio no existe."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    # CONFIRMAR RESERVA

    def confirmar(self):

        self.estado = "Confirmada"

   
    # CANCELAR RESERVA

    def cancelar(self):

        self.estado = "Cancelada"

    # MOSTRAR INFORMACIÓN


    def mostrar_reserva(self):

        return (
            "\n========== RESERVA ==========\n"
            f"{self.cliente.mostrar_info()}\n"
            f"Servicio: "
            f"{self.servicio.descripcion()}\n"
            f"Costo: "
            f"${self.servicio.calcular_costo()}\n"
            f"Estado: {self.estado}\n"
        )