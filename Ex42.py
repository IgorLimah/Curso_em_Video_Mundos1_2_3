#Código que lê o comprimento de 3 retas e diga se elas formam um triângulo: Equilátero, Isóceles ou Escaleno

a,b,c = list(map(int,input("Digite os números: ").split()))

if a+b > c and a+c > b and b+c > a:
    print("As retas formam um triângulo!")

if a == b and b == c:
    print("O triângulo formado é do tipo Equilátero.")
elif a == b and b != c:
    print("O triângulo formado é do tipo Isóceles.")
else:
    print("O triângulo formado é do tipo Escaleno.")