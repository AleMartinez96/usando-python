# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

try:
    numero: int = int(input("ingrese un numero: "))
    index: int = 1
    while index <= 10:
        print(f"{numero} x {index} = {numero * index}")
        index += 1
except ValueError:
    print("El dato ingresado no es valido")
