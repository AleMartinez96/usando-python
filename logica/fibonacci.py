def sucesion_fibonacci(numero: int) -> list[int]:
    lista: list[int] = []
    if numero > 0:
        a: int
        b: int = 0
        c: int = 1
        for _ in range(numero):
            a = b
            b = a + c
            c = a
            lista.append(a)
    return lista


def sucesion_recursiva(numero: int) -> int:
    if numero < 2:
        return numero
    return sucesion_recursiva(numero - 1) + sucesion_recursiva(numero - 2)


for i in range(12):
    print(sucesion_recursiva(i), i)
