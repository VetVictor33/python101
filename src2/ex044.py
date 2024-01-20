price = float(input('Qual o valor do produto? R$ '))
print('Forma de pagamento?')
payment_method = int(input('''
  [1] - Dinheiro/Cheque 10% de desconto
  [2] - Débito 5% de desconto
  [3] - 2x sem juros
  [4] - 3x ou mais com 30% de juros
'''))


if(1 > payment_method or payment_method > 4):
  print('Opção inválida! Devolva os produtos')
elif payment_method == 1:
  print(f'R$ {price * 0.90:.2f}')
elif payment_method == 2:
  print(f'R$ {price * 0.95:.2f}')
elif payment_method == 3:
  print(f'2x R${price / 2:.2f}')
elif payment_method == 4:
  portions = int(input('Quantas parcelas? ')) 
  print(f'{portions}x {price * 1.3/portions:.2f} total {price * 1.3:.2f}')