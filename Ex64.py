#Código que leia vários números com parada em 999 e exiba a soma dos números lidos
numbers = 0
soma = 0

while numbers != 999:
    numbers = int(input("Digite um valor: "))
    if numbers == 999:
        break
    soma += numbers
print(f"Soma: {soma}")

exit()

