#Programa que calcula área de uma parede e quanta tinta necessária para pinta-la

largura = float(input("Digite  a largura da parede ( m²):  "))
altura = float(input("Digite a altura da parede (m²): "))

print(f"A área da parede é {largura * altura}  m²\n Quantidade de tinta necessária para pinta-la: {(largura * altura)/2:.2f} litros")