from __future__ import annotations
import persona


class Universidad:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__personas: list[persona.Persona] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def personas(self) -> list[persona.Persona]:
        return self.__personas

    def agregar_persona(self, persona: persona.Persona) -> None:
        if not self.__personas.__contains__(persona):
            self.__personas.append(persona)
