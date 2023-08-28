#Faça um programa que converta medidas

n = float(input('Digite o valor da distância(m): '))

print(f'A medida corresponde a:\n{n/1000}Km\n{n/100}hm\n{n/10}dam\n{n*10}dm\n{n*100}cm\n{n*1000}mm')
print('Fim')