dados = [[0] * 3 for x in range(5)]

#Entrada de dados das quantidades
for linha in range(4):
    print("Armazem: ", linha + 1)
    for col in range(3):
        print("Produto: ", col + 1)
        dados[linha][col] = int(input())

#Entrada de dados dos valores
for col in range(3):
    print("Digite o valor do produto:")
    dados[4][col] = float(input())

# A quantidade de itens  armazenados em cada armazem
totalarm=0
for lin in range(4):
    print("Armazem: ", lin+1)
    for col in range(3):
        totalarm = totalarm + dados[lin][col]
    print("Total armazem e:", totalarm)
    totalarm = 0

#Qual o armazem possui maior estoque do produto 2
omaior=0
armdomaior = 0
for lin in range(4):
    if dados[lin][1] > omaior:
        omaior = dados[lin][1]
        armdomaior = lin
print("O armazem ", armdomaior , end=' - ')
print(" possui a maior qtd de ", omaior)

#Qual o armazem possui menor estoque
''' Versão da sala de aula
omenor=0
armmenor=0
for lin in range(4):
    for col in range(3):
        if lin == 0 and col == 0:
            omenor = dados[lin][col]
            armmenor = lin
        else:
            if dados[lin][col] < omenor:
                omenor = dados[lin][col]
                armmenor = lin
print("o armazem ", armmenor, end=' ')
print(' possui a menor qtd de', omenor)
'''

#Correção do algoritmo
omenor=0
armmenor=0
soma = 0
for lin in range(4):
    for col in range(3):
        soma += dados[lin][col]
    if lin == 0:
        omenor = soma
        armmenor = lin
    else:
        if soma < omenor:
            omenor = soma
            armmenor = lin
    soma = 0
print("o armazem ", armmenor, end=' ')
print(' possui a menor qtd de', omenor)



#Qual o custo total de cada produto
somaprod=0
valtotprod=0
for col in range(3):
    for lin in range(4):
        #somaprod = somaprod + dados....
        somaprod += dados[lin][col]
    valtotprod = somaprod * dados[4][col]
    print("O custo total e: ", valtotprod)
    print("do produto" , col + 1)
    somaprod = 0










