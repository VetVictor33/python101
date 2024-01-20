
grades = []
while(True):
  grade = input('Digite a nota, ou digite q para finalizar ')
  if grade == 'q':
    break
  grades.append(float(grade))

grades_sum = 0
for grade in grades:
  grades_sum += grade

avg = grades_sum/len(grades)

approved_avg = 7
second_chance_avg = 5

if avg < second_chance_avg:
  print('Você foi 100% REPROVADO. Tente novamente ano que vem!')
elif avg >= approved_avg:
  print('APROVADO! Próximo!')
else:
  print('Você está de RECUPERAÇÃO!')

