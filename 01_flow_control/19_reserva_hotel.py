"""
Se solicita crear un sistema de reservación de Hotel.
Se debe pedir la siguiente información al usuario
    - Nombre del cliente
    - Días de estadía en el Hotel
    - Cuarto con vista al mar?
El Hotel tiene las siguientes tarifas: 
    - Cuarto sin vista al mar: $150.5 por día
    - Cuarto con vista al mar: $190.5 por día

El sistema debe calcular el costo total de la estadía dependiendo si escogió un cuarto
con vista al mar o no.
Además debe indicar si escogió un cuarto con vista al mar o no
"""

from os import system


system("cls")

CON_VISTA_AL_MAR: float = 190.5
SIN_VISTA_AL_MAR: float = 150.5

nombre_cliente: str = input("Cual es su nombre?: ")
estadia: int = int(input("Cuantos días se va a quedar?: "))
con_vista_al_mar: str = input("Quiere un cuarto con vista al mar (Si/No)?: ")

if con_vista_al_mar.lower() == "si":
    costo_total: float = CON_VISTA_AL_MAR * estadia
else:
    costo_total: float = SIN_VISTA_AL_MAR * estadia

print(
    f"----- RESERVA REALIZADA -----\nCliente: {nombre_cliente}\nDías de estadia: {estadia}\nHabitación con vista al mar: {con_vista_al_mar}\nTotal a pagar: {costo_total}"
)
