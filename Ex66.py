#Código que leia vários números inteiros e pare com o valor 999 e some os números.

counter = 0
soma = 0
while True:
    numbers = int(input("Digite um valor: "))
    if numbers == 999:
        break
    soma += numbers
    counter += 1
print(f"A soma dos {counter} valores é = {soma}")
