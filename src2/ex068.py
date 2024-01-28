from random import randint

def winsOddOrEven(choice, n):
  choice = 'even' if choice == 1 else 'odd'
  if choice == 'even':
    if n % 2 == 0:
      return True
    return False
  elif choice == 'odd':
    if n % 2 == 0:
      return False
    return True

wins = 0
while True:
  print('[1] Par')
  print('[2] Impar')
  player = int(input('[1/2]? '))
  if player not in [1, 2]:
    continue
  n = randint(1, 100)
  if winsOddOrEven(player, n):
    wins += 1
  else:
    print(f'Errou! O número foi {n}')
    break
  print(f'Acertou! O número foi {n}')
print(f'Venceu {wins} vezes')