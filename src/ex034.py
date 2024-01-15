wage = float(input('Do you wanna a raise? Tell me your wage? '))


if (wage <= 1250):
  new_wage = wage * 1.15
else:
  new_wage = wage * 1.1

print(f'Your new wage is R${new_wage:.2f}')