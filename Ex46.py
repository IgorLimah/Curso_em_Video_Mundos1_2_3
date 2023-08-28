#Código que conta regressivamente de 10 até 0

from time import sleep

print("O estouro de foguetes começará em:")

for i in range(10, -1, -1):
    print(f'{i}')
    sleep(1)

print(f"{'-=' * 11}\nBOOOOM    BOOOOM\n{'-=' * 11}")

exit()
