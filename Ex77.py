#Código tupla com várias palavras, mostrando quais são as vogais das palavras

tuple_words = ('Fe', 'Acreditar','Tudo', 'Possivel', 'Para', 'Quem', 'Acredita', 'Eu', 'Acredito', 'Vou', 'Conseguir',
               'Que', 'Desejo', 'utilizar', 'Esperança', 'Hope', 'Chuva', 'Cafe', 'Aula', 'Matematica')

vowels = ('a', 'e', 'i', 'o', 'u')

for word in tuple_words:
    found_vowels = []
    for letter in word:
        if letter.lower() in vowels:
            found_vowels.append(letter)
    if found_vowels:
        print(f"A palavra {word.upper()} tem as seguintes vogais: {' '.join(found_vowels)}")
    else:
        print(f"A palavra {word.upper()} não tem vogais")

exit()
