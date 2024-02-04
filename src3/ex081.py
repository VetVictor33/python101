numbers = list()

while True:
  n = input('Forneça um número [\'q\' p/ sair]: ')
  try: 
    numbers.append(int(n))
  except:
    break
    

if not numbers:
  print('Você não forneceu número algum :(')
else:
  desc = numbers[:]
  desc.sort(reverse=True)
  print(f'Você digitou {len(numbers)} números')
  print(f'Os números em ordem decrescente foram {desc}')
  if 5 in numbers:
    print('... e tem um 5 na lista!!!')
  else:
    print('... mas não tem um 5 na lista!!!')