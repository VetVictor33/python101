people = []

heavier = lighter = 0
while True:
    name = input('Digite o nome: ')
    if name == 'q': break
    weight = float(input('Digite o peso: '))
    print('Digite q p/ sair')

    if heavier == 0 and lighter == 0:
        heavier = lighter = weight
    elif weight >= heavier:
        heavier = weight
    elif weight < lighter:
        lighter = weight
    people.append({'name': name, 'weight': weight})


print(f'Você cadastrou {len(people)}')
print(f'O menor peso foi {lighter:.2f}kg, peso de ', end='')

for person in people:
    if person['weight'] == lighter:
        print(person['name'], end=', ')


print(f'\n O maior peso foi {heavier:.2f}kg, peso de ', end='')
for person in people:
    if person['weight'] == heavier:
        print(person['name'], end=', ')
print()