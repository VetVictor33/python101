
greater = 0
smaller = float('inf')

rounds = int(input('How much numbers do you want to compare?'))

while (rounds != 0):
  number = int(input('Choose a number: '))
  rounds -= 1

  if number > greater:
    greater = number
  if smaller > number:
    smaller = number

print(f'The greater number was {greater} and the smaller was {smaller}')