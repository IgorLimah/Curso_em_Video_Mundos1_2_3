#Programa que calcula Lê a quantidade de dias de um carro alugado e km percorridos e calcula os valores

quantidade_dias = int(input("Quantidade de dias: "))
km_percorridos = float(input("KM percorridos: "))
print(f" Total a pagar: R$ {(quantidade_dias * 60) + (km_percorridos * 0.15):.2f}")