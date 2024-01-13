name = input('Quel est ton nom? ')

upper = name.upper()
lower = name.lower()
length = len(name.replace(' ', ''))
first_name_length = len(name.split(' ')[0])

print(f"""
      Uppercase = {upper}
      Lowercase = {lower}
      No spaces length = {length}
      First name length = {first_name_length}
""")
