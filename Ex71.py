#Código que simula o funcionamento de um caixa eletrônico

notas_50 = notas_20 = notas_10 = notas_1 = 0

while True:
    value = int(input("Qual valor a ser sacado? R$ "))
    if value <= 0:
        print("Dado inválido!")
        continue

    if value >= 50:
        notas_50 = value // 50
        value %= 50
    if value >= 20:
        notas_20 = value // 20
        value %= 20
    if value >= 10:
        notas_10 = value // 10
        value %= 10
    if value >= 1:
        notas_1 = value

    break

print(f"Notas de R$ 50: {notas_50}\nNotas de R$ 20: {notas_20}\nNotas de R$ 10: {notas_10}\nNotas de R$ 1: {notas_1}")





