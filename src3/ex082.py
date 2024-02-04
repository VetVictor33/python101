numbers = []
odds = []
evens = []

while True:
  n = input('Dê um número pro pae [\'q\' p/ sair]: ')
  try: 
    n = int(n)
    numbers.append(n)
    if n % 2 == 0:
      evens.append(n)
    else:
      odds.append(n)
  except:
    break

print(f'Todos os números {numbers}')
print(f'Números pares {evens}')
print(f'Números ímpares {odds}')