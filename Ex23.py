#Programa que leia um número com 4 casas decimais e mostre na tela cada um dos dígitos separados

number = int(input("Digite um número: "))

#print(f"Unidade: {number[3]}\nDezena: {number[2]}\nCentena: {number[1]}\nMilhar: {number[0]}")

print(f"Unidade: {number //1 % 10 }\nDezena: {number // 10 % 10}\nCentena: {number // 100 % 10}\nMilhar: {number // 1000 % 10}")
exit()
