"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""


def obtener_goal(goal: int, numeros: list[int]) -> list[int] | None:
    visto: dict[int, int] = {}
    for index, value in enumerate(numeros):
        numero: int = goal - value
        print(visto)
        if numero in visto:
            return [visto[numero], index]
        visto[value] = index
    return None


nums = [4, 5, 5, 6, 2]
print(obtener_goal(8, nums))
