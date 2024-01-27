sexo = 'sim'
while sexo != 'M' and sexo != 'F':
  sexo = input('Digite o sexo [F/M]: ').strip().upper()
qualOSexo = {
  'F': 'mulher',
  'M': 'homem',
}

print(f'Então você é {qualOSexo[sexo]}')
