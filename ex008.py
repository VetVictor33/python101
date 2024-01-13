def convertToCentimeter(meter):
  return meter * 100

def converToMillimeter(meter):
  return convertToCentimeter(meter) * 10

meter = input('Type your meter: ')

print('It\'s {} centimeter and {} millimeter'.
      format(convertToCentimeter(int(meter)), 
             converToMillimeter(int(meter))))