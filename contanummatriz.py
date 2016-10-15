__author__ = 'Walter'

numeros = [[0] * 5 for x in range(3)]

for linha in range(3):
    for col in range(5):
        print("Digite um numero l:", linha , " c:", col)
        numeros[linha][col] = int(input())
print("Linha - Coluna")
for linha in range(3):
    for col in range(5):
        print(numeros[linha][col], end=" ")
    print()

print("Coluna - Linha")
for col in range(5):
    for linha in range(3):
        print(numeros[linha][col], end=" ")
    print()

contador = 0
for linha in range(3):
    for col in range(5):
        if numeros[linha][col] >= 15 and \
            numeros[linha][col] <= 20:
            contador = contador + 1
print("A soma dos numeros entre 15 e 20 e:", contador)