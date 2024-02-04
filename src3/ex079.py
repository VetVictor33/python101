numbers = []

while True:
  n = input(f'Digite um número número: ')

  try:
    n = int(n)
  except:
    continue

  if n not in numbers:
    numbers.append(n)
  
  stop = input(f'Press F to stop ')
  if stop and stop in 'Ff': 
    break

numbers.sort()
print(f'Você escolheu os números: {numbers}')