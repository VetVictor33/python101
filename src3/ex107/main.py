import currency

n = float(input('Digite um valor: R$'))

print(f'Você digitou {currency.convert_to_currency(n)}')
print(f'Valor com 50% de aumento {currency.convert_to_currency((currency.increase(0.5,n)))}')
print(f'Valor com 90% de desconto {currency.convert_to_currency((currency.decrease(0.9,n)))}')
print(f'Dobro {currency.convert_to_currency((currency.double(n)))}')
print(f'Metade {currency.convert_to_currency((currency.half(n)))}')