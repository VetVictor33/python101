import math

number = int(input('Tell me a number: '))

print(f'{number ** 2} com **2, {pow(number, 2)} com .pow(), {math.pow(number, 2)} com math.pow()')
print(f'{number ** (1/2)} com **(1/2) {math.sqrt(number)} com math.sqrt()')

