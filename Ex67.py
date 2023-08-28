#Código que mostre a tabuada de vários números, um de cada vez. Código stop quando valor for negativo

while True:
    numbers = int(input("Digite um número para ver sua tabuada: "))
    if numbers < 0:
        break

    for i in range(0, 11, 1):
        print(f'{numbers} x {i} = {numbers * i}')

exit()
