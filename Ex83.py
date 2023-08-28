#Código que analisa uma expressão matemática

expression = str(input("Digite a expressão: "))
list = []

for sim in expression:
    if sim == '(':
        list.append('(')
    elif sim == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break
if len(list) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")


