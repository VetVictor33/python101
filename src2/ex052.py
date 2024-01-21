n = int(input('Digite um número: '))

divided = 0
for c in range (1, n + 1, 1):
  if n % c == 0:
    print(f'[{c}]', end=' ')
    divided+=1
  else:
    print(f'{c}', end=' ')
print(f'\nO número {n} foi dividido {divided} vezes, logo{'' if divided > 1 else 'não'} é primo.')