#Código que recebe vários valores em lista, não armazena os repetidos e mostre os valores em ordem crescente
numbers = []
while True:
    values = input("Digite um valor ou digite [S] para sair: ")
    if values.upper() == 'S':
        break
    numbers.append(values)
    if values not in numbers:
        numbers.append(values)


print(f"Os valores digitados foram: {sorted(numbers)}")



