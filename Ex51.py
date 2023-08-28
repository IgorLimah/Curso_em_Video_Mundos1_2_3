#Código que lê o primeiro termo de PA e a razão e mostre os 10 primeiros termos
n = 0
print('-=' * 11)

print("PROGRESSÃO ARITMÉTICA")

print('-=' * 11)

first_term = int(input("Digite o primeiro termo: "))
reason = int(input("Digite a razão da PA: "))

print()

print("Os 10 primeiros termos da Progressão Aritmética são: ")

print()

for i in range(1, 11):
    term = first_term + (i - 1) * reason
    print(term, end=' → ')

exit()


