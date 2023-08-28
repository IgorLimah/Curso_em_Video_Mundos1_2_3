#Programa que leia um número inteiro e mostre se par ou ímpar

from time import sleep

number = int(input("Digite um número: "))
print(f"Analisando o número {number}...... ")
sleep(2)
if number % 2 == 0:
    print(f"{number} é um número par!")
else:
    print(f"{number} é um número ímpar!")

exit()