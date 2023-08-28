#Código que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura/comprimento)
#e mostre a área do terreno

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"Controle de Terrenos".center(50, "-"))
    print(f"A área de um terreno {largura} x {comprimento} é de {area_terreno:.2f} m².")

largura = float(input("Largura (m²): "))
comprimento = float(input("Largura (m²): "))

area(largura, comprimento)

