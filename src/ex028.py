from random import randint

chosen = int(input('Guess a number between 0 and 6 '))

random_number = randint(0, 6)

if chosen == random_number:
  print('Acerto, mizeravi')
else:
  print('ERRrrrrou!')