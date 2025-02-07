from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        self.__nombre = valor

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, valor: str):
        self.__apellido = valor

    def nombre_completo(self) -> str:
        return f"nombre: {self.__apellido} {self.__nombre}"

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int):
        self.__edad = valor

    def __str__(self) -> str:
        return (
            f"nombre: {self.__nombre}, apellido: {self.__apellido}, edad: {self.__edad}"
        )

    @abstractmethod
    def puedo_votar(self) -> bool:
        pass

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Persona):
            return (
                self.__apellido == value.__apellido
                and self.__edad == value.__edad
                and self.__nombre == value.__nombre
            )
        return False

    def __hash__(self) -> int:
        return hash((self.__apellido, self.__edad, self.__nombre))
