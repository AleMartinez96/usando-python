# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

inicio: int = 1
suma: int = 0
while inicio <= 20:
    if inicio % 2 == 0:
        suma += inicio
    inicio += 1

print(f"el resultado de sumar los numeros pares del 1 al 20 es: {suma}")