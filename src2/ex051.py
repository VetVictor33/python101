first_n = int(input('Qual o primeiro termo da PA? '))
ration = int(input('Qual a razão da PA? '))

for c in range(first_n, ration * 10, ration):
  print(c, end=' ')