doTheMath = {
  1 : lambda a, b: a + b,
  2 : lambda a, b: a * b,
  3 : lambda a, b: a if a > b else b
}

while True:
  n1 = int(input('N1: '))
  n2 = int(input('N2: '))
  operation = int(input('''
Digite a operação desejada:
                        [1]Somar
                        [2]Multiplicar
                        [3]Maior
                        [4]Trocar números
                        [5]Sair
Operação: '''))
  if operation == 5:
    print('Você saiu do programa')
    break
  if operation != 4:
    print(doTheMath[operation](n1, n2))