#Código que recebe um valor entre 0 a 20 e armazene o em uma tupla.

while True:
    numbers_word = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                    'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    number = int(input("Digite um número entre 0 e 20: "))

    if 0 <= number <= 20:
        number_word = numbers_word[number]
        print(f"Você digitou o número {number_word}")
    else:
        print("Número inválido, digite um número entre 0 e 20. ")
exit()
