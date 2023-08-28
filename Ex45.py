#Código que simula jogo pedra, papel e tesoura

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computer = randint(0, 2)

print("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")

player = int(input("Qual é sua jogada? "))
print('-=' * 11)
print(f"Computador jogou {itens[computer]}")
print(f"Jogador jogou {itens[player]}")
print('-=' * 11)

if computer == 0:
    if player == 0:
        print("EMPATE")
    elif player == 1:
        print("JOGADOR VENCE")
    elif player == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computer == 1:
    if player == 0:
        print("COMPUTADOR VENCE")
    elif player == 1:
        print("EMPATE")
    elif player == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")

elif computer == 2:
    if player == 0:
        print("JOGADOR VENCE")
    elif player == 1:
        print("COMPUTADOR VENCE")
    elif player == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
