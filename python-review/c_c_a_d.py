def count_characters_and_digits(text: str) -> dict[str, int]:
    """
    Counts the number of alphabetic characters (excluding spaces)
    and numeric digits in the input text.

    Args:
        text (str): The input string provided by the user.

    Returns:
        dict[str, int]: A dictionary with count of characters and digits.
                        Example: {"Characters": 6, "Numbers": 3}
    """
    char_count = 0
    digit_count = 0
    
    for char in text:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            char_count += 1
    
    return {"Characters": char_count, "Numbers": digit_count}

if __name__ == "__main__":
    user_input = input("Enter your text: ").strip()
    result = count_characters_and_digits(user_input)
    print(result)

    # TODO: Add input validation if stricter control is needed (e.g., filter emojis or symbols)
