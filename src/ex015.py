
day_price = 60
km_price = 0.15

def cal_car_rent(km, days):
  return days * day_price + km * km_price


days = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros rodou?  '))

price = cal_car_rent(km, days)

print(f'Você deve pagar R${price:.2f}')