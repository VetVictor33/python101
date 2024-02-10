# Printa a doc:
# print(input.__doc__)
# help(print)

# Docstring
def soma(a, b, c=0):
    """Soma a com b
    Args:
        a (int): Primeiro valor
        b (int): Segundo valor
        c (int): Terceiro valor, opcional

    Returns:
        int: Resultado da soma
    """
    return a + b + c

print(soma(1,2))
print(soma(1,2, 4))

# help(soma)