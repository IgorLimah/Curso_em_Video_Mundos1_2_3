#Código que mostra a tabuada de um número

print('-=' * 11)

print("GERADOR DE TABUADAS")

print('-=' * 11)

number = int(input("Digite o número para gerar a tabuada: "))
print()
print(f"A tabuada de {number} é:")
print()
for i in range(0, 11, 1):
        print(f'{number} x {i} = {number * i}')

exit()
