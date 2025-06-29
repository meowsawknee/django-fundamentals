def sum_up_to(n: int) -> int:
    """Returns the sum of all integers from 0 up to and including n.
                
    Args:
        n (int): The upper limit of the range (inclusive)

    Returns:
        int: The sum of the sequence from 0 to n.
    """
    return sum(range(n + 1))

if __name__ == "__main__":
    user_input = input("Enter an integer: ").strip()

    # TODO: Add input validation to handle non-integer inputs later
    number = int(user_input)

    result = sum_up_to(number)
    print(f"Sum from 0 to {number} is: {result}")
