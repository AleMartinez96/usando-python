"""
Considerando que estamos dentro de un sistema bancario, se solicita preguntar al usuario
si desea continuar dentro del sistema.
1. Si deseamos continuar dentro del sistema imprimir "continuamos dentro del sistema"
2. De lo contrario imprimir "saliendo del sistema"
"""

pregunta: str = input(
    "Desea continuar dentro del sistema?\nSi\nNo\nIngrese su opción: "
)

if pregunta.lower() == "si":
    print("continuamos dentro del sistema")
else:
    print("saliendo del sistema")
