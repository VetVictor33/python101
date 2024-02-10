matrix = [[],[],[]]

for a in range(3):
    for b in range(3):
        matrix[a].append(int(input(f'Digite um número posição ({a},{b}): ')))

for n in matrix[0]:
    print(f'[ {n} ]', end= '')
print()
for n in matrix[1]:
    print(f'[ {n} ]', end= '')
print()
for n in matrix[2]:
    print(f'[ {n} ]', end= '')
print()