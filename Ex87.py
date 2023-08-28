#Código que lê uma matriz de 3x3 dimensões e preencha a matriz com valores inputados, print a matriz, soma de todos
#os números pares, soma dos valores da terceira coluna, o maior valor da segunda linha


numbers = [[], [], []]
counter_line0 = 0
counter_line1 = 0
counter_line2 = 0
counter_total = 0
sum_line2 = 0

for i in range(1,4):
    line_0 = int(input("Digite a linha 1: "))
    numbers[0].append(line_0)
    if line_0 % 2 == 0:
        counter_line0 += line_0

for i in range(1,4):
    line_1 = int(input("Digite a linha 2: "))
    numbers[1].append(line_1)


    if line_1 % 2 == 0:
        counter_line1 += line_1

for i in range(1,4):
    line_2 = int(input("Digite a linha 3: "))
    numbers[2].append(line_2)
    sum_line2 += line_2
    if line_2 % 2 == 0:
        counter_line2 += line_2

formatted_numbers = [[f"[{value}]" for value in line] for line in numbers]
counter_total = (counter_line0 + counter_line1 + counter_line2)
max_line1 = max(numbers[1])

for line in formatted_numbers:
    print(' '.join(line))

print(f"Soma dos valores pares: {counter_total}\nSoma dos valores 3ª coluna: {sum_line2}\nMaior valor da segunda linha: {max_line1}")


