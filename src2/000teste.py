from random import randint

options = ['Pedra', 'Papel', 'Tesoura']
while True :
  player = int(input('''
  [1] Pedra
  [2] Papel
  [3] Tesoura
  '''))
  if 4 > player> 0:
    break


player = options[player - 1]
machine = options[randint(0, 2)]

print(f'Jogador: {player}')
print(f'Computador: {machine}')

if player == 'Pedra':
  if machine == 'Pedra':
    print('Empate!')
  elif machine == 'Papel':
    print('O computador venceu!')
  elif machine == 'Tesoura':
    print('O jogador venceu!')
elif player == 'Papel':
  if machine == 'Pedra':
    print('O jogador venceu!')
  if machine == 'Papel':
    print('Empate!')
  if machine == 'Tesoura':
    print('O computador venceu!')
elif player == 'Tesoura':
  if(machine == 'Pedra'):
    print('O computador venceu!')
  elif(machine == 'Papel'):
    print('O jogador venceu!')
  elif(machine == 'Tesoura'):
    print('Empate')