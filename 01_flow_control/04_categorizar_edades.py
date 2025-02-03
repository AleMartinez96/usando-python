# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

try:
    edad: int = int(input("Ingrese una edad: "))
    if edad >= 0 and edad <= 2:
        print("bebé")
    elif edad >= 3 and edad <= 12:
        print("niño")
    elif edad >= 13 and edad <= 17:
        print("adolecente")
    elif edad >= 18 and edad <= 64:
        print("adulto")
    elif edad >= 65:
        print("adulto mayor")
    else:
        print("la edad no puede ser menor a cero")
except ValueError:
    print("el dato ingresado no es valido")
