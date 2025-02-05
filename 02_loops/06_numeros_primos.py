# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

try:
    n: int = int(input("ingrese un numero: "))
    if n > 0:
        numero = 2
        while numero <= n:
            divisor: int = 2
            while (divisor < numero) and (numero % divisor != 0):
                divisor += 1
            if divisor >= numero and (numero != 0 and numero != 1):
                print(numero)
            numero += 1
    else:
        print("el numero ingresado no es positivo")
except ValueError:
    print("El dato ingresado no es valido")
