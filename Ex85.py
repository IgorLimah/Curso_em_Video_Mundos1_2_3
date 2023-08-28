#Código que lê 7 valores em lista, mostre uma lista de pares e ímpares

numbers = [[], []]

for i in range(1,8):
    values = int(input("Digite um valor: "))
    if values % 2 == 0:
        numbers[0].append(values)
    else:
        numbers[1].append(values)
print(f"Valores pares: {sorted(numbers[0])}\nValores ímpares: {sorted(numbers[1])}")

