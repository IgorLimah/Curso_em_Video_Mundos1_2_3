#Código que lê o peso de 5 pessoas o mostre o qual foi o maior e qual foi o menor

greater_weight = 0
lower_weight = 300

for i in range(5):
    weight = float(input("Digite o peso: "))
    if weight > greater_weight:
        greater_weight = weight
    elif weight < lower_weight:
        lower_weight = weight
print(f"O menor peso foi {lower_weight}\nO maior peso foi {greater_weight}")

exit()


