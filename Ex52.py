#Código que lê um número e verifica se é primo

number = int(input("Digite um número: "))

count_divisors = 0

for i in range(1, number + 1):
    if number % i == 0:
        count_divisors += 1
if count_divisors == 2:
    print(f"O número {number} é um número primo.")
else:
    print(f"{number} não é um número primo")

exit()
