#Código que leia o sexo de pessoas nos valores M/F.

sex = str(input("Digite o sexo (M/F) ou digite 0 para encerrar:  ")).upper()

while sex != "M" and sex != "F":
    print("Resposta inválida, digite novamente!")
    sex = str(input("Digite o sexo (M/F) ou digite 0 para encerrar:  ")).upper()

exit()
