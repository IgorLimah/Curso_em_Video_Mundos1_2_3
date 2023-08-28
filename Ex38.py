#Código que lê 2 valores e compares -os

value1, value2 = list(map(int, input("Digite os dois valores a serem comparados: ").split()))

if value1 > value2:
    print(f"O primeiro valor {value1} é o maior!")
elif value2 > value1:
    print(f"O segundo valor {value2} é o maior!")
else:
    print(f"Não existe valor maior, os dois valores {value1}, {value2} são iguais.")
