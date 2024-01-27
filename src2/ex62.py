first_n = int(input('Digite o primeiro termo da PA: '))
ration = int(input('Digite a razão da PA: '))
limit = int(input('Quantos números você quer saber?'))

n = first_n
count = 0

while count < limit:
  print(n, end=' ')
  n += ration
  count+=1
  if count == limit:
    plus = int(input('\nDigite 0 para sair ou quantos termor a mais você quer saber: '))
    limit+=plus
