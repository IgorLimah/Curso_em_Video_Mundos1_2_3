#Código que calcule a soma de números impares multíplos de 3 de 1 á 500
summ = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        summ += i
print(f"Total da soma é {summ}")

exit()
