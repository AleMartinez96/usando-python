from datetime import datetime
from os import system
from alumno import Alumno
from profesor import Profesor
from materia import Materia
from votacion import Votacion
from universidad import Universidad

system("cls")

alumno1: Alumno = Alumno("maria", "perez", 21)
alumno2: Alumno = Alumno("jose", "garcia", 31)
alumno3: Alumno = Alumno("ruben", "lopez", 25)

profe1: Profesor = Profesor("silvia", "espindola", 56)
profe2: Profesor = Profesor("mario", "martinez", 35)
profe3: Profesor = Profesor("monica", "mamani", 50)

materia1: Materia = Materia(1, "poo", profe1)
materia2: Materia = Materia(2, "ami", profe3)
materia3: Materia = Materia(3, "alga", profe2)

materia1.finalizacion = datetime(2024, 2, 2)
materia2.finalizacion = datetime(2024, 3, 21)
materia3.finalizacion = datetime(2022, 2, 2)

alumno1.agregar_materia(materia1)
alumno1.agregar_materia(materia2)

alumno2.agregar_materia(materia3)
alumno2.agregar_materia(materia1)

alumno3.agregar_materia(materia3)
alumno3.agregar_materia(materia2)

profe1.agregar_materia(materia1)
profe2.agregar_materia(materia3)
profe3.agregar_materia(materia2)

universidad: Universidad = Universidad("UNSa")
universidad.agregar_alumno(alumno1)
universidad.agregar_alumno(alumno2)
universidad.agregar_alumno(alumno3)
universidad.agregar_profesor(profe1)
universidad.agregar_profesor(profe2)
universidad.agregar_profesor(profe3)

votaciones: Votacion = Votacion()
print(f"alumnos autorizados a votar:")
for alumno in votaciones.alumnos_autorizados(universidad.alumnos):
    print(alumno)

print(
    f"el porcentaje de alumnos que pueden votar son: {votaciones.porcentaje_alumnos_votantes(universidad.alumnos)}"
)

print(
    f"el porcentaje de profesores que pueden votar son: {votaciones.porcentaje_profesores_votantes(universidad.profesores)}"
)

print(
    f"cantidad de votos totales: {votaciones.votos_totales(universidad.alumnos, universidad.profesores)}"
)
