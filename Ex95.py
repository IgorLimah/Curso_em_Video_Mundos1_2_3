team = list()
player = dict()
matches = list()

while True:
    player.clear()
    player['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {player['nome']} jogou? "))
    matches.clear()

    for c in range(0, tot):
        matches.append(int(input(f"Quantos gols na partida {c+1}? ")))
    player['Gols'] = matches[:]
    player['Total'] = sum(matches)
    team.append(player.copy())

    while True:
        breaks = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if breaks in 'SN':
            break
        print("Erro! Responda apenas S ou N.")
    if breaks == 'N':
        break
print('-=' * 40)
print("cod", end='')
for i in player.keys():
    print(f"{i:<15}", end='')
print()
print('-=' * 40)

for k, v in enumerate(team):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-=' * 40)

while True:
    search = int(input("Exibir dados de qual jogador? (0 para encerrar) "))
    if search == 0:
        break
    if search >= len(team):
        print(f"Erro! Não existe jogador com código de {search}!")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {team[search]['nome']}:")

        for i , g in enumerate(team[search]['Gols']):
            print(f"No jogo {i+1} fez {g} gols.")

    print('-=' * 40)