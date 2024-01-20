altura = float(input('Altura '))
peso = float(input('Peso '))

imc = peso/pow(altura, 2)

print(f'IMC {imc:.2f}')
if imc < 18.5:
  print('Abaixo do ', end='')
elif imc <= 25:
  print('No ', end='')
elif imc <= 30:
  print('Sobrepeso - Acima do ', end='')
elif imc <= 40:
  print('Obesidade - muito acima do ', end='')
else :
  print('Obesidade mórbida - muito acima do ', end='')

print('peso ideal')