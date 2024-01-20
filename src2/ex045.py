from random import randint

options = ['Pedra', 'Papel', 'Tesoura']
option_loses_to = {
  'Pedra': 'Papel',
  'Papel': 'Tesoura',
  'Tesoura': 'Pedra'
}

while(True):
  player = int(input('''
  [1] Pedra
  [2] Papel
  [3] Tesoura
  '''))
  if(4 > player> 0):
    break

player = player - 1
machine = randint(0, 2)


print(f'Jogador: {options[player]}')
print(f'Máquina: {options[machine]}')

if options[player] == option_loses_to[options[machine]]:
  print('Vitória do Jogador!')
elif options[machine] == option_loses_to[options[player]]:
  print('Vitória da máquina')
else:
  print('Empate!')

machine = options[machine]
player = options[player]

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

opção_que_vence = {
  'Pedra': 'Papel',
  'Papel': 'Tesoura',
  'Tesoura': 'Pedra'
}

if(player == opção_que_vence[machine]):
  print('O jogador venceu!')
elif(machine == opção_que_vence[player]):
  print('O computador venceu!')
else:
  print('Empate!')