number = int(input('Digite um número inteiro: '))


print('Escolha a base de conversão: ')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

choice = int(input('Opção: '))

if choice == 1 :
  answer = bin(number)[2:]
  print(f'{number} em binário é {answer}')
elif choice == 2:
  answer = oct(number)[2:]
  print(f'{number} em octal é {answer}')
else:
  answer = hex(number)[2:]
  print(f'{number} em hexadecimal é {answer}')