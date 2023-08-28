#Código para aprovar empréstimo de casa

home_price = float(input("Digite o valor da casa: R$ "))
wages = float(input("Digite o valor do salário: R$ "))
years_pay = int(input("Digite em quantos anos será o pagamento da casa: "))

months_pay = (years_pay * 12)
price_pay = (home_price / months_pay)
wages_percent = (wages * 0.30)

if price_pay > wages_percent:
    print(f"Desculpe, empréstimo negado! As prestações ficam no valor de R$ {price_pay:.2f} e estão acima de 30% do seu salário: R$ {wages_percent:.2f}.")
else:
    print(f"Empréstimo aprovado! As prestações serão de R$ {price_pay:.2f} por {months_pay} meses.")