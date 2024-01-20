first_grade = float(input('Qual a primeira nota? '))
second_grade = float(input('Qual a segunda nota? '))

approved_avg = 7
second_chance_avg = 5

avg_grade = (first_grade + second_grade) / 2

if avg_grade < second_chance_avg:
  print('Você foi 100% REPROVADO. Tente novamente ano que vem!')
elif avg_grade >= approved_avg:
  print('APROVADO! Próximo!')
else:
  print('Você está de RECUPERAÇÃO!')