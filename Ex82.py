#Código que lê vários valores em lista, cria 2 listas para amarzenar pares e ímpares

numbers = []
numbers_pares = []
numbers_impares = []

while True:
    value = input("Digite um valor ou digite [S] para sair: ")
    if value.upper() == 'S':
        break
    number = int(value)
    numbers.append(number)
    if number % 2 == 0:
        numbers_pares.append(number)
    else:
        numbers_impares.append(number)

print(f"Lista completo: {numbers}\nLista de pares: {numbers_pares}\nLista de ímpares: {numbers_impares}")

exit()

