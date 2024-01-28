women = men = adults = 0

print('---contador de gente---'.upper())
while True:
  person_gender = input('[M/F]').strip()
  if person_gender not in ('MmFf'): continue

  person_age = int(input('Idade: '))
  if person_gender in 'Mm':
    men += 1
  else: 
    women += 1
  if person_age >= 18:
    adults += 1
  stop = input('Vai parar? [Y/N]')
  if stop not in 'nN': break

print(f'Contei aqui {women} mulheres, {men} homens, desses {adults} adultos')