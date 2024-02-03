import argparse

def argparse_func() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='Enter a name',dest='name',type=str)
    parser.add_argument(help='Enter your age',dest='age',type=int)
    parser.add_argument(help='Enter any decimal (ex. 3.14)',dest='fav_dec',type=float)

    args = parser.parse_args()

    name = args.name
    age = args.age
    fav_dec = args.fav_dec

    print("Name: ", name)
    print("Age: ", age)
    print("Favorite Decimal: ", fav_dec)

argparse_func()