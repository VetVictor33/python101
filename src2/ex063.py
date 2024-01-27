primeiro_desejado = int(input('A partir de qual termo você quer saber a sequência de Fibonacci? '))
limite = int(input('Quantos termos você quer saber? '))

atual = 0
precedente = abs(-1)
proximo = atual + precedente

contador = 0
while contador < limite:
  if primeiro_desejado <= atual:
    print(atual, end= ' ')
    contador+=1
  atual = proximo
  precedente = atual - precedente
  proximo = atual + precedente