#Código que lê nome jogador, qtde partidas, qtde gols. Mostra total de gols.

data_player = dict()
data_player['Nome'] = str(input("Nome do jogador: "))
data_player['Partidas'] = int(input("Quantidade de Partidas Jogadas: "))
data_player['Gols'] = []

for i in range(data_player['Partidas']):
    gols_partida = int(input(f"Quantidade de gols na partida {i+1}: "))
    data_player['Gols'].append(gols_partida)
print("-=" * 30)

print(f"O Jogador {data_player['Nome']} jogou {data_player['Partidas']} partidas")

print("-=" * 30)

print("Quantidade de gols por partida:")

for partida, gols in enumerate(data_player['Gols'], start=1):
    print(f"Partida {partida}: {gols} gols")

print("-=" * 30)

print(f"Total de gols: {sum(data_player['Gols'])}")

exit()


