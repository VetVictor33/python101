heights = []
while True:
  height = input('Digite o peso: ')
  if not(height):
    break
  heights.append(float(height))

heights.sort()
lighter = heights[0]
heavier = heights[-1]

print(f'O menor peso foi {lighter:.2f}kg')
print(f'O maior peso foi {heavier:.2f}kg')