class Movie:

    def __init__(self, movie_name: str) -> None:
        self.__movie_name = movie_name

    @property
    def movie_name(self):
        return self.__movie_name

    @movie_name.setter
    def movie_name(self, movie_name: str):
        self.__movie_name = movie_name

    def __str__(self) -> str:
        return self.__movie_name
