#Programa que gera aletoriamente de 0 a 5 números e o usuário tenta adivinhar qual foi o número gerado. Imprima se o usuário acertou ou errou
import random
from time import sleep
number = int(input("Digite o número que você irá adivinhar: "))
sort_number = random.randint(1,5)
print("Processando....")
sleep(2)

if number == sort_number:
    print("Parabéns! Você acertou o número que pensei.")
else:
     print(f"Ah que pena você errou! O número que pensei foi o {sort_number}! ")
