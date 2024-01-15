from datetime import date

def is_leap_year(year):
  multiple_four = year % 4 == 0
  multiple_hundred = year % 100 == 0
  multiple_four_hundred = year % 400 == 0

  if multiple_four_hundred or (multiple_four and not(multiple_hundred)):
    return True
  else:
    return False

year = int(input('Digite um ano para saber se ele é bissexto. Ex: 2013 '))

print(f'{year} {'É bissexto' if is_leap_year(year) else 'Não é bissexto'}')

year = date.today().year

print(f'{year} {'É bissexto' if is_leap_year(year) else 'Não é bissexto'}')