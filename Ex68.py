#Código que jogar par ou impar, stopa quando o jogador perde e exibe quantas vitórias consecutivas

from random import randint

victory = 0

while True:
    player_choice = int(input("Digite um número: "))
    computer_choice = randint(0, 10)  # Escolhe um número aleatório entre 1 e 10
    total = player_choice + computer_choice
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {player_choice}\ne o computador {computer_choice}\nTotal: {total}")
    print("Deu PAR" if total % 2 == 0 else "Deu ÍMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            victory += 1
        else:
            print("Você Perdeu!")
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            victory += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente......")

print(f"GAME OVER! Você venceu {victory} vezes")





