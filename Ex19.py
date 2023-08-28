#Programa que monta uma lista e sorteia um nome.

import random

students_names = []

for i in range(4):
    name = str(input("Digite o nome do aluno(a): "))
    students_names.append(name)

random_name = random.choice(students_names)
print(f"O aluno sorteado para apagar o quadro é {random_name}")

exit()