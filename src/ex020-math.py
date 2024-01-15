from random import shuffle

student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Forth student: ')

students = [student1, student2, student3, student4]

shuffle(students)

for index, student in enumerate(students):
  print(f'{student} will be {index+1}')