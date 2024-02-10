from random import randint
from time import sleep

players = [
    {'player': 1},
    {'player': 2},
    {'player': 3},
    {'player': 4},
]

for player in players:
    player['dice'] = randint(1,6)

players.sort(key= lambda x : x['dice'], reverse=True)

for index, player in enumerate(players):
    print(f'{index+1}º lugar: ', end='')
    for k,v in player.items():
        print(f'{k}: {v}', end=' ')
    print()
    sleep(1)
    