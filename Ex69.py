#Código que mostra a média da idade e qual o nome do mais velho e qual mulher tem menos de 20 anos

count_age = 0
count_man = 0
count_women = 0

while True:
    age = int(input("Idade: "))
    sex = str(input("Sexo (M/F): "))

    if sex.upper() == "F":
        if age < 20:
            count_women += 1
    if sex.upper() == "M":
        count_man += 1
    if age > 18:
        count_age += 1
    answer = str(input("Deseja continuar? [S/N]").upper())
    if answer == 'N':
        break


print(f"O total de pessoas com mais de 18 anos:  {count_age}\nA quantidade de homens cadastrados é {count_man}\nHá {count_women} mulheres menores de 20 anos.")

exit()
