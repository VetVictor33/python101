numbers = []

for c in range (5):
  n = input(f'Digite um número número[{c+1}/5]: ')
  if n.isdigit():
    numbers.append(int(n))
  else:
    print('Só estamos aceitando números no momento, não seja moleque e siga as instruções')
    continue

print(f'Lista: {numbers}')
if numbers:
  print(f'O MAIOR n foi {max(numbers)} na posição {numbers.index(max(numbers)) + 1}')
  print(f'O MENOR n foi {min(numbers)} na posição {numbers.index(min(numbers)) + 1}')