while True:
  n = int(input('Digite um número para saber sua tabuada[<0 / sair]: '))
  if( n < 0): break
  for count in range(1, 11):
    print(f'{n} x {count:2d} = {n * count}')