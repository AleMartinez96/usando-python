"""
Crear un programa para determinar el costo de envio de un paquete según el destino (nacional-internacional)
y el peso del paquete.
- costo de la tarifa: nacional $10 x kilo. internacional $20 x kilo
El programa debe solicitar 2 valores:
- El destino
- Peso del paquete
Al final se debe imprimir el costo de envío del paquete.
"""

TARIFA_NACIONAL: float = 10
TARIFA_INTERNACIONAL: float = 20

costo_total: float = 0
destino: str = input("cual es el destino? (Nac o Int)?: ")
if destino.lower() == "nac" or destino.lower() == "int":
    peso_paquete: float = float(input("Ingrese el peso del paquete: "))
    tarifa: float = (
        TARIFA_NACIONAL if destino.lower() == "nac" else TARIFA_INTERNACIONAL
    )
    print(f"Destino: {destino}\nCosto de envío: {peso_paquete * tarifa}")
else:
    print("Destino desconocido")
