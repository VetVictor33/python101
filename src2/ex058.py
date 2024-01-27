from random import randint
from time import sleep

import pygame

pygame.mixer.init()
wrong = pygame.mixer.Sound('./src/faustao-errou.mp3')
right = pygame.mixer.Sound('./src/acerto-mizeravi.mp3')

tries = 0
finishedMessage = {
  1: 'De primeira! Você é profissional!',
  2: 'Depois de apenas duas tentativas!',
  3: '3 tentativas é o limite para ainda ser bom!',
  4: 'Depois de 4 tentativas você também tá de brincadeira, né...'
}
upperLimit = 10
lowerLimit = 0
print('\033[0;32m<', '=' * 40, '>')
print(f'{'This is THE GAME':=^40}')
print('<', '=' * 40, '>', '\033[m')
while(True):
  tries+=1

  chosen = int(input(f'\033[0;32;43mEscolha um número entre {lowerLimit} e {upperLimit}\033[m '))
  random_number = randint(lowerLimit, upperLimit)


  print('PROCESSANDO OS PROCESSOS COM O USO DE NANOPROCESSADORES')
  sleep(0.2)
  print('...')
  sleep(0.5)

  if chosen == random_number:
    print('\033[0;32mAcerto, mizeravi!\033[m')
    if(tries < 5):
      print(finishedMessage[tries])
    else:
      print(f'Depois de {tries} tentativas fico na dúvida se você realmente venceu hahahaha')
    right.play()
    sleep(2)
    break
  else:
    print(f'\033[0;31mERRrrrrou!\033[m \033[4mIt was \033[32m{random_number} \033[m')
    wrong.play()
    sleep(2)

pygame.quit()