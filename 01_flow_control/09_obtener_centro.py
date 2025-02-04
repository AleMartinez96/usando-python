# Ejercicio 9: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

numeros: list[int] = [10, 20, 30, 40, 50]
medio: int = len(numeros) // 2
print(numeros[medio])
