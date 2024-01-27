number = int(input('De qual número você quer o fatorial? '))
while_factorial = 1
number_factor = number
while number_factor > 0:
  while_factorial *= number_factor
  number_factor -= 1

for_factorial = 1
for number in range(number, 1, -1):
  for_factorial *= number

print(f'O fatorial de {number} no while é {while_factorial}')
print(f'O fatorial de {number} no for é {for_factorial}')