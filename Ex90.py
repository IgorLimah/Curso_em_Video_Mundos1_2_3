#Código que lê o nome, média e situação guardando em dicionário.

student = dict()
student['Nome'] = str(input("Nome: "))
student['Media'] = float(input(f"Média de {student['Nome']}: "))

if student['Media'] >= 7:
    student['situação'] = 'Aprovado'
elif 5 <= student['Media'] < 7:
    student['situação'] = 'Recuperação'
else:
    student['situação'] = 'Reprovado'

for k, v in student.items():
    print(f"{k}: {v}")

exit()


