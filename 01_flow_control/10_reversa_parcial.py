# Ejercicio 10: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

numeros: list[int] = [1, 2, 3, 4, 5, 6]
medio: int = len(numeros) // 2
inverso_parcial: list[int] = numeros[:medio][::-1] + numeros[medio:]
print(inverso_parcial)
