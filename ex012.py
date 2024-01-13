def give_me_a_raise(old_salary, raise_percentage):
  salary_raise = old_salary + old_salary * (raise_percentage/100)
  return salary_raise

old_salary = int(input('Tell us your current salary. We\'ll see what we can do... '))
deserved_raise = int(input('Tell us your percentage expectation: '))

new_salary = give_me_a_raise(old_salary, deserved_raise)

# print('Because you are a good asset to our company we are giving you a much deserved {}% raise, which is ${} more than your old salary, making it now ${} '.
#       format(deserved_raise, new_salary - old_salary, new_salary))
print(f'Because you are a good asset to our company we are giving you a much deserved {deserved_raise}% raise, which is ${new_salary - old_salary} more than your old salary, making it now ${new_salary} ')