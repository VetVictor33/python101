matrix = [[],[],[]]

for a in range(3):
    for b in range(3):
        matrix[a].append(int(input(f'Digite um número posição ({a},{b}): ')))

for line in matrix:
    for n in line:
        print(f'[{n:^7}]', end= '')
    print()