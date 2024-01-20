from datetime import date

age = int(input('Informe sua idade: '))

year = date.today().year

years_to_serve = 18 - age

if age < 18:
  print(f'Você tem {age} anos e falta{'m' if years_to_serve > 1 else ''} {years_to_serve} ano{'s' if years_to_serve > 1 else ''} para o alistamento')
elif age == 18:
  print(f'Hora de se alistar')
else:
  print(f'Você já tem {age} e deveria ter se alistado há {years_to_serve * -1} ano{'s' if years_to_serve < -1 else ''}, tome vergonha nessa cara')