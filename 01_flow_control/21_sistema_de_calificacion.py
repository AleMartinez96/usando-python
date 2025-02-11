"""
Crear un programa para convertir una calificación numérica (0-10) a una letra (A-F)
- Si es >= 9 -> A
- Si es >= 8 y < 9 -> B
- Si es >= 7 y < 8 -> C 
- Si es >= 6 y < 7 -> D
- Si es >= 0 y < 6 -> F
- En otros casos -> valor desconocido
"""

calificacion: int = int(input("Ingrese su calificación: "))

if calificacion >= 9:
    print("Tu calificación es: A")
elif calificacion >= 8 and calificacion < 9:
    print("Tu calificación es: B")
elif calificacion >= 7 and calificacion < 8:
    print("Tu calificación es: C")
elif calificacion >= 6 and calificacion < 7:
    print("Tu calificación es: D")
elif calificacion >= 0 and calificacion < 6:
    print("Tu calificación es: F")
else:
    print("Valor desconocido")
