def conversion_base(numero: int, base: int) -> str:
    conversion: str = ""
    while numero > 0:
        resto: int = numero % base
        numero //= base
        conversion += str(resto)
    return conversion[::-1]


print(conversion_base(10, 2))
