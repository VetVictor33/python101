def give_me_a_raise(old_salary, raise_percentage):
  salary_raise = old_salary * (raise_percentage/100)
  return salary_raise

old_salary = float(input('Tell us your current salary. We\'ll see what we can do... '))
raise_percentage = float(input('Tell us your percentage expectation: '))

salary_raise = give_me_a_raise(old_salary, raise_percentage)

new_salary = old_salary + salary_raise

print(f'Because you are a good asset to our company we are giving you a much deserved {raise_percentage:.2f}% raise, which is ${salary_raise:.2f} more than your old salary, making it now ${new_salary:.2f} ')