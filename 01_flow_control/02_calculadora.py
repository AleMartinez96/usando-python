# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

try:
    numero1: float = float(input("Ingrese el primer numero: "))
    numero2: float = float(input("Ingrese el siguiente numero: "))
    operacion: str = input(
        """
                       1. suma
                       2. resta
                       3. multiplicacion
                       4. division
                       Ingrese su opcion: 
                       """
    )
    if operacion == "1":
        print(f"el resultado de sumar {numero1} + {numero2} = {numero1 + numero2}")
    elif operacion == "2":
        print(f"el resultado de restar {numero1} - {numero2} = {numero1 - numero2}")
    elif operacion == "3":
        print(
            f"el resultado de multiplicar {numero1} * {numero2} = {numero1 * numero2}"
        )
    elif operacion == "4":
        if numero2 != 0:
            print(
                f"el resultado de dividir {numero1} / {numero2} = {numero1 / numero2}"
            )
        else:
            print("no se puede realizar la division por 0")
except ValueError:
    print("los datos ingresados no son validos")
