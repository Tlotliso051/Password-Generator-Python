import random
import string


def user_length(message):
    """
    Prompt the user to input the length of the password.

    :param message: The message displayed to the user.
    :type message: str
    :return: The length of the password as an integer.
    :rtype: int
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter only numbers. Try again....")


def generate_password(length):
    """
    Generate a random password.

    :param length: The length of the password.
    :type length: int
    :return: The randomly generated password.
    :rtype: str
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(length)]
    return "".join(password)


def password_message(message, m="_"):
    """
    Display a message for the password.

    :param message: The main message.
    :type message: str
    :param m: The character used for decoration.
    :type m: str
    """
    print(message.ljust(20, "_").title())
    print(m.ljust(30, "_").title())


def print_password(password):
    """
    Print the generated password to the user.

    :param password: The generated password.
    :type password: str
    """
    password_message("Here is the password.")
    print("\n" + password)


def main():
    """
    The main function.
    """
    length_of_password = user_length("Enter length of the password: ")
    generated_password = generate_password(length_of_password)
    print_password(generated_password)


if __name__ == "__main__":
    main()
