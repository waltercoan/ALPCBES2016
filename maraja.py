__author__ = 'Walter'
salario = 0
perc = 0
for ano in range(1995,2017):
    if ano == 1995:
        salario = 1000
    if ano == 1996:
        perc = 1.5
    if ano >= 1997:
        perc = perc * 2
    valaumento = (salario * perc) / 100
    salario = salario + valaumento
    print("Ano: ", ano , " salario: ", salario)
