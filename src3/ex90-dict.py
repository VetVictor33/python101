students = list()
student = dict()
while True:
    student['nome'] = input('Nome: ')
    student['nota'] = float(input('Nota:'))
    if student['nota'] < 7:
        student['situação'] = 'Reprovado(a)'
    else:
        student['situação'] = 'Aprovada(o)'
    students.append(student.copy())
    stop = input('Wanna stop[y/n]: ')
    if stop and stop in 'Yy': break

for student in students:
    for k, v in student.items():
        print(f'{k.capitalize()} -- {v}') 