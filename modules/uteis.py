def read_int(value: str, annoyed=False) -> int:
    """Solicita um input ao usuário até que ele forneça um número

    Args:
        value (str): Mensagem que deseja fornecer ao usuário
        annoyed (bool, optional): Retorna uma mensagem malcriado caso o usuário não forneça um número. Defaults to False

    Returns:
        int: Número digitado pelo usuário
    """
    user_input = input(value)
    while not user_input.isnumeric():
        if annoyed:
            print('Aí não, boca de leite...')
        else:
            print('Só aceitamos números...')
        user_input = input(value)
    return int(user_input)

def factorial(n: int, show=False) -> int:
    """Recursive function that calculate the factorial of a given number

    Args:
        n (int): Number witch the factorial is desired
        show (bool, optional): Prints the process. Defaults to False.
    """
    if n <= 1:
        fac = n * 1
        if show: print(f'{n} ', end ='')
        return fac
    fac = n * factorial(n - 1, show=show)
    if show: print(f'x{n} ', end='')
    return fac
