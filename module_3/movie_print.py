def movie_print(movies, rating):
    for movie in movies:
        if rating == "all":
            print(f"{movie.name} - Rated {movie.rating}, Price: {movie.price}")
        else:
            if movie.rating == rating:
                print(f"{movie.name} - Rated {movie.rating}, Price: {movie.price}")
                