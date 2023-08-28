#Programa que lê o salário de um funcionário e mostre seu novo valor com acréscimo de 15%

salario = float(input("Digite o salário: R$ "))
print(f"Salário com acréscimo de 15%: R$ {salario + (salario * 0.15):.2f}")


