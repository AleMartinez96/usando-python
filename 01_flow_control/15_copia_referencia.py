# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original: list[int] = [1, 2, 3]
copia_1: list[int] = original[:]
copia_2: list[int] = original.copy()
referencia: list[int] = original

referencia[0] = 10

print(original)
print(copia_1)
print(copia_2)
print(referencia)
