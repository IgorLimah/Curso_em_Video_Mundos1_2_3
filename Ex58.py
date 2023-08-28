#Programa que gera aletoriamente de 0 a 5 números e o usuário tenta adivinhar qual foi o número gerado. Imprima se o usuário acertou ou errou
import random
from time import sleep
count_error = 0

print("Pensei um número, você é capaz de advinha-lo: ")

number = int(input("Digite o número que você acha que pensei: "))

sort_number = random.randint(1,5)

print("Processando....")
sleep(2)

while number != sort_number:
    print(f"Ah que pena você errou!")
    number = int(input("Digite o número que você acha que pensei: "))
    count_error += 1

if number == sort_number:
    print(f"Pensei no número {sort_number}. Você precisou de {count_error} tentativas para acertar.  Parabéns, você acertou o número que pensei!!!")

exit()
