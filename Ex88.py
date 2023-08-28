#Código que pergunta ao usuário quantidade de palpites e gera jogos mega sena

import random

shot = int(input("Quantos jogos deseja fazer? "))

for j in range(shot):
    numeros_sorteados = []
    for i in range(6):
        numero_sorteado = random.randint(1, 60)
        numeros_sorteados.append(numero_sorteado)
    print(f"Sequência {j + 1}: {sorted(numeros_sorteados)}")