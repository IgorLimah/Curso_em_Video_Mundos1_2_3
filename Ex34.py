#Programa que pergunta o salário de um funcionário e calcule o valor do seu aumento

wage = float(input("Digite o valor do salário: "))

if wage > 1250.00:
    print(f"O aumento no salário é de 10% e o novo valor do salário é R$ {(wage * 0.1) + wage:.2f}")
else:
    print(f"O aumento no salário é de 15% e o valor do salário é R$ {(wage * 0.15) + wage:.2f} ")

exit()