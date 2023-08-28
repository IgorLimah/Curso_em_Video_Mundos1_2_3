#Programa que leia a velocidade de um carro, se a velocidade for maior que 80 o carro será multado e uma multa calculada a 7,00 por cada km excedente.

velocity = float(input("Digite a velocidade: "))

if velocity > 80:
  print(f"Veículo multado por ultrapassar o limite de 80 km/h\nA multa será de R$ {(velocity - 80) * 7:.2f}.")

else:
    print("Tenha um bom dia, dirija com segurança!")

exit()