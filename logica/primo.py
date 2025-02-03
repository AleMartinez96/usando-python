def is_primo(numero: int) -> bool:
    divisor: int = 2
    while (divisor < numero) and (numero % divisor != 0):
        divisor += 1
    return divisor >= numero and (numero != 0 and numero != 1)


lista: list[int] = []
for i in range(101):
    if is_primo(i):
        lista.append(i)

print(lista)


def primo(num: int):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for num in range(1, 10):
    if primo(num):
        print(num)
