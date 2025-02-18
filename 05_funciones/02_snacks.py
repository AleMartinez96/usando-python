from os import system

"""
Crear un programa donde podras comprar snacks de una lista inicial.
Cada snack tiene:
    1. id
    2. nombre
    3. precio.
Para comprar un snack se debe indicar el id del snack a comprar y se agregara a una lista de productos comprados
Además se debe mostrar el ticket de venta final con el total de productos y el total de venta.
"""

snack_disponibles: list[dict[str, object]] = [
    {"id": 1, "nombre": "papas fritas", "precio": 1200},
    {"id": 2, "nombre": "gomitas", "precio": 300},
    {"id": 3, "nombre": "coca-cola", "precio": 1500},
]
mis_compras: list[dict[str, object]] = []


def agregar_compra(compra: dict[str, object]):
    mis_compras.append(compra)
    print("Nueva compra agregada")


def mostrar_snack():
    for snack in snack_disponibles:
        print(
            f"id: {snack.get("id")}, nombre: {snack.get("nombre")}, precio: {snack.get("precio")}"
        )


def mostrar_mis_compras():
    if len(mis_compras) is not 0:
        for producto in mis_compras:
            print(
                f"id: {producto.get("id")}, nombre: {producto.get("nombre")}, precio: ${producto.get("precio")}"
            )
    else:
        print("No hay datos cargados")


def imprimir_ticket():
    suma_total: float = 0
    texto: str = ""
    for producto in mis_compras:
        precio: object = producto.get("precio")
        suma_total += float(precio) if isinstance(precio, (int, float, str)) else 0
        texto += f"id: {producto.get("id")}, nombre: {producto.get("nombre")}, precio: {producto.get("precio")}\n"
    texto += f"monto total: {suma_total}$"
    return texto if suma_total != 0 else "Sin datos"


def buscar_snack(id_snack: int):
    for snack in snack_disponibles:
        if snack.get("id") == id_snack:
            return snack
    return None


while True:
    system("cls")
    opcion: int = int(
        input(
            """
            1. Comprar snack
            2. Ver snack disponibles
            3. Ver compras realizadas
            4. Salir
            Ingrese su opción: """
        )
    )
    if opcion == 1:
        print("----- REALIZANDO COMPRA -----")
        id_snack: int = int(input("Ingrese el ID del snack: "))
        compra: dict[str, object] | None = buscar_snack(id_snack)
        if compra is not None:
            agregar_compra(compra)
        else:
            print(f"No tenemos el snack con ID {id_snack}")
    elif opcion == 2:
        print("----- SNACKS DISPONIBLES -----")
        mostrar_snack()
    elif opcion == 3:
        print("----- COMPRAS REALIZADAS -----")
        mostrar_mis_compras()
    elif opcion == 4:
        print(f"----- TICKET -----\n{imprimir_ticket()}")
        print("----- QUE TENGAS UN EXCELENTE DÍA -----")
        break
    else:
        print("----- OPCIÓN INCORRECTA... INTENTE NUEVAMENTE -----")
    system("pause")
