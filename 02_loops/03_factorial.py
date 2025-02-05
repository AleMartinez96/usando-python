# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.


try:
    numero: int = int(input("ingrese un numero positivo: "))
    resultado: int = 1
    aux: int = numero
    if numero > 0:
        while numero > 0:
            resultado *= numero
            numero -= 1
        print(f"el factorial de {aux} es {resultado}")
    elif numero == 0:
        print(f"el factorial de {aux} es {1}")
    else:
        print("el numero ingresado no es positivo")
except ValueError:
    print("el dato ingresado es invalido")
