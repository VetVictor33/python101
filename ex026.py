name = input('Say your name... ')

print(f"""
You have {name.upper().count('A')} A's
The first A is the number {name.upper().index('A') + 1}
The last A is the number  {name.upper().rfind('A') + 1}
""")