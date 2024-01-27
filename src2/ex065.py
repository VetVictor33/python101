count = total = greater = lower = 0

while True:
  n = input('Digite um número ou [q] p/ sair: ')
  if n == 'q': break
  else: n = int(n)

  if count == 0: greater = lower = n
  total += n
  if(greater <= n): greater = n
  if(lower > n): lower = n
  
  count += 1

avg = total/count

print(f'Números digitados: {count}\nTotal: {total}\nMédia: {avg:.2f}\nMenor: {lower}\nMaior: {greater}')
