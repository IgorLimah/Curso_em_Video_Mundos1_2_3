#Código que lê valores jogados por dados aleatórios, guarde em dicionário e mostre em ordem. Vencedor = maior valor

from random import randint
from operator import itemgetter

raffle = {'Player 1':randint(1,6),
          'Player 2':randint(1,6),
          'Player 3':randint(1,6),
          'Player 4':randint(1,6)}

ranking = list()

for k, v in raffle.items():
    print(f"{k} tirou {v} no dado")

ranking = sorted(raffle.items(), key=itemgetter(1), reverse=True)
print()
print("RANKING")
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")
exit()
