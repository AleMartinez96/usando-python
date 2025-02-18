"""
Crea un sistema de inventarios que tenga las
siguientes opciones:
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto por ID
    4. Salir
Detalles del producto
    1. ID
    2. Nombre
    3. Precio
    4. Cantidad
"""

from os import system


lista_de_productos: list[dict[str, object]] = []


def agregar_producto():
    id_producto: int = int(input("ingrese el id del producto: "))
    nombre: str = input("ingrese el nombre: ")
    precio: float = float(input("ingrese el precio: "))
    cantidad: int = int(input("ingrese la cantidad: "))
    lista_de_productos.append(
        {"id": id_producto, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    )
    print("Nuevo producto agregado")


def mostrar_inventario():
    if len(lista_de_productos) != 0:
        for producto in lista_de_productos:
            print(
                f"id: {producto.get("id")}, nombre: {producto.get("nombre")}, precio: ${producto.get("precio")}, cantidad: {producto.get("cantidad")}"
            )
    else:
        print("No hay datos cargados")


def buscar_producto():
    if len(lista_de_productos) != 0:
        id_producto: int = int(input("Ingrese el ID del producto: "))
        buscar_producto_id(id_producto)
    else:
        print("No hay datos cargados")


def buscar_producto_id(id_producto: int):
    for producto in lista_de_productos:
        if producto.get("id") == id_producto:
            print("---------- Producto encontrado ----------")
            print(
                f"id: {producto.get("id")}, nombre: {producto.get("nombre")}, precio: ${producto.get("precio")}, cantidad: {producto.get("cantidad")}"
            )
        else:
            print("No se encontro el producto")


while True:
    system("cls")
    print("------- MENU -------")
    opcion: int = int(
        input(
            """
            1. Mostrar inventario
            2. Agregar nuevo producto
            3. Buscar producto por ID
            0. Salir
            Ingrese su opción: """
        )
    )
    if opcion == 1:
        print("------- Mostrando el inventario -------")
        mostrar_inventario()
    elif opcion == 2:
        print("------- Agregando nuevo producto -------")
        agregar_producto()
    elif opcion == 3:
        print("------- Buscando producto -------")
        buscar_producto()
    elif opcion == 0:
        print("------- Que tenga un lindo día -------")
        break
    else:
        print("------- Opción incorrecta. Ingrese nuevamente -------")
    system("pause")
