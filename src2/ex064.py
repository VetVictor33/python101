total = 0
while(True):
  n = int(input('Qual numero quer somar? [999 para encerrar]: '))
  if n == 999:
    print('Programa encerrado')
    break
  total += n

print(f'Soma = {total}')