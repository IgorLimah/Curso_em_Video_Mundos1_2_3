#Função chamada contador(). Recebe 3 parâmetros: Início, fim, passo. Realiza 3 contagens: 1, 10, 1 - 10, 0 , 2 - Person.

from time import sleep

def counter(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1

    print(f"Contagem de {start} até {end} de {step} em {step}")
    print('-=' * 20)

    cont = start

    if start < end:
        while cont <= end:
            print(f"{cont}", end=' ')
            sleep(0.7)
            cont += step
        print()
        print('-=' * 20)
    else:
        cont = start
        while cont >= end:
            print(f"{cont}", end=' ')
            sleep(0.7)
            cont -= step
        print()
        print('-=' * 20)

#programa principal:

counter(1, 10, 1)
counter(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")

start = int(input("Início:   "))
end = int(input("Fim:        "))
step = int(input("Intervalo: "))
counter(start, end, step)