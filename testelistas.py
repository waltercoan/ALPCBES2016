__author__ = 'Walter'
#lista = [1,2,3,4]
#print("Primeiro",lista[0])
#print("Ultimo",lista[3])

lista = []
continua = 's'
while(continua == 's'):
    print("Digite o valor?")
    valor = float(input())
    lista.append(valor)
    print("Tem mais um? S/N")
    continua = input()

#print(lista)
soma = 0
omaior = 0
omenor = 0
#for umnumero in lista:
for i in range(0,len(lista)):
    #print(umnumero)
    if lista[i] > omaior:
        omaior = lista[i]

    if i == 0:
        omenor = lista[i]
    else:
        if lista[i] < omenor:
            omenor = lista[i]
    soma = soma + lista[i]

print("A soma total e: ", soma)
print("O maior e: ", omaior)

media = soma / len(lista)
print("A media dos valores e ", media)
