def factorial(n):
  if n == 1:
    return n * 1
  return n * factorial(n-1)

number = int(input('De qual número você quer o fatorial? '))
print(f'Fatorial de {number} com recursiva {factorial(number)}')