from __future__ import annotations
import persona
import alumno
import profesor


class Votacion:
    def __init__(self) -> None:
        pass

    def alumnos_autorizados(
        self, personas: list[persona.Persona]
    ) -> list[alumno.Alumno]:
        return [
            persona
            for persona in personas
            if isinstance(persona, alumno.Alumno) and persona.puedo_votar()
        ]

    def profesores_autorizados(
        self, personas: list[persona.Persona]
    ) -> list[profesor.Profesor]:
        return [
            persona
            for persona in personas
            if isinstance(persona, profesor.Profesor) and persona.puedo_votar()
        ]

    def porcentaje_alumnos_votantes(self, personas: list[persona.Persona]) -> float:
        self.autorizados: int = len(self.alumnos_autorizados(personas))
        self.total_alumnos: int = sum(
            1 for persona in personas if isinstance(persona, alumno.Alumno)
        )
        return self.autorizados / self.total_alumnos if self.total_alumnos != 0 else 0

    def porcentaje_profesores_votantes(self, personas: list[persona.Persona]) -> float:
        self.autorizados: int = len(self.profesores_autorizados(personas))
        self.total_profesores: int = sum(
            1 for persona in personas if isinstance(persona, profesor.Profesor)
        )
        return (
            self.autorizados / self.total_profesores
            if self.total_profesores != 0
            else 0
        )

    def votos_alumnos(self, personas: list[persona.Persona]) -> int:
        return len(self.alumnos_autorizados(personas))

    def votos_profesores(self, personas: list[persona.Persona]) -> int:
        return len(self.profesores_autorizados(personas)) * 3

    def votos_totales(self, personas: list[persona.Persona]) -> int:
        return self.votos_alumnos(personas) + self.votos_profesores(personas)
