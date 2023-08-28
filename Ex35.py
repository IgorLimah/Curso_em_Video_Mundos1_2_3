#Código que lê o comprimento de 3 retas e diga se elas formam um triângulo ou não

a,b,c = list(map(int,input("Digite os números: ").split()))

if a+b > c and a+c > b and b+c > a:
    print("As retas formam um triângulo!")
else:
    print("As retas não formam um triângulo!")