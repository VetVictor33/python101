city = input('Digite o nome da sua cidade: ')

city = city.split(' ')[0].capitalize()

if (city == 'Santo'):
  print('You live on a Santo city')
else:
  print('Go away, your are not from a Santo city!')