def fahrenheit_to_celsius(F):
  return ((F-32) * 5/9)

def celsius_to_fahrenheit(C):
  return ((C*9)/5) + 32

def kelvin_to_celsius(K):
  return K - 273.15

F = float(input('How much Fahrenheit? '))
C = float(input('How much Celsius? '))
K = float(input('How muck Kelvin?' ))

print(f'{F}ºF is {fahrenheit_to_celsius(F):.2f}ºC')
print(f'{C}ºC is {celsius_to_fahrenheit(C):.2f}ºF')
print(f'{K}ºK is {kelvin_to_celsius(K):.2f}ºC')