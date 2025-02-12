"""
Sea el mensaje codificado: 
†‡¡4>myd4y m4yd4y*z! ¿H$$··0‡‡l4#? ¿hy>4 &%4··lg*6u13n *l4h1*q? ¡*¡*¡N3c3%5170 4yud4*x!*#║¤

Convierte números a letras según:
0 -> o
1 -> i
3 -> e
4 -> a
5 -> s
7 -> t
Si encuentras el símbolo >, intercambia la letra que está a su izquierda con la de la derecha.
Si encuentras el símbolo *, elimina la letra que está a su derecha.
Elimina los símbolos > y * después de haberlos evaluado.
Elimina cualquier símbolo que no sea letra, número, ¿?!¡, o espacio.
¡Las letras con acento hay que mantenerlas!
El mensaje original debe contener información vital de la misión.
"""

import re


def traducir_mensaje(mensaje: str):
    caracteres: list[str] = list(mensaje)
    pattern: re.Pattern[str] = re.compile(r"[a-zA-Zá-úÁ-Ú\d\s¿?!¡]")

    i: int = 0
    while i < len(caracteres):
        valor: str = caracteres[i]
        if valor.isdigit() and int(valor) in palabras_map:
            caracteres[i] = palabras_map[int(valor)]
        elif valor == ">":
            cambiar_posicion(caracteres, i)
            i -= 1
        elif valor == "*":
            caracteres.pop(i + 1)
            caracteres.pop(i)
            i -= 2
        elif not pattern.match(valor):
            caracteres.pop(i)
            i -= 1
        i += 1
    return "".join(caracteres)


def cambiar_posicion(caracteres: list[str], index: int):
    izq: str = caracteres[index - 1]
    der: str = caracteres[index + 1]
    izq = palabras_map[int(izq)] if izq.isdigit() and int(izq) in palabras_map else izq
    der = palabras_map[int(der)] if der.isdigit() and int(der) in palabras_map else der
    caracteres[index - 1] = der
    caracteres[index + 1] = izq
    caracteres.pop(index)


palabras_map: dict[int, str] = {0: "o", 1: "i", 3: "e", 4: "a", 5: "s", 7: "t"}

mensaje: str = (
    "†‡¡4>myd4y m4yd4y*z! ¿H$$··0‡‡l4#? ¿hy>4 &%4··lg*6u13n *l4h1*q? ¡*¡*¡N3c3%5170 4yud4*x!*#║¤"
)

print(traducir_mensaje(mensaje))
