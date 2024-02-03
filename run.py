from dataclasses import dataclass
from module_1 import movie_count as count
from module_2 import movie_remove as mov_del
from module_3 import movie_print as mov_print


@dataclass
class Movie:
    name: str
    rating: str
    price: float

def main():
    movies=[
        Movie("Thor: Love and Thunder", "PG-13", 15),
        Movie("Spider-Man: No Way Home", "PG-13", 14),
        Movie("Smile", "R", 17)
    ]
    movies.append(Movie("Barbarian", "R", 20))
    print(movies[2])

    highest_price=max(movies, key=lambda p:p.price)
    print(f"The most expensive movie is {highest_price}")

    movies[3].price-=1
    print(f"updated price of {movies[3].name} is {movies[3].price} dollars")

    print(f"There are {count.movie_count(movies)} movies logged")
    print("\nMovies:")
    mov_print.movie_print(movies, "all")

    mov_del.movie_remove(movies, 2)

    print("\nMovies rated R:")
    mov_print.movie_print(movies, "R")

    print("\nMovies:")
    mov_print.movie_print(movies, "all")

if __name__=="__main__":
    main()

