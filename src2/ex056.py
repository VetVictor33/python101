count = 1
people = []

while True:
  print(f'---- {count}ª pessoa ----')
  name = input('Nome:')

  if not(name):break

  age = int(input('Idade:'))
  gender = input('Sexo(M/F):').upper()
  people.append({"name": name, "age": age, "gender": gender})
  
  count +=1

age_sun = 0
oldest_man = {"age": -1}
younger_than_20_women = []

for person in people:
  age_sun += person.get('age')
  if(person.get('gender') == 'F' and person.get('age') < 20):
    younger_than_20_women.append(person)
  if(person.get('gender') == 'M' and oldest_man.get('age') < person.get('age')):
    oldest_man = person

age_avg = age_sun / len(people)

print(f'Média de idade {age_avg:.2f} anos')
if(not(oldest_man.get('age')== -1)):
  print(f'O homem mais velho tem {oldest_man.get('age'):.2f} anos e se chama {oldest_man.get('name')}')
print(f'Ao todos temos {len(younger_than_20_women)} mulheres com menos de 20')