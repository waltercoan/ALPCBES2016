__author__ = 'Walter'
#Cria matriz com 5 linhas e 4 colunas
vendas = [ [0] * 4 for i in range(5)]

for linha in range(5):
    print("Vendedor: " , linha)
    for coluna in range(4):
        print("Semana", coluna, end=" ")
        print("Digite o valor")
        vendas[linha][coluna] = float(input())

    print()
#O total de vendas do mes de cada vendedor
totalvend = 0
for linha in range(5):
    for coluna in range(4):
        totalvend = totalvend + vendas[linha][coluna]
    print("O total do mes e", totalvend, " do vend: ", linha)
    totalvend = 0

#O total de vendas de cada semana
# (todos os vendedores juntos por semana)
totsemana=0
for coluna in range(4):
    for linha in range(5):
        totsemana = totsemana + vendas[linha][coluna]
    print("O total e:" , totsemana, " na semana", coluna)
    totsemana = 0

#O TOTAL DE VENDAS DO MES!!!!!!
totalgeral = 0
for linha in range(5):
    for coluna in range(4):
        totalgeral = totalgeral + vendas[linha][coluna]
print("O total geral é", totalgeral)
