def ANSI_colors() -> object:
    """Return an object with color names as keys  and the the ANSI colors as values

    Returns:
        str: ANSI pattern color
    """
    colors = {
        'end' : '\033[m',
        'white' : '\033[0;30;40m',
        'red' : '\033[0;31;40m',
        'green' : '\033[0;32;40m',
        'yellow' : '\033[0;33;40m',
        'blue' : '\033[0;34;40m',
        'magenta' : '\033[0;35;40m',
        'ciano' : '\033[0;36;40m',
        'gray' : '\033[0;37;40m',
    }

    return colors

def paint_text(text: str, color: str):
    """Paints a text with the given color if available

    Args:
        text (str): any text
        color (str): available colors: ANSI colors, ex: 'red'

    Returns:
        _type_: Painted text if color available, else return untouched text
    """
    colors = ANSI_colors()
    if color in colors:
        return f'{colors[color]}{text}{colors["end"]}'
    return text