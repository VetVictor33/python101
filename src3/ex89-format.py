def print_line():
    print('-=' * 15)

def print_grades(students_grades):
  print(f'{"No.":>2}', end='')
  print(f'{"Nome".upper():>15}', end='')
  print(f'{"Média".upper():>10}')
  for index, student in enumerate(students_grades):
    print(f'{index+1:>2}', end='')
    print(f'{student[0].upper():>15}', end='')
    avg = (student[1][0] + student[1][1]) / 2
    print(f'{avg:>10.2f}')

print_line()
print(f'{"Calculando a média".upper():^30}')
print_line()

students_grades = []
c = 0
while True:
    print(f'Aluno {c + 1}:')
    name = input('Nome: ')
    grade1 = float(input('Nota (1/2): '))
    grade2 = float(input('Nota (2/2): '))
    student = [name, [grade1, grade2]]
    students_grades.append(student)
    
    c+=1

    stop = input('Aperte x p/ sair ou enter para prosseguir ')
    if stop: break

print_line()
print_grades(students_grades)
print_line()

while True:
  student = input('Quer ver a nota de quais aluno (No)? [q p/ encerrar]: ')
  if not student.isnumeric():
    break
  elif int(student) > len(students_grades):
    print_grades(students_grades)
    continue 

  student = int(student) - 1
  print(f'As notas de {students_grades[student][0]} são: ', end='')
  for grande in students_grades[student][1]:
    print(f'{grande:.2f}', end=' ')
  print()
