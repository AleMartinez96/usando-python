# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

try:
    anio: int = int(input("Ingrese un año: "))
    if anio <= 0:
        print("el año debe ser mayor a cero")
    elif (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"el año {anio} es bisiesto")
    else:
        print(f"el año {anio} no es bisiesto")
except ValueError:
    print("el valor ingresado no valido")
