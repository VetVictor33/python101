numbers = []

while True:
  n = input(f'Digite um número número: ')

  if not n.isdigit():
    continue

  n = int(n)
  if n not in numbers:
    numbers.append(n)
  
  stop = input(f'Press F to stop ')
  if stop and stop in 'Ff': 
    break

numbers.sort()
print(f'Você escolheu os números: {numbers}')