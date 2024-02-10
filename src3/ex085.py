numbers = [[],[]]
print('Digite [q] a qualquer momento p/ encerrar.')
while True:
    n = input('Digite um número: ')
    if not n.isalnum(): break
    n = int(n)
    if n % 2 == 1:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

numbers[0].sort()
numbers[1].sort()

if numbers[0] or numbers[1]:
    if numbers[0]:
        print(f'Você digitou os número ímpares: {numbers[0]}')
    else:
        print('Você não digitou números ímpares')

    if numbers[1]:
        print(f'Você digitou os número pares: {numbers[1]}')
    else:
        print('Você não digitou números pares')
else:
    print('Você não digitou numero algum')