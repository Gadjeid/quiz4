from collections.abc import Iterable

class Game:
    def __init__(self, title, genre, publisher):
        self._title = title
        self._genre = genre
        self._publisher = publisher

    @property
    def title(self):
        return self._title, self._genre, self._publisher
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, tuple):
            if len(new_title) == 3:
                val1, val2, val3 = new_title
            elif len(new_title) == 2:
                val1, val2 = new_title
                val3 = "Unknown Publisher"
            else:
                raise ValueError("Tuple must have 2 or 3 elements (title, genre[, publisher])")
        else:
            val1 = new_title
            val2 = "Unknown Genre"
            val3 = "Unknown Publisher"
        self._title = val1
        self._genre = val2
        self._publisher = val3

def main():
    games = [
        Game("Tekken 7", "Fighting Game", "Bandai Namco Studios & Arika"),
        Game("Persona 3 FES", "Role-playing Game", "Atlus")
    ]
    print("Game: ", games[0].title)
    print("Game: ", games[1].title)

    games[1].title = ("Persoan 3 Reload", "Role-playing Game")
    games[0].title = ("Tekken 8", "Fighting Game")

    print("Game: ", games[0].title)
    print("Game: ", games[1].title)

    games[1].title = ("Persoan 3 Reload", "Role-playing Game", "Bandai Namco Studios & Arika")
    games[0].title = ("Tekken 8", "Fighting Game", "Atlus")

    print("Game: ", games[0].title)
    print("Game: ", games[1].title)

if __name__ == "__main__":
    main()
