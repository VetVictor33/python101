from random import randint

def mega_sena(tries):
    games = []
    for c in range(tries):
        games.append([])
        while len(games[c]) < 6:
            n = randint(1, 60)
            if n not in games[c]:
                games[c].append(n)
    return games

games = int(input('Quantos jogos você quer apostar? '))
print(f'Tomae: {mega_sena(games)}')
    