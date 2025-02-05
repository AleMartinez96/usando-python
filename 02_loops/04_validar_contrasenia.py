# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

while True:
    password: str = input("ingrese una contraseña de al menos 8 caracteres: ")
    if len(password) >= 8:
        print("-------- contraseña valida --------")
        break
    print("-------- contraseña invalida --------")
