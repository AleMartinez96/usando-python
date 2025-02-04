# Ejercicio 8: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

numeros: list[int] = [1, 2, 3]
duplicado: list[int] = numeros + numeros
print(duplicado)
