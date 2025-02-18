"""
Se solicita crear un sistema de reservación de Hotel.
Se debe pedir la siguiente información al usuario
    - Nombre del cliente
    - Días de estadía en el Hotel
    - Cuarto con vista al mar?
El Hotel tiene las siguientes tarifas: 
    - Cuarto sin vista al mar: $150.5 por día
    - Cuarto con vista al mar: $190.5 por día

El sistema debe calcular el costo total de la estadía dependiendo si escogió un cuarto con vista al mar o no.
Además debe indicar si escogió un cuarto con vista al mar o no
"""


class Cliente:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Cuarto:
    def __init__(self, vista_al_mar: str, dias: int) -> None:
        self.vista_al_mar = vista_al_mar
        self.dias = dias


class Tarifa:
    __CON_VISTA_AL_MAR: float = 190.5
    __SIN_VISTA_AL_MAR: float = 150.5

    def __init__(self, cliente: Cliente, cuarto: Cuarto) -> None:
        self.cliente = cliente
        self.cuarto = cuarto

    def costo_total(self):
        if self.cuarto.vista_al_mar.lower() == "si":
            return self.__CON_VISTA_AL_MAR * self.cuarto.dias
        return self.__SIN_VISTA_AL_MAR * self.cuarto.dias

    def mostrar_info(self):
        return f"cliente: {self.cliente.nombre}, dias: {self.cuarto.dias}, total a pagar: {self.costo_total()}, con vista al mar?: {self.cuarto.vista_al_mar}"


cliente1: Cliente = Cliente(input("Ingrese su nombre: "))
vista_al_mar: str = input("Con vista al mar? Si/No: ")
estadia: int = int(input("Cuantos días se va a quedar?: "))
cuarto1: Cuarto = Cuarto(vista_al_mar, estadia)
tarifa: Tarifa = Tarifa(cliente1, cuarto1)
print(tarifa.mostrar_info())
