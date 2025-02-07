from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from profesor import Profesor
    from alumno import Alumno


class Universidad:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__profesores: list["Profesor"] = []
        self.__alumnos: list["Alumno"] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def alumnos(self) -> list["Alumno"]:
        return self.__alumnos

    @property
    def profesores(self) -> list["Profesor"]:
        return self.__profesores

    def agregar_alumno(self, alumno: "Alumno") -> None:
        if not self.__alumnos.__contains__(alumno):
            self.__alumnos.append(alumno)

    def agregar_profesor(self, profesor: "Profesor") -> None:
        if not self.__profesores.__contains__(profesor):
            self.__profesores.append(profesor)
