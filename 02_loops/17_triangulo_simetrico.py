"""
Crear un programa que dibuje un triangulo simetrico
"""

filas: int = int(input("Ingrese el número de filas: "))
for i in range(1, filas + 1):
    print(" " * (filas - i), "*" * (2 * i - 1))
