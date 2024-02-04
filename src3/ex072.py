numbers = (
  'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
  'seis', 'sete', 'oito', 'nove', 'dez',
  'onze', 'doze', 'treze', 'quatorze', 'quinze',
  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
  n = input('Digite um número entre 0 e 20: ')
  if n == 'q': break
  if not n.isdigit() or 0 < int(n) > 20:
    print('Tá me tirando? Digita "q" pra sair ou tente outra vez')
    continue
  print(f'Você digitou o número {numbers[int(n)]}')