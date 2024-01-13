def average(first, second):
  return (first + second)/2

first_grade = input('Gib me your first grade: ')
second_grade = input('Gib me ur second grade: ')
average_grade = average(float(first_grade), float(second_grade))

print(f'Your average grade is {average_grade}')