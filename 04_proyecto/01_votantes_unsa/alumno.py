from persona import Persona
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from materia import Materia


class Alumno(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        super().__init__(nombre, apellido, edad)
        self.__materias: list["Materia"] = []

    def agregar_materia(self, materia: "Materia") -> None:
        if not self.__materias.__contains__(materia):
            self.__materias.append(materia)

    def mostrar_materias(self) -> None:
        for materia in self.__materias:
            print(materia)

    def puedo_votar(self) -> bool:
        cont: int = 0
        for materia in self.__materias:
            if materia.ha_pasado_un_anio():
                cont += 1
        return cont >= 2

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Alumno):
            return super().__eq__(value) and self.__materias == value.__materias
        return False

    def __hash__(self) -> int:
        return hash((super().__hash__(), self.__materias))
