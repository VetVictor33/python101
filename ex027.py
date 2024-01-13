name = input('Qual seu nome? ')

name_array = name.split(' ')

first_name = name_array[0]
last_name = name_array[-1:][0]

print(f"""
Primeiro nome: {first_name}
Last Name: {last_name}
""")