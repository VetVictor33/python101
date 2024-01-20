r1 = float(input('Digite um lado do triangulo (1/3) '))
r2 = float(input('Digite um lado do triangulo (2/3) '))
r3 = float(input('Digite um lado do triangulo (3/3) '))

condition1 = r1 + r2 > r3
condition2 = r1 + r3 > r2
condition3 = r3 + r2 > r1

triangle = condition1 and condition2 and condition3

if(not(triangle)):
  print('Essas retas não formam um triângulo')
elif r1 == r2 == r3:
  print('Triângulo equilátero')
elif r1 != r2 !=r3 !=r1:
  print('Triângulo escaleno')
else:
  print('Triangulo isósceles')