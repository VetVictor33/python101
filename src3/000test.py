tupla = ('oi', 'hola', 'hi', 'salut', 'hallo')
tupla_sem_parenteses = 'tupla', 'sem', 'parênteses'

print(tupla[0: len(tupla)])
print(tupla_sem_parenteses[-1])
print(tupla_sem_parenteses[0:-1])

for index, greetings in enumerate(tupla):
  print(f'Greetings #{index} = {greetings}')

print(sorted(tupla))