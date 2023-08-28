#Código que lê um número inteiro e converte pra binário, octadecimal e hexadecimal

number = int(input("Digite um número: "))
i= -1
while i != 0:
    choice = int(input("Digite 1 para converter em binário\n2 para converter para Octadecimal\n3 para converter para Hexadecimal\nOu digite 0 para encerrar: "))
    if choice == 0:
        break
    elif choice == 1:
        print(f"O número {number} convertido para binário é {bin(number)}")
    elif choice == 2:
        print(f"O número {number} convertido para octadecimal é {oct(number)}")
    elif choice == 3:
        print(f"O número {number} convertido para hexadecimal é {hex(number)}")
print("Programa encerrado, obrigado por usar.")
exit()

