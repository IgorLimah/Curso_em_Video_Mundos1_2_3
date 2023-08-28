#Código que mostra a média da idade e qual o nome do mais velho e qual mulher tem menos de 20 anos

oldest_man = 0
name_oldest = ""
count_women = 0
count_age = []

for i in range(4):
    name = str(input("Nome: "))
    age = int(input("Idade: "))
    sex = str(input("Sexo (M/F): "))

    if sex.upper() == "F":
        if age < 20:
            count_women += 1
    elif sex.upper() == "M":
        if age > oldest_man:
            oldest_man = age
            name_oldest = name

    count_age.append(age)

average_age = sum(count_age) / 4
print(
    f"A média de idade do grupo é {average_age:.1f}\nO nome do homem mais velho é {name_oldest}\nHá {count_women} mulheres menores de 20 anos.")

exit()

