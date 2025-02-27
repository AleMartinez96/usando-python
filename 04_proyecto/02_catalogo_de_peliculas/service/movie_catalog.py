import os
from pathlib import Path
from domain.movie import Movie


class MovieCatalog:

    MOVIE_NAME_FILE_PAHT = "movie_name.txt"

    @classmethod
    def add_movie(cls, movie: Movie):
        with open(cls.MOVIE_NAME_FILE_PAHT, "a", encoding="utf8") as file:
            file.write(f"{movie.movie_name}\n")

    @classmethod
    def list_movie(cls):
        file_exists: Path = Path(cls.MOVIE_NAME_FILE_PAHT)
        if file_exists.exists():
            with open(cls.MOVIE_NAME_FILE_PAHT, "r", encoding="utf8") as file:
                print("Catálogo de películas".center(50, "-"))
                print(file.read())
        else:
            print(f"El archivo: {cls.MOVIE_NAME_FILE_PAHT} no existe")

    @classmethod
    def remove_file(cls):
        file: Path = Path(cls.MOVIE_NAME_FILE_PAHT)
        if file.exists():
            os.remove(cls.MOVIE_NAME_FILE_PAHT)
            print(f"Archivo elimando: {cls.MOVIE_NAME_FILE_PAHT}")
        else:
            print(f"El archivo: {cls.MOVIE_NAME_FILE_PAHT} no existe")
