# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

from os import system


system("cls")

numeros: list[int] = [5, 2, 8, 1, 9, 4, 2]
print("desordenado", numeros)
numeros.sort()
print("ordenado", numeros)

print(f"el numero 2 aparece {numeros.count(2)} veces")

print(f"el numero 7 esta en la lista? {7 in numeros}")
