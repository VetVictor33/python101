from lib.utils.colors import ANSI_colors

colors = ANSI_colors()

def line(length=30, character='-') -> str:
    """Return a line with the due length or 30

    Args:
        length (int, optional): Line length. Defaults to 30.
    """
    generated_line = character * length
    return generated_line

def generate_title(title:str, color:str, line_len=48) -> str:
    """Generate system main title

    Args:
        title (str): Desired title
        color (str): ANSI pattern text color
        line_len (int, optional): content length. Defaults to 48.

    Returns:
        str: return styled text to be displayed
    """
    generated_title = f'{color}{title:^{line_len}}{colors["end"]}'
    return generated_title

def header(title: str, line_len=48, color=colors['end']):
    """Prints system header

    Args:
        title (str): Desired title
        line_len (int, optional): Content length. Defaults to 48.
        color (str, optional): ANSI pattern text color. Defaults to none.
    """
    print(line(line_len))
    print(generate_title(title, color, 44))
    print(line(line_len))

def main_header(title:str, line_len=48):
    """Generates system main header

    Args:
        title (str): Desired title
        line_len (int, optional): Content length. Defaults to 48.
    """

    header(title, line_len, colors['green'])

def options_menu(options: dict):
    """Prints the itens of a dict of options

    Args:
        options (dict): Expects a dictionary with number as keys and options as value

    """
    for option, text in options.items():
        print(f'\033[32m{option} - \033[34m{text}\033[m')
    print(line(48))