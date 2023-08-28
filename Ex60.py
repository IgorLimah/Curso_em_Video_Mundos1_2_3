#Código que lê um número e mostre o fatorial:
factor = 1
number = int(input("Digite um valor para ver o seu fatorial: "))
counter = number
while counter > 0:
    print(f"{counter}", end='')
    print("x" if number > 1 else " = ", end='')
    factor *= number
    counter -= 1


print(f"{factor,}", end='')

exit()
