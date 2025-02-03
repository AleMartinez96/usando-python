texto: str = "hola"
cadena: str = ""
rango: int = len(texto) - 1
for i in range(len(texto)):
    cadena += texto[rango - i]

print(cadena)
