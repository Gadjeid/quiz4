from typing import Iterable, Sized, List

def element_length(words: Iterable[Sized]) -> List[int]:
    result = []
    for word in words:
        result.append(len(str(word)))
    return result

def main():
    words = ["control", "dominion", "fear"]
    lengths = element_length(words)

    print("Words: ", words)
    print("Lengths: ", lengths)

    numbers = [19, 223, 542, 299]
    lengths = element_length(numbers)

    print("\nNumbers: ", numbers)
    print("Lengths: ", lengths)

if __name__ == "__main__":
    main()