from random import randint

my_crazy_tupla = (
  randint(0, 1000),
  randint(0, 1000),
  randint(0, 1000),
  randint(0, 1000),
  randint(0, 1000),
)

greater = smaller = my_crazy_tupla[0]

for craziness in my_crazy_tupla:
  if craziness > greater:
    greater = craziness
  elif craziness < smaller:
    smaller = craziness

print(f'Minha tupla aleatória: {my_crazy_tupla}')
print(f'Maior número {greater}')
print(f'Menor número {smaller}')