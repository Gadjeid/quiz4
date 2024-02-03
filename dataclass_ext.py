from dataclasses import dataclass

@dataclass
class Movie:
    name: str
    rating: str
    price: float

    def discounted_price(self, discount_percentage: float) -> float:
        discount_amount = (discount_percentage / 100) * self.price
        return self.price - discount_amount


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

    discount_percentage = 15
    print(f"{movies[0].name} has a {discount_percentage}% discount! The discounted price is {movies[0].discounted_price(discount_percentage)}")


if __name__=="__main__":
    main()

