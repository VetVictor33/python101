from random import randint
from time import sleep

import pygame

pygame.mixer.init()
wrong = pygame.mixer.Sound('./src/faustao-errou.mp3')
right = pygame.mixer.Sound('./src/acerto-mizeravi.mp3')

print('<', '=' * 40, '>')
print(f'{'This is THE GAME':=^40}')
print('<', '=' * 40, '>')
chosen = int(input('Guess a number between 0 and 6 '))

random_number = randint(0, 6)

print('LEMME SEE IF YOU ARE RIGHT')
sleep(0.2)
print('...')
sleep(1)

if chosen == random_number:
  print('Acerto, mizeravi')
  right.play()
  sleep(2)
else:
  print(f'ERRrrrrou! It was {random_number}')
  wrong.play()
  sleep(2)

pygame.quit()