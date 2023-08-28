#Código que Lê a idade de 7 pessoas e mostre quantas atingiram a maioridade

from datetime import date
actual_year = date.today().year
majority = 0
minor = 0

for i in range(7):
    born_year = int(input("Digite o ano de nascimento: "))
    if (actual_year - born_year) < 18:
        minor += 1
    elif (actual_year - born_year) > 18:
        majority += 1

print(f"O total de menores são {minor}\nO Total de maiores são {majority} ")

exit()

