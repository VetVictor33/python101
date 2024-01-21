from datetime import date

adult = 0
teen = 0
time_traveler = 0
year = date.today().year

while True:
  born_in = input('Digite o ano de nascimento ou q para sair: ')
  if born_in == 'q':
    break
  if int(born_in) > year:
    time_traveler += 1
  elif year - int(born_in) >= 18:
    adult+=1
  else:
    teen+=1

print(f'Temos {adult} adultos e {teen} jovens')
if time_traveler > 0:
  print(f'Também temos {time_traveler} viajantes do futuro')