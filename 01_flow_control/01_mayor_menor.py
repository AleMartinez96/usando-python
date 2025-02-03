# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

valor1: str = input("Ingrese el primer numero: ")
valor2: str = input("Ingrese el siguiente numero: ")

if not valor1.isnumeric() or not valor2.isnumeric():
    print("los datos ingresados no son validos")
else:
    numero1: int = int(valor1)
    numero2: int = int(valor2)
    if numero1 > numero2:
        print(f"{numero1} es mayor a {numero2}")
    elif numero1 == numero2:
        print(f"{numero1} es igual a {numero2}")
    else:
        print(f"{numero1} es menor a {numero2}")
