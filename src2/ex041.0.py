from datetime import date

born_in = int(input('Qual seu ano de nascimento? '))

year = date.today().year
age = year - born_in

if born_in > year:
  print(f'Não aceitamos viajantes do futuro! Tente em {born_in - year} ano(s)')
elif age <= 9:
  print('Mirin')
elif age <= 14:
  print('Infantil')
elif age <=19:
  print('Junior')
elif age <=25:
  print('Sênior')
else: 
  print('Master')