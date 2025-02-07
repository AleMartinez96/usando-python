from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from profesor import Profesor
    from alumno import Alumno


class Votacion:
    def __init__(self) -> None:
        pass

    def alumnos_autorizados(self, alumnos: list["Alumno"]) -> list["Alumno"]:
        return [alumno for alumno in alumnos if alumno.puedo_votar()]

    def profesores_autorizados(self, profesores: list["Profesor"]) -> list["Profesor"]:
        return [profesor for profesor in profesores if profesor.puedo_votar()]

    def porcentaje_alumnos_votantes(self, alumnos: list["Alumno"]) -> float:
        self.autorizados: int = len(self.alumnos_autorizados(alumnos))
        self.total_alumnos: int = len(alumnos)
        return self.autorizados / self.total_alumnos

    def porcentaje_profesores_votantes(self, profesores: list["Profesor"]) -> float:
        self.autorizados: int = len(self.profesores_autorizados(profesores))
        self.total_profesores: int = len(profesores)
        return self.autorizados / self.total_profesores

    def votos_alumnos(self, alumnos: list["Alumno"]) -> int:
        return len(self.alumnos_autorizados(alumnos))

    def votos_profesores(self, profesores: list["Profesor"]) -> int:
        return len(profesores) * 3

    def votos_totales(
        self, alumnos: list["Alumno"], profesores: list["Profesor"]
    ) -> int:
        return self.votos_alumnos(alumnos) + self.votos_profesores(profesores)
