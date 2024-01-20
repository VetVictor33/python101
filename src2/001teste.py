from random import randint

options = ['Pedra', 'Papel', 'Tesoura']
while True:
  player = int(input('''
  [1] Pedra
  [2] Papel
  [3] Tesoura
  '''))
  if 4 > player> 0:
    break

player = options[player - 1]
machine = options[randint(0, 2)]

opção_que_vence = {
  'Pedra': 'Papel',
  'Papel': 'Tesoura',
  'Tesoura': 'Pedra'
}

print(f'Jogador: {player}')
print(f'Computador: {machine}')

if player == opção_que_vence[machine]:
  print('O jogador venceu!')
elif machine == opção_que_vence[player]:
  print('O computador venceu!')
else:
  print('Empate!')