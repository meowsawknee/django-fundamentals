import random


def odd_or_even() -> str:
    """
    Generates a random number and returns whether it is odd or even.

    Returns:
        str: "odd" if the number is odd, "even" if it is even.
    """
    number = random.randint(1, 100) # Generates a number between 1 and 100
    return "odd" if number % 2 != 0 else "even"

if __name__ == "__main__":
    odd_or_even()
