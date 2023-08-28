#Código que leia 4 valores e guarde-os em tupla, mostre quantas vezes apareceu 9, posição do 3 e os pares

values = ()

for i in range(4):
    value = int(input("Digite um valor: "))
    values += (value,)

print(f"O número 9 apareceu {values.count(9)} vezes")


if 3 in values:
    print(f"O número 3 apareceu primeira vez na {values.index(3) + 1}ª posição")
else:
    print("O número 3 não foi digitado nenhuma vez")

print("Os valores pares digitados foram ", end=' ')
for i in values:
    if i % 2 == 0:
        print(i, end=', ')


exit()



