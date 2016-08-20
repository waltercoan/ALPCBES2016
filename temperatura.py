__author__ = 'Walter'
temp = [0]  * 12
meses =[ "Jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
maiortemp=0
mesmaior=0
menortemp=0
mesmenor=0
for m in range(0,12):
    print("Digite a temperatura do mes ", meses[m])
    temp[m] = float(input())

for m in range(0,12):
    if temp[m] > maiortemp:
        maiortemp = temp[m]
        mesmaior = m
    if m ==0:
        menortemp = temp[m]
        mesmenor = m
    else:
        if temp[m] < menortemp:
            menortemp = temp[m]
            mesmenor = m

print( "No mes", meses[mesmaior], " aconteceu a maior temperatura ",
        " de ", maiortemp, " graus")

print( "No mes", meses[mesmenor], " aconteceu a menor temperatura ",
        " de ", menortemp, " graus")