user_input = input('Type something ')

print('Is {} numeric?'.format(user_input), user_input.isnumeric())
print('Is {} alpha?'.format(user_input), user_input.isalpha())
print('Is {} alphanumeric?'.format(user_input), user_input.isalnum())