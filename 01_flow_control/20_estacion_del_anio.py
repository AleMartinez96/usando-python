"""
Se solicita proporcianar el valor de un mes (1-12) e indicar la estación del año según lo siguiente:
- meses: 1, 2, 12 -> invierno
- meses: 3, 4, 5 -> primavera
- meses: 6, 7, 8 -> verano
- meses: 9, 10, 11 -> otoño
- cualquier otro valor -> estación desconocida
"""

mes: int = int(input("Ingrese un mes del 1 al 12: "))

if mes == 1 or mes == 2 or mes == 12:
    print("estacion: invierno")
elif mes == 3 or mes == 4 or mes == 5:
    print("estacion: primavera")
elif mes == 6 or mes == 7 or mes == 8:
    print("estacion: verano")
elif mes == 9 or mes == 10 or mes == 11:
    print("estacion: otoño")
else:
    print("estacion desconocida")
