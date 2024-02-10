from random import randint
from time import sleep

def mega_sena(tries):
    games = []
    for c in range(tries):
        games.append([])
        while len(games[c]) < 6:
            n = randint(1, 60)
            if n not in games[c]:
                games[c].append(n)
    return games

n_games = int(input('Quantos jogos você quer apostar? '))
games = mega_sena(n_games)

for game in games:
    print(game)
    sleep(1)
