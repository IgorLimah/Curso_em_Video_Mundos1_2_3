#Programa que leia no nome completo de uma pessoa e mostre: O nome com todas a letras maísculas, mínúsculas ,
# quantas letras tem ao todo e quantas tem o primeiro nome


full_name = str(input("Digite o nome: ")).strip()
name_up = full_name.upper()
name_low = full_name.lower()
first_name = full_name[0]

print(f"Seu nome em maíusculo é : {name_up}\nSeu nome em mínúsculo é: {name_low}\nSeu nome tem {len(full_name)} Letras\nSeu primeiro nome tem {(full_name.find(''))} letras")

exit()


