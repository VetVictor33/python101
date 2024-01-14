name = input('Say your name... ').upper().strip()

print(f"""
You have {name.count('A')} A's
The first A is the number {name.index('A') + 1}
The last A is the number  {name.rfind('A') + 1}
""")