#Brady Heinz 1.3 Assignment 1/18/26

def countdown(bottles: int) -> None:
  
    while bottles > 1:
        next_count = bottles - 1
        next_word = "bottle" if next_count == 1 else "bottles"

        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {next_count} {next_word} of beer on the wall.\n")

        bottles -= 1

    # bottles == 1
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.\n")


def get_positive_int(prompt: str) -> int:
    """Prompt until the user enters an integer >= 1."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value >= 1:
                return value
            print("Please enter a whole number of 1 or more.")
        except ValueError:
            print("Please enter a whole number (example: 12).")


def main() -> None:
    bottles = get_positive_int("How many bottles of beer are on the wall? ")
    countdown(bottles)
    print("Don't forget to buy more beer!")


if __name__ == "__main__":
    main()
