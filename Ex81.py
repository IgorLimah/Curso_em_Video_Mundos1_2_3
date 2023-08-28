#Código que lê vários números e mostre quantos foram digitados, decrescente e se o valor 5 foi digitado

numbers = []
count_numbers = 0
count_five = 0

while True:
    values = input("Digite um valor ou digite [S] para sair: ")
    if values.upper() == 'S':
        break
    numbers.append(values)
    count_numbers += 1
    if 5 in numbers:
        print("O valor 5 faz parte da lista.")
    else:
        print("O valor 5 não foi encontrado na lista.")

print(f"Quantida de números digitados: {count_numbers}\nValores ordenados: {sorted(numbers)}")