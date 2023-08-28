#Código que lê nome, sexo, e idade de várias pessoas. Guarde em dicionários e dicinários em lista
#Mostre a qtde de pessoas cadastradas, Média de idade, todas as mulheres, pessoas com idade acima média
# galera = list()
# pessoa = dict()
#galera.append(pessoa.copy())

data_person = {}
person_list = []
tot = 0
sum_age = 0
women = []
high_age = []

while True:
    name_person = str(input("Nome: "))
    person_list.append(name_person)
    sexo_person = str(input("Sexo [M/F]: ")).upper()
    person_list.append(sexo_person)
    age_person = int(input("Idade: "))
    tot += 1
    sum_age += age_person
    person_list.append(age_person)
    print()
    breaks = str(input("Deseja continuar: [S/N]: ")).upper()

    if breaks == 'N':
        break

data_person['Nome'] = person_list[0]
data_person['Sexo'] = person_list[1]
data_person['Idade'] = person_list[2]

average_age = (sum_age / tot)

if sexo_person == 'F':
    women.append(name_person)

if age_person > (sum_age / tot):
    high_age.append(person_list)

print(f"Quantidade pessoas Cadastradas: {len(person_list[0])}\nA média de idade: {average_age:.2f}\nMulheres cadastradas: {women}\nPessoas com idade acima da média: {high_age}")
