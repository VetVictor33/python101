def is_odd(number):
  if number % 2 == 0:
    return True
  else:
    return False
  
chosen_number = int(input('Escolhe um numero aí então '))

print(f'{'Par' if is_odd(chosen_number) else 'Impar' }')