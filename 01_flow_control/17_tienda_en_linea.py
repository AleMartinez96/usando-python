"""
Crear un sistema que ofrezca descuento dependiendo del monto de compra,
o si es miembro de la tienda.
1. Si ha comprado mas de $1000 y es miembro se aplica un descuento del 10%
2. Si solo es miembro de la tienda se aplica un descuento del 5%
3. Si no cumple con ninguna de las anteriores se aplica un descuento del 0%
"""

MONTO_COMPRA_DESC: int = 1000
DESC_MONTO_MIEMBRO: float = 0.1
DESC_MIEMBRO: float = 0.05

monto: float = float(input("Ingrese el monto de la compra realizada: "))
es_miembro: str = str(
    input("Eres miembro de la tienda?\nSi\nNo\nIngrese su opción: ")
)

descuento: float = 0

if monto >= MONTO_COMPRA_DESC and es_miembro.lower() == "si":
    descuento = monto * DESC_MONTO_MIEMBRO
    print(f"Tu compra tiene un descuento del 10%")
    print(f"Monto de la compra: {monto}")
    print(f"Descuento: {descuento}")
    print(f"Monto total a pagar: {monto - descuento}")
elif es_miembro.lower() == "si":
    descuento = monto * DESC_MIEMBRO
    print(f"Tu compra tiene un descuento del 5%")
    print(f"Monto de la compra: {monto}")
    print(f"Descuento: {descuento}")
    print(f"Monto total a pagar: {monto - descuento}")
else:
    print(f"Tu compra no tiene descuento")
    print(f"Monto de la compra: {monto}")
