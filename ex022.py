name = input('Quel est ton nom? ')

upper = name.upper()
lower = name.lower()
length = len(name.replace(' ', ''))
first_name = name.split(' ')[0]
first_name_length = len(first_name)


print(f"""
      Uppercase = {upper}
      Lowercase = {lower}
      No spaces length = {length}
      First name = {first_name}
      First name length = {first_name_length}
""")
