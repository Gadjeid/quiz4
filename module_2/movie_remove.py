def movie_remove(movies, index):
    if index >= 0 and index < len(movies):
        del movies[index]
        print(f"Movie at index {index} removed.")
    else:
        print(f"Invalid index. Error removing movie at {index}")