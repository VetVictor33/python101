phrase = input('Digite uma palavra: ').replace(' ', '')
inverted_phrase = phrase[::-1]

# for letter in range (len(phrase) - 1, -1, -1):
#   inverted_phrase += phrase[letter]

print(f'A {phrase.upper()} invertida é {inverted_phrase.upper()}')
if inverted_phrase == phrase:
  print('É um palíndromo')
else:
  print('Não é um palíndromo')