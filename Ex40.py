#Programa que leia duas notas e mostre sua média: Reprovado: 5, Recuperaçao: 5.0-6.9 e Aprovado: 7+.

grade1, grade2 = list(map(float, input("Digite as suas notas 1 e notas 2: ").split()))

average = (grade1 + grade2)/2

if average <= 5:
    print(f" Média {average}. Você está reprovado!")
elif average >= 7:
    print(f" Média {average}. Você está aprovado!")
else:
    print(f" Média {average}. Você está de recuperação!")

exit()