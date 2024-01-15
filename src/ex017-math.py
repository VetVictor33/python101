from math import hypot

adj = float(input('Qual o cateto adjacente do seu triângulo retângulo? '))
ops = float(input('Cateto oposto? '))

hypotenusesByMath = hypot(adj, ops)
hypotenusesByMe = (adj ** 2 + ops ** 2) ** (1/2)

print(f'Essa é a hipotenusa segundo Math, meu caro Pitágoras {hypotenusesByMath:.2f}')
print(f'Essa é a hipotenusa segundo Eu, meu caro Pitágoras {hypotenusesByMath:.2f}')