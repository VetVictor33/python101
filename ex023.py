
number = '-1'

while(int(number) < 0 or int(number) > 9999):
  number = input('Type a number from 0 to 9999 ')

number = number.rjust(4, '0')

print(f"""
        unidades: {number[3]}
        dezenas: {number[2]}
        centenas: {number[1]}
        milhar: {number[0]}
""")

print('----math is fun -----')

number = int(number)

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print(f'unidades: {u}')
print(f'dezenas: {d}')
print(f'centenas: {c}')
print(f'milhar: {m}')