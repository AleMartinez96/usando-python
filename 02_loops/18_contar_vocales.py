"""
Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".

Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de vocales encontradas es el que se debe imprimir).
"""

texto: str = "Hola mundo"
vocales: list[str] = ["a", "e", "i", "o", "u"]
cont: int = 0

for caracter in texto:
    if caracter in vocales:
        cont += 1

print(cont)
