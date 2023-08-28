#Código que calcula o imc:

weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

imc = weight / (height * 0.01) ** 2

if imc < 18.5:
    print(f" Seu IMC é {imc:.2f}: Abaixo do Peso.")
elif imc >= 18.5 and imc <= 25:
    print(f"Seu IMC é {imc:.2f}: Peso Ideal.")
elif imc >= 25 and imc <= 30:
    print(f"Seu IMC é {imc:.2f}: Sobrepeso.")
elif imc >= 30 and imc <= 40:
    print(f"Seu IMC é {imc:.2f}: Obesidade.")
else:
    print(f"Seu IMC é {imc:.2f}: Obesidade Mórbida")