import math
def read_int(message:str, range: tuple = (-math.inf, math.inf), error_message='Valor inválido. Tente novamente'):
    """Reads user input until it's a valid integer

    Args:
        message (str): Message to display to user
        range (tuple, optional): Range of valid integers. Defaults to (-math.inf, math.inf).
        error_message (str, optional): Show when user inout a not integer. Defaults to 'Valor inválido. Tente novamente' red colored.

    Returns:
        _type_: returns an integer inputted by user
    """
    while True:
        try:
            n = int(input(message))
            if range[0] > n or n > range[1]:
                raise ValueError()
            return n
        except ValueError:
            print(f'\033[31m{error_message}\033[m')
            continue

def read_str(message:str, error_message='Valor inválido. Tente novamente'):
    """Reads user input until it's a valid string, empty string is considered invalid

    Args:
        message (str): Message to display to user
        error_message (str, optional): Show when user fails to input a valid string. Defaults to 'Valor inválido. Tente novamente' red colored.

    Returns:
        _type_: striped string
    """
    while True:
        try:
            n = str(input(message)).strip()
            if not n:
                raise ValueError()
            return n
        except ValueError:
            print(f'\033[31m{error_message}\033[m')
            continue
