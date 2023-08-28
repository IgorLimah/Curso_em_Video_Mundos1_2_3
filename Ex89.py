#Código que lê nome e 2 notas de vários alunos. Printa média de cada um dos alunos, notas individuais

file_student = [[], [], []]

while True:
    name = str(input("Nome: "))
    file_student[0].append(name)
    grade1 = float(input("Nota 1: "))
    grade2 = float(input("Nota 2: "))
    average = (grade1 + grade2) / 2
    file_student[1].append(average)  # Armazena a média na segunda lista
    file_student[2].append([grade1, grade2])
    stop = str(input("Deseja continuar? [S/N] "))
    if stop.upper() == 'N':
        break

print("Nome                  Média")
for i, (name, average, _) in enumerate(zip(*file_student)):
    print(f"{name:<20}{average:>8.1f}")

while True:
    print("\nExibir dados por Aluno:")
    answer = input("Digite o nome do aluno ou 0 para encerrar: ")

    if answer == '0':
        break

    if answer in file_student[0]:
        index = file_student[0].index(answer)  # Encontra o índice do aluno na lista de nomes
        grades = file_student[2][index]  # Recupera as notas do aluno pelo índice
        print(f"Notas do aluno {answer}: {grades[0]}, {grades[1]}")
    else:
        print("Aluno não encontrado.")
