#Programa que leia 3 números e diga qual é o maior e menor

number = list(map(int,input("Digite os números: ").split()))
print(f"O maior número é {max(number)}\nO menor número é {min(number)}.")
