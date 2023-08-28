#Programa que leia a distência de uma viagem em km e calcule o preço da passagem cobrando 0,50 por km  para viagem até 200km
#e 0,45 pra viagens mais longas

distance = float(input("Digite a kilometragem da viagem: "))
print(f"A kilometragem digitado é {distance:.0f} km")
if distance <= 200:
    print(f"O preço da passagem para a distância de {distance:.0f} km é de R$ {(0.50 * distance):.2f}.")
else:
    print(f"O preço da passagem para a distância de {distance:.0f} km é de R$ {(0.45 * distance):.2f}.")
