def increase(rate: float, value: float) -> float:
    """Increases the given value by the given rate

    Args:
        rate (float): Rate to increase value
        value (float): Current value

    Returns:
        float: Increased value
    """
    return value + value * rate

def decrease(rate: float, value: float) -> float:
    """Decrease the given value by the given rate

    Args:
        rate (float): Rate to decrease value
        value (float): Current value

    Returns:
        float: Decreased value
    """
    return value - value * rate

def double(value: float) -> float:
    """Double the given value

    Args:
        value (float): Value to be doubled

    Returns:
        float: Doubled value
    """
    return value * 2

def half(value: float) -> float:
    """Cut the value in halt

    Args:
        value (float): Value to be halved

    Returns:
        float: Halved value
    """
    return value / 2

def convert_to_currency(value:float, currency='R$') -> str:
    """Return a value formatted to the given currency or R$

    Args:
        value (float): Value to be formatted
        currency (str, optional): Currency. Defaults to 'R$'.

    Returns:
        str: Formatted value
    """
    return f'{currency}{value:.2f}'.replace('.', ',')