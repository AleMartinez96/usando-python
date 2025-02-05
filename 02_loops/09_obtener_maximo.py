# Ejercicio 9: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros: list[int] = [15, 5, 25, 10, 20]
mayor: int = 0
for i in numeros:
    if mayor == 0:
        mayor = i
    elif i > mayor:
        mayor = i

print(mayor)