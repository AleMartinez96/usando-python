from os import system

from domain.movie import Movie
from service.movie_catalog import MovieCatalog as catalog

while True:
    system("cls")
    try:
        option: int = int(
            input(
            """
            1. Agregar película
            2. Listar películas
            3. Eliminar archivo
            4. Salir
            Ingrese su opción: """
            )
        )
        if option == 1:
            movie = Movie(input("Ingrese el nombre de la película: "))
            catalog.add_movie(movie)
            print("Película agregada correctamente")
        elif option == 2:
            print("Listando películas")
            catalog.list_movie()
        elif option == 3:
            catalog.remove_file()
        elif option == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción incorrecta. Ingrese nuevamente")
    except ValueError as e:
        print(f"Error: {e}. Solo se admiten números")
    system("pause")
