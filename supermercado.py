__author__ = 'Walter'
print("Digite o valor de venda media mensal")
vendmed = float(input())
print("Digite o preco atual")
precoa = float(input())

if vendmed < 500 or precoa < 30:
    #aumento
    novopreco = precoa + (precoa * 12 / 100)
    #aqui1
else:
    if (vendmed >= 500 and vendmed < 1600) \
        or (precoa >= 30 and precoa < 80):
        #aumento
        novopreco = precoa + (precoa * 15 / 100)
        #aqui2
    else:
        if vendmed >= 1600 or precoa >= 80:
            #desconto
            novopreco = precoa - (precoa * 25 / 100)
            #aqui3
print(" O novo preco e: %.2f" % novopreco)