def login_check(username: str, password: str) -> str:
    """Checks username and password against 'admin'.

    Args:
        username (str): The input username.
        password (str): The input password.

    Returns:
        str: Login status message.
    """
    if username != "admin":
        return "User not found!"
    elif password != "admin":
        return "Incorrect password!"
    else:
        return "Successful login!"



if __name__ == "__main__":
    user_input = input("Enter your username: ").strip()
    password_input = input("Enter your password: ").strip()
    result = login_check(user_input, password_input)
    print(result)
