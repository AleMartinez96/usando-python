# Ejercicio 11: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

numeros: list[int] = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.insert(2, 10)
numeros[0] = 0

print(numeros)
