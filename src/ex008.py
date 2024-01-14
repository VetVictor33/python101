def convertToCentimeter(meter):
  return meter * 100

def converToMillimeter(meter):
  return convertToCentimeter(meter) * 10

meter = input('Type your meter: ')
cm = convertToCentimeter(int(meter))
mm = converToMillimeter(int(meter))

print(f'{meter} meter is {cm} centimeter and {mm} millimeter')