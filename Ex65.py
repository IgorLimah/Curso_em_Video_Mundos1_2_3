#Código que leia vários numero inteiros  e mostre a média, maior e menor
answer = 'S'
soma = 0
quantity = 0

while answer in 'S':
    numbers = int(input("Digite um valor: "))
    soma += numbers
    quantity += 1

    answer = str(input("Deseja continuar? [S/N]: ").upper())

print(f"Soma: {soma}\nMédia {soma / quantity}")

exit()
