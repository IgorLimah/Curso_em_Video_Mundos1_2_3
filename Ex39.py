#Código que lê o ano de nascimento e informa alistamento militar

from datetime import date

actual_year = date.today().year

born_year = int(input("Digite sua idade: "))

if (actual_year - born_year) < 18:
    print(f"Você ainda não pode se alistar, faltam {18 - (actual_year - born_year)} anos para poder se alistar!")
elif (actual_year - born_year) > 18:
    print(f"Você passou do prazo para se alistar em {(actual_year - born_year) - 18} anos. Aliste se imediatamente!")
else:
    print("Voce está na hora de se alistar!")