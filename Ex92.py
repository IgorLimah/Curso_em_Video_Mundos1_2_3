#Código que lê nome, ano de nascimento e carteira de trabalho e guarde em dicionário mostrando idade.Usuário com
#carteira de trabalho recebe ano de contratação e salário. Mostrar tempo que falta pra aposentar.

from datetime import datetime

current_year = datetime.now().year

data_person = dict()
data_person['Nome'] = str(input("Nome: "))
data_person['Idade'] = int(input("Ano de nascimento: "))
data_person['CTPS'] = int(input("Carteira de trabalho (Digite 0 caso não tenha CTPS): "))
data_person['Idade'] = (current_year - data_person['Idade'])


if data_person['CTPS'] != 0:
    data_person['Contratação'] = int(input("Ano de contratação: "))
    data_person['Salário'] = float(input("Salário: "))
    data_person['Ano de Aponsentadoria'] = data_person['Contratação'] + 35

print('-=' *30)

for k, v in data_person.items():
    print(f"{k}: {v}")


exit()
