#função chamada maior que recebe vários parâmetros em inteiros e analisa qual é o maior

def find_max(*num):
    maximum = max(num)
    return maximum

values = []

while True:
    value = input("Digite um Valor ou  'stop' para encerrar: ")
    if value == 'stop':
        break
    values.append(int(value))

result = find_max(*values)

print(f"O maior valor é: {result}")

