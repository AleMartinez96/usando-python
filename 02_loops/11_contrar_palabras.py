# Ejercicio 11: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra: str = input("introduzca una letra: ")
cont: int = 0

for i in palabras:
    if i.lower().startswith(letra):
        cont += 1

print(f"la cantidad de palabras que comienzan con la letra '{letra}' son: {cont}")
