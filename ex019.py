from random import randint, choice

student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Forth student: ')

students = [student1, student2, student3, student4]

chosen = students[randint(0, 3)]
chosen_random = choice(students)

print(f'Student {chosen} is the one to blank the board')
print(f'Student {chosen_random} is the one to blank the board')