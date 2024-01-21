from random import randint
from time import sleep

import pygame

pygame.mixer.init()
wrong = pygame.mixer.Sound('./src/faustao-errou.mp3')
right = pygame.mixer.Sound('./src/acerto-mizeravi.mp3')

print('\033[0;32m<', '=' * 40, '>')
print(f'{'This is THE GAME':=^40}')
print('<', '=' * 40, '>', '\033[m')

while(True):
  chosen = int(input('\033[0;32;43mGuess a number between 0 and 6\033[m '))
  random_number = randint(0, 6)


  print('LEMME SEE IF YOU ARE RIGHT')
  sleep(0.2)
  print('...')
  sleep(0.5)

  if chosen == random_number:
    print('\033[0;32mAcerto, mizeravi!\033[m')
    right.play()
    sleep(2)
    break
  else:
    print(f'\033[0;31mERRrrrrou!\033[m \033[4mIt was \033[32m{random_number} \033[m')
    wrong.play()
    sleep(2)

pygame.quit()