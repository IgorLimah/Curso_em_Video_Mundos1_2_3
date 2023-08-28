#Código que lê uma frase e diga se é políndromo.

word = input("Digite uma palavra: ").strip()

word_inverted = word[::-1]

if word == word_inverted:
    print(f"A palavra '{word}' é um palíndromo!")
else:
    print(f"A palavra '{word}' não é um palíndromo!")

exit()
