#Código que lê o ano de nascimento de um atleta e diga sua categoria de acordo com a idade

age = int(input("Digite a idade: "))

if age <=9:
    print("Categoria: MIRIM")
elif age > 9 and age <= 14:
    print("Categoria: INFANTIL")
elif age > 14 and  age <= 19:
    print("Categoria: JUNIOR")
elif age > 19 and age <= 20:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")

exit()
