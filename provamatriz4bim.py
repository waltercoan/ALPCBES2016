__author__ = 'Walter'
qtd = [[0] * 4 for x in range(5)]
preco = [[0] * 4 for x in range(5)]
tempo = [[0] * 4 for x in range(5)]

for lin in range(5):
    print("linha" , lin+1)
    for col in range(4):
        print("col" , col+1)
        print("Digite a quantidade")