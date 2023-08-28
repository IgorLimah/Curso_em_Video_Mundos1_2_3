#Código tupla que tenha nome produtos e preços. Imprima os dados organizados em forma tabular

product_list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90 )

print('-' * 45)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 45)
for i in range(0, len(product_list), 2):
    item = product_list[i]
    price = product_list[i + 1]
    dots = '.' * (35 - len(item))
    print(f"{item}{dots}R$ {price:.2f}")
print('-' * 45)

exit()


