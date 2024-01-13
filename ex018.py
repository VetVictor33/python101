from math import cos, sin, tan, radians

degree = float(input('Qual o seu ângulo favorito? '))

radians = radians(degree)

n_cos = cos(radians)
n_sin = sin(radians)
n_tan = tan(radians)

print(f'A tangente de {degree:.2f}º é {n_tan:.2f}º, seno {n_sin:.2f}º e cosseno {n_cos:.2f}º. ')