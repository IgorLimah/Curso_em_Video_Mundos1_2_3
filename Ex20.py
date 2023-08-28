#Programa que leia nomes e embaralha a ordem em um sorteio


students_names = []

for i in range(4):
    name = str(input("Digite o nome do aluno(a): "))
    students_names.append(name)

random_name = sorted(students_names)
print(f"A ordem de apresentação é  {random_name}")

exit()