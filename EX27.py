#Programa que lê um nome completo e mostre o primeiro e o último nome separadamente

name = str(input('Digite uma frase: ')).upper().split()

if len(name) > 1:
    first_name = name[0]
    last_name = name[-1]
    print(f"Primeiro Nome: {first_name}\nÙltimo nome: {last_name}")