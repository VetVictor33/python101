def calc_ticket_price(km):
  if km <= 200:
    return km * 0.5
  else:
    return km * 0.45
  

km = int(input('Para quão longe você vai, meu cara Patati? '))

ticket_price = calc_ticket_price(km)

print(f'Custará apenas R${ticket_price}')