import random


def odd_or_even(number: int | None = None) -> str:
    """Determine whether a number is odd or even.
    If no number is provided, generates a random number between 1 and 100.

    Args:
        number (int | None, optional): The number to check. If none, a random number will be generated.

    Returns:
        str: "odd" if the number is odd, "even" if the number is even.
    """
    if number is None:
        number = random.randint(1, 100)
        print(f"Generated number: {number}")
    return "odd" if number % 2 != 0 else "even"

if __name__ == "__main__":
    user_input = input("Enter a number (or press Enter to generate randomly): ").strip()
    if user_input.isdigit():
        result = odd_or_even(int(user_input))
    else:
        result = odd_or_even()
    print(result)

# TODO: Add input validation to handle non-integer or invalid inputs without crashing.
