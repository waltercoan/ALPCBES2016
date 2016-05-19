__author__ = 'Walter'
cont = 0
maisvelho = 0
maisnovo=0
while cont < 10:
    print("Digite a idade da crianca")
    idade = int(input())
    if idade > maisvelho:
        maisvelho = idade
    if cont == 0:
        maisnovo = idade
    else:
        if idade < maisnovo:
            maisnovo = idade
    cont = cont + 1
print("A crianca mais velha e", maisvelho)
print("A crianca mais nova e", maisnovo)
