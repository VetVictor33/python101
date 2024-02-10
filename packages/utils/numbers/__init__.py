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
