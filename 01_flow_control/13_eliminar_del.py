# Ejercicio 13: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

numeros: list[int] = list(range(1, 11))
del numeros[2:5]
print(numeros)
