def printTable(n):
  for c in range(1, 11):
    print(f'{n} x {c:2} = {c * n:2}')

number = input('Type a number you what the numeric table: ')

printTable(int(number))