# Ejercicio 5: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

caracteres: list[str] = [
    "C",
    "o",
    "d",
    "i",
    "g",
    "o",
    " ",
    "s",
    "e",
    "c",
    "r",
    "e",
    "t",
    "o",
]

mensaje: list[str] = caracteres[7:]
print(mensaje)
