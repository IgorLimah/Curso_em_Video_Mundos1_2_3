#Código que lê 6 números inteiros e mostre a soma somente dos pares

summ = 0

for i in range(6):
    numbers = int(input("Digite um valor: "))
    if numbers % 2 == 0:
        summ += numbers
print(f"A soma dos valores pares é {summ}")

exit()
