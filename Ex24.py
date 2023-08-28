#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

city = str(input("Digite o nome da cidade: "))
list_city = []
list_city.append(city)

if city.lower().startswith("santo"):
     print("Verdadeiro")
else:
    print("Falso")

print(city[:5].lower() == "Santo")