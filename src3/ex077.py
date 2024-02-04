words = 'zarabatana', 'coberta', 'free willy', 'tuc tuc'
vowels = 'a', 'e', 'i', 'o', 'u'

for word in words:
  print(f'\nA palavra {word.upper()} tem as vogais: ', end='')
  for letter in word:
    if letter in vowels:
      print(letter, end=' ')