def printTable(number):
  count = 1
  while count <= 10:
    print('{} * {:2} = {:2}'.format(number, count, count * number))
    count += 1
  return

number = input('Type a number you what the numeric table: ')

printTable(int(number))