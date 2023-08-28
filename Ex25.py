#Programa que lê o nome de uma pessoa e diz se tem silva no nome

name = str(input('Digite um nome: ')).lower().split()

if "silva" in name:
    print(f"O nome tem Silva.")
else:
    print("O nome não tem Silva.")

exit()