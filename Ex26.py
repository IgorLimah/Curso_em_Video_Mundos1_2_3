#Programa que lê uma frase diga quantas vezes a letra "a" aparece, em que posição aparece a primeira vez e na última vez

phrase = str(input('Digite uma frase: ')).upper()

positions = []
for index, char in enumerate(phrase):
    if char == 'A':
        positions.append(index + 1)
print(f"A letra 'A' aparece nas posições: {positions}\nA palavra A aparece {phrase.count('A')} vezes.")
print(f"A primeira letra 'A' apareceu na posição {phrase.find('A')+1}\nA última letra 'A' apareceu na posição {phrase.rfind('A')}")

exit()