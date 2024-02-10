def grater(*n):
    if not len(n):
        raise AttributeError('Atributo obrigatório, meu parça')
    grater = n[0]
    for number in n:
        if number > grater:
            grater = number
    return grater

print(grater(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(grater(1, 2, 3, 4, 53, 6, 7, 8, 9))
print(grater(11, 2, 3, 4, 5, 6, 7, 8, 9))
print(grater(1, 22, 3, 4, 5, 6, 7, 8, 9))
print(grater(1, 2, 3, 43, 5, 6, 47, 8, 9))
print(grater())