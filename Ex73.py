#Código tupla com os primeiros 20 colocados do campeonato BR

teams = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá',
         'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthias', 'Goiás', 'Bahia',
         'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')
sorted_teams = sorted(teams)
team_find = 'Cruzeiro'
print(f"5 primeiros colocados: {teams[0:5]}\n4 últimos colocados: {teams[-1:-5:-1]}\nO Cruzeiro está na posição:"
      f" {teams.index(team_find) + 1}\nOs times em ordem alfabética: {sorted(teams)}")

#for teams in sorted_teams:
 #   print(teams,',',end='')