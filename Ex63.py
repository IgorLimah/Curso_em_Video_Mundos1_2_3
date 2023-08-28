#Código que lê um número n inteiro e mostre os primeiros elementos de Fibonacci.

fib_sequence = []
a,b = 0,1
i = 0

n = int(input("Digite quantos números da sequência deseja gerar? "))

for i in range(n):
    fib_sequence.append(a)
    a,b = b, a+b

print(fib_sequence)