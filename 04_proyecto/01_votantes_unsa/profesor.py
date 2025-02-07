from __future__ import annotations
from persona import Persona
import materia


class Profesor(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        super().__init__(nombre, apellido, edad)
        self.__cargo = "sin cargo"
        self.__materias: list[materia.Materia] = []

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, valor: str) -> None:
        self.__cargo = valor

    def agregar_materia(self, materia: materia.Materia) -> None:
        if not self.__materias.__contains__(materia):
            self.__materias.append(materia)

    def __str__(self) -> str:
        return f"{super().__str__()}, cargo: {self.__cargo}"

    def puedo_votar(self) -> bool:
        self.__cargo = "regular" if len(self.__materias) > 0 else "sin cargo"
        return self.__cargo == "regular"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Profesor):
            return super().__eq__(value) and self.__materias == value.__materias
        return False

    def __hash__(self) -> int:
        return hash((super().__hash__(), tuple(self.__materias)))
