#Código que leia dois valores e mostre um menu na tela: Somar, multiplicar, maior, novos números, sair do programa

numbers = 0

while numbers != 5:
    options = int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha uma das opções: "))
    if options == 5:
        break
    elif options == 1:
        number_1, number_2 = list(map(int,input("Digite os valores: ").split()))
        soma = (number_1 + number_2)
        print(f"{soma}")
    elif options == 2:
        number_1, number_2 = list(map(int,input("Digite os valores: ").split()))
        multiply = (number_1 * number_2)
        print(f"{multiply}")
    elif options == 3:
        number_1, number_2 = list(map(int, input("Digite os valores: ").split()))
        if number_1 > number_2:
            maior = number_1
        else:
            maior = number_2
        print(f"O maior é: {maior}")
    elif options == 4:
        number_1, number_2 = list(map(int, input("Digite os valores: ").split()))


exit()



