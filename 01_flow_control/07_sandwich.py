# Ejercicio 7: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan_arriba: list[str] = ["pan arriba"]
ingredientes: list[str] = ["jamon", "queso", "tomate"]
pan_abajo: list[str] = ["pan abajo"]

sandwich: list[str] = pan_arriba + ingredientes + pan_abajo
print(sandwich)
