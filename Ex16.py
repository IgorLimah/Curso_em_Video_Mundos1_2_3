#Programa que leia um número real e mostre sua porção inteira

import math

number = float(input("Digite um número real: "))

print(f"A parte inteira de {number} é {math.trunc(number)}")

exit()
