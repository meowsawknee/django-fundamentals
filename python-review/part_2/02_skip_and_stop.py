def print_sequence() -> None:
    """
    Prints numbers from 1 to 10, skipping 5 and stopping at 8.
    """
    for number in range(1, 11):
        if number == 5:
            continue # skip 5
        elif number == 8:
            break # stop at 8
        print(number)



if __name__ == "__main__":
    print_sequence()