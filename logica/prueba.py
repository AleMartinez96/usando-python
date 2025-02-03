import math


def division():
    try:
        op1 = float(input("Ingrese un valor: "))
        op2 = float(input("Ingrese otro valor: "))
        valor = op1 / op2
        print("La division es: " + str(valor))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error {e}")


def calcular_raiz(numero: int) -> float:
    if numero < 0:
        raise ValueError("Error. Valor negativo")
    return math.sqrt(numero)


# division()

print(calcular_raiz(-1))
