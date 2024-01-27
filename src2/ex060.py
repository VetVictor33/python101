number = int(input('De qual número você quer o fatorial? '))

while_factorial = 1
number_factor = number
print(f'{number}!={number}', end='')
while number_factor > 0:
  while_factorial *= number_factor
  number_factor -= 1
  if(number_factor > 0):
    print(f'x{number_factor}', end='')

for_number = number
for_factorial = 1
for number in range(number, 1, -1):
  for_factorial *= number


print(f'={while_factorial}')
print(f'O fatorial de {for_number} no for é {for_factorial}')
