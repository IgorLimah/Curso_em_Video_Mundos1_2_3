#Programa que leia o âgulo qualquer e mostre na tela o valor do seno e cosseno e tangente do ângulo

import math

angulo = float(input("Digite o valor do ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O ângulo de {angulo}° tem:\nSeno de {seno:.2f}\nCosseno de {cosseno:.2f}\nTangente de {tangente:.2f} ")
