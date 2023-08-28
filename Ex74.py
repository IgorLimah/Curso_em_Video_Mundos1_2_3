#Código que gere 5 números em um tupla e mostre a listagem, maior e menor

from random import randint

numbers = tuple(randint(1,100) for _ in range(5))
print(f"{numbers}\nMaior: {max(numbers)}\nMenor: {min(numbers)}")

exit()

