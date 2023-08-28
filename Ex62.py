n = 0
i = 1
print('-=' * 11)

print("PROGRESSÃO ARITMÉTICA")

print('-=' * 11)

first_term = int(input("Digite o primeiro termo: "))
reason = int(input("Digite a razão da PA: "))

print()

print("Os 10 primeiros termos da Progressão Aritmética são: ")

print()

while i < 11:
    term = first_term + (i - 1) * reason
    print(term, end=' → ')
    i += 1