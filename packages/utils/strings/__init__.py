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
