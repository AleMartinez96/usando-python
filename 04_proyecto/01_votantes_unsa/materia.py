from __future__ import annotations
import calendar
from datetime import datetime
import profesor


class Materia:
    def __init__(self, id: int, nombre: str, responsable: profesor.Profesor) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__responsable = responsable
        self.__finalizacion: datetime = datetime.now()

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        self.__id = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def responsable(self) -> profesor.Profesor:
        return self.__responsable

    @responsable.setter
    def responsable(self, valor: profesor.Profesor) -> None:
        self.__responsable = valor

    @property
    def finalizacion(self) -> datetime:
        return self.__finalizacion

    @finalizacion.setter
    def finalizacion(self, valor: datetime) -> None:
        self.__finalizacion = valor

    def ha_pasado_un_anio(self) -> bool:
        self.fecha: datetime = datetime.now()
        self.dias_anio: int = 366 if calendar.isleap(self.fecha.year) else 365
        return abs(self.finalizacion - self.fecha).days >= self.dias_anio

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Materia):
            return (
                self.__nombre == value.__nombre
                and self.__responsable == value.__responsable
                and self.__id == value.__id
            )
        return False

    def __hash__(self) -> int:
        return hash((self.__nombre, self.__responsable, self.__id))

    def __str__(self) -> str:
        return f"id: {self.__id}, nombre: {self.__nombre}, responsable: {self.__responsable.nombre_completo()}"
