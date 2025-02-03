from math import pi, tan


# class Poligono:

#     def area(self):
#         pass

#     def print_area(self):
#         pass


# class Triangulo(Poligono):

#     def area(self):
#         return 0


def area_poligono(n: float, l: float) -> float:
    area: float = n * l**2 / (4 * tan(pi / n))
    return area


n = 6
l = 10
resultado = area_poligono(n, l)
print(resultado)
