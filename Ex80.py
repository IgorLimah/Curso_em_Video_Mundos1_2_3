#Código que lê 5 valores e mostre em ordem crescente sem usar função sort
lista = []

position = 0
for c in range(0,5):
    numbers = int(input("Digite um valor: "))
    if c == 0 or numbers > lista[-1]:
        lista.append(numbers)
        print('Adicionado ao final da lista')
    else:
        position = 0
        while position < len(lista):
            if numbers <= lista[position]:
                lista.insert(position, numbers)
                print(f"Adicionado na posição {position} da lista")
                break
            position += 1
print(f"Os valores digitados em ordem foram {lista}")

