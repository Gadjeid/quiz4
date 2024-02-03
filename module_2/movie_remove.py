def movie_remove(movies, index):
    if index >= 0 and index < len(movies):
        del movies[index]
        print(f"Movie at index {index} removed.")
    else:
        print("Invalid index. Error removing movie")