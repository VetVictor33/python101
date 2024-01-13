def average(first, second):
  return (first + second)/2

first_grade = input('Gib me your first grade: ')
second_grade = input('Gib me ur second grade: ')

print('Your average grade is {}'.
      format(average(int(first_grade), int(second_grade))))