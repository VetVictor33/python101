ns = (int(input('Digite o 1º número: ')),
int(input('Digite o 2º número: ')),
int(input('Digite o 3º número: ')),
int(input('Digite o 4º número: ')),
int(input('Digite o 5º número: ')))


print(f'9 apareceu {ns.count(9)}x')
try:
  print(f'3 foi o {ns.index(3) + 1}º')
except ValueError:
  print('Você não digitou o 3')
print('Os valores pares foram: ', end='')
for n in ns:
  if n % 2 == 0:
    print(n, end=', ')