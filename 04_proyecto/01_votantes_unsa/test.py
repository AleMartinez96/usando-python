from os import system
from datetime import datetime
from alumno import Alumno
from profesor import Profesor
from materia import Materia
from votacion import Votacion
from universidad import Universidad

system("cls")

# Crear instancias de alumnos
alumno1: Alumno = Alumno("maria", "perez", 21)
alumno2: Alumno = Alumno("jose", "garcia", 31)
alumno3: Alumno = Alumno("ruben", "lopez", 25)

# Crear instancias de profesores
profe1: Profesor = Profesor("silvia", "espindola", 56)
profe2: Profesor = Profesor("mario", "martinez", 35)
profe3: Profesor = Profesor("monica", "mamani", 50)

# Crear materias y asignar responsables
materia1: Materia = Materia(1, "poo", profe1)
materia2: Materia = Materia(2, "ami", profe3)
materia3: Materia = Materia(3, "alga", profe2)

# Configurar fechas de finalización
materia1.finalizacion = datetime(2024, 2, 2)
materia2.finalizacion = datetime(2024, 3, 21)
materia3.finalizacion = datetime(2022, 2, 2)

# Asignar materias a alumnos
alumno1.agregar_materia(materia1)
alumno1.agregar_materia(materia2)
alumno2.agregar_materia(materia3)
alumno2.agregar_materia(materia1)
alumno3.agregar_materia(materia3)
alumno3.agregar_materia(materia2)

# Asignar materias a profesores
profe1.agregar_materia(materia1)
profe2.agregar_materia(materia3)
profe3.agregar_materia(materia2)

# Crear la universidad y registrar a todas las personas
universidad: Universidad = Universidad("UNSa")
universidad.agregar_persona(alumno1)
universidad.agregar_persona(alumno2)
universidad.agregar_persona(alumno3)
universidad.agregar_persona(profe1)
universidad.agregar_persona(profe2)
universidad.agregar_persona(profe3)

# Crear la votación
votacion: Votacion = Votacion()

print("Alumnos autorizados a votar:")
for alumno in votacion.alumnos_autorizados(universidad.personas):
    print(alumno)

print(
    f"El porcentaje de alumnos que pueden votar es: {votacion.porcentaje_alumnos_votantes(universidad.personas)}"
)
print(
    f"El porcentaje de profesores que pueden votar es: {votacion.porcentaje_profesores_votantes(universidad.personas)}"
)
print(f"Cantidad de votos totales: {votacion.votos_totales(universidad.personas)}")
