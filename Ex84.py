#Código que lê o nome, peso de várias pessoas em uma lista. Mostre qtd de pessoas cadastradas, pessoas com  kg e -KG

personal_file = []
max_height = []
min_height = []

while True:
    name = (str(input("Nome: ").upper()))
    height = float(input("Peso: "))
    personal_file.append([name,height])
    stops = str(input("Deseja continuar? [S/N] "))
    if stops.upper() == 'N':
        break

max_height_value = max(personal_file, key=lambda x: x[1])[1]
min_height_value = min(personal_file, key=lambda x: x[1])[1]

for name, height in personal_file:
    if height == max_height_value:
        max_height.append((name, height))
    if height == min_height_value:
        min_height.append((name, height))

print(f"Quantidade de pessoas cadastradas: {len(personal_file[0])}\nPessoas mais pesadas: {max_height}\nPessoas mais leves: {min_height} ")


