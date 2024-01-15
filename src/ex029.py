
def cal_ticket(speed, max_speed, infraction_index):
  exceeded_speed = speed - max_speed
  if exceeded_speed < 1:
    return
  return exceeded_speed * infraction_index

max_speed = 80
speed = float(input('Qual a velocidade do carro, guarda? '))

ticket = cal_ticket(speed, max_speed, 7)

if(ticket):
  print(f'Multa no valor de R${ticket}!')
else: 
  print('Sem multa hoje!')