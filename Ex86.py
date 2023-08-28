#Código que lê uma matriz de 3x3 dimensões e preencha a matriz com valores inputados, print a matriz

numbers = [[], [], []]

for i in range(1,4):
    line_0 = int(input("Digite a linha 1: "))
    numbers[0].append(line_0)
for i in range(1,4):
    line_1 = int(input("Digite a linha 2: "))
    numbers[1].append(line_1)
for i in range(1,4):
    line_2 = int(input("Digite a linha 3: "))
    numbers[2].append(line_2)

formatted_numbers = [[f"[{value}]" for value in line] for line in numbers]

for line in formatted_numbers:
    print(' '.join(line))



