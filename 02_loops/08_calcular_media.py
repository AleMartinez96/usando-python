# Ejercicio 8: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

numeros: list[int] = [10, 20, 30, 40, 50]

suma: int = 0
for i in numeros:
    suma += i
print(f"la media es: {suma / len(numeros)}")
