#Programa que Lê um número e mostra a sua tabuada

m = int(input('Digite o número para ver sua tabuada: '))

for i in range(0, 11, 1):
    print(f'{m} x {i} = {m * i}')