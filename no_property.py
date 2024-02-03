class Game:
    def __init__(self, title, genre, publisher):
        self._title = title
        self._genre = genre
        self._publisher = publisher

    def get_title(self):
        return self._title, self._genre, self._publisher
    
    def set_title(self, new_title, genre, publisher):
        self._title = new_title
        self._genre = genre
        self._publisher = publisher

def main():
    games = [
        Game("Tekken 7", "Fighting Game", "Bandai Namco Studios & Arika"),
        Game("Persona 3 FES", "Role-playing Game", "Atlus")
    ]
    print("Game: ", games[0].get_title())
    print("Game: ", games[1].get_title())

    games[1].set_title("Persoan 3 Reload", "Role-playing Game", "Bandai Namco Studios & Arika")
    games[0].set_title("Tekken 8", "Fighting Game", "Atlus")

    print("Game: ", games[0].get_title())
    print("Game: ", games[1].get_title())

if __name__ == "__main__":
    main()
