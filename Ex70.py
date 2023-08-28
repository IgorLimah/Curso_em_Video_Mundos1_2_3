#Código que lê o nome, preços de produtos. Pergunta se deseja continuar lendo e mostre o total das compras, quantos produtos
#custam mais que 100,00 e nome do produto mais barato

total = 0
max_price = 0
name_price = ''

while True:
    product_name = str(input("Nome do Produto: "))
    product_price = float(input("Preço do Produto:R$ "))
    total += product_price

    if product_price > 1000:
        max_price += 1

    if product_price < 100:
        name_price = product_name

    stop_cont = str(input("Deseja continuar [S/N]: ").upper())
    if 'N' in stop_cont:
        break

print(f"Total Gastos: R$ {total:.2f}\n{max_price} produtos custam mais de R$ 1.000,00\n{name_price} foi o produto mais barato")





