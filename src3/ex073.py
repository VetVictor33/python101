teams = (
    "Palmeiras",
    "Grêmio",
    "Atlético - MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Atlético - PR",
    "Internacional",
    "Fortaleza",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América - MG",
)

print('=-' * 30)
print(f'{'Brasileirão 2023':^60}')
print('=-' * 30)

print('Os 5 primeiros colocados: ')
for position, team in enumerate(teams[:5]):
  print(f'{position + 1}º - {team}')

print('Os 4 últimos: ')
for index in range(len(teams), len(teams) - 4, -1):
  print(f'{index}º - {teams[index - 1]}')

print('Todos os times em ordem alfabética: ')
for team in sorted(teams):
  print(f'{team}', end='; ')