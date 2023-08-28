# Código que lê 5 valores númericos e guarda-s em uma lista. Mostre o maior, menor com suas posições
numbers = []
for i in range(1, 6):
    value = int(input("Digite os valores: "))
    numbers.append(value)

print(f"Você digitou os valores {numbers}\nO maior valor digitado foi {max(numbers)} na posição {numbers.index(max(numbers)) + 1}\nO menor valor digitado foi {min(numbers)} na posição {numbers.index(min(numbers)) + 1}")

exit()
