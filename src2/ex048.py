sun = 0
for c in range (1, 501):
  if c % 3 == 0 and c % 2 != 0:
    sun += c

print(sun)