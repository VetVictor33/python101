numbers = []

for index in range(5):
  n = int(input(f'Digite um número [{index + 1}/5]: '))
  if not numbers:
    numbers.append(n)
    print('O primeiro item foi adicionado')
    continue
  index_to_insert = 0 
  for index, number in enumerate(numbers):
    if n >= number:
      index_to_insert = index + 1
    elif n < number:
      numbers.insert(index, n)
      print(f'{n} foi adicionado na posição {index}')
      break
    if index == len(numbers) - 1:
      numbers.insert(index_to_insert, n)
      print(f'{n} foi adicionado na posição {index_to_insert}')
      break

print(numbers)