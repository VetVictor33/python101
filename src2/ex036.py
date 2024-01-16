threshold_percentage = 0.3

loan = float(input('De quando você precisa? R$'))
wage = float(input('Quanto é seu salário? R$'))

years = int(input('Quantos anos de financiamento? '))

months = years * 12
month_payment = loan / months

print(f'Serão necessários {months} parcelas de R${month_payment:.2f}')

if month_payment > wage * threshold_percentage:
  print('Empréstimo recusado! Tente pagar em mais anos.')
else:
  print('Aprovado!')