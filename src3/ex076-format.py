market = (
  'Gabinete', 150.69,
  'Placa mãe', 799.99,
  'processador', 1500.00,
  'ram', 999.99,
  'placa de vídeo', 2999.99,
  'cooler', 295.50,
  'mouse', 99.99,
  'teclado', 130.90,
  'webcam', 199.96
)
total = 0

print('-=' * 25)
print(f'{'montando o seu pc'.upper():^50}')
print('-=' * 25)

for item in market:
  if isinstance(item, str):
    print(f'{item.capitalize():.<30}', end=' ')
  else:
    print(f'R$ {item:>7.2f}')
    total += item
print(f'{'Total'.upper():*<30}', end=' ')
print(f'R$ {total:>7.2f}')

print('--' * 25)