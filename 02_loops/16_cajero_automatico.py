"""
Se les deja crear la aplicación de cajero automatico.
Las funciones principales de un cajero son:
    1. Depositar
    2. Retirar 
    3. Consultar
El saldo puede tener un valor inicial por ejemplo $1000.
"""

from os import system


saldo: float = float(input("Ingrese el saldo inicial: "))
saldo = saldo if saldo >= 0 else 0

valor: float = 0
while True:
    system("cls")
    opcion: int = int(
        input(
            """Que acción desea realizar?
            1. Depositar
            2. Retirar
            3. Consultar
            0. Salir
            Ingrese su opción: """
        )
    )
    if opcion == 1:
        valor = float(input("Cuanto desea depositar?: "))
        saldo += valor
        print(f"El deposito se realizo con exito...\nSaldo actual: {saldo}")
    elif opcion == 2:
        valor = float(input("Cuanto desea retirar?: "))
        if saldo >= valor:
            saldo -= valor
            print(f"El retiro se realizo con exito...\nSaldo actual: {saldo}")
        else:
            print("No se pudo realizar la acción: Saldo insuficiente...")
    elif opcion == 3:
        print(f"Su saldo actual es: {saldo}")
    elif opcion == 0:
        print("Saliendo del cajero. Que tenga un excelente día")
        break
    else:
        print("La opción ingresada no es valida... Ingrese nuevamente")
    system("pause")
