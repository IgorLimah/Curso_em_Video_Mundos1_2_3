#Programa que lê o preço de um produto e mostre seu novo preço com desconto de 5%

preco = float(input("Digite  o preço do produto: R$  "))

print(f"O novo preço do produto é R$ {preco - (preco * 0.05):.2f}")