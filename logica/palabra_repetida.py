import re

texto: str = (
    "hoy me fui a caminar. me fui a trabajar. me fui a la, casa de mi "
    "tia".lower())

texto: str = re.sub(r"[.,;:!?¡¿'\"“”«»()\[\]{}\-_/\\|`~@#$%^&*+=<>]", "", texto)
lista: list[str] = texto.split(" ")
palabras: dict[str, int] = {}

for key in lista:
    palabras[key] = palabras.get(key, 0) + 1

print(palabras)
