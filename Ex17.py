#Programa que leia o comprimento do cateto oposto e adjacente e calcule a hipotenusa

import math

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adj = float(input("Digite o cateto adjacente: "))
hipotenusa = (math.hypot(cateto_oposto, cateto_adj))

# metodo matemático tradicional: print(f"A hipotenusa tem valor de {(cateto_oposto **2 + cateto_adj **2) **(0.5):.2f} ")

print(f"A hipotenusa tem valor de {hipotenusa:.2f} ")

exit()
