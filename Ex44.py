# Código que calcula do valor de um produto de acordo com a forma de pagamento

product_value = float(input("Valor do produto: R$ "))
pay_condition = int(input("Digite a condição de pagamento:\n1- Dinheiro - 10% de desconto\n2- A vista no cartão - 5% de desconto\n3- 2x no cartão - Sem desconto\n4- 3x ou mais no cartão - 20% de juros : "))

if pay_condition == 1:
    print(f"Total: R$ {product_value - (product_value * 0.1) }")
elif pay_condition == 2:
    print(f"Total: R$ {product_value - (product_value * 0.05)}")
elif pay_condition == 3:
    print(f"Total: R$ {product_value}")
else:
    print(f"Total: R$ {(product_value * 0.2) + product_value}")
