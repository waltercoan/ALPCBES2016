__author__ = 'Walter'
maisalto=0
maisbaixo=0
somaaltf=0
contf=0
sexomaisalto = ""
for pessoa in range(0,10):
    print("Pessoa: ", pessoa+1)
    print("Digite a altura")
    altura = float(input())
    print("Digite o sexo M/F")
    sexo = input()

    if sexo == 'f' or sexo == 'F':
        #acumulador
        somaaltf = somaaltf + altura
        #contador
        contf = contf + 1

    if altura > maisalto:
        maisalto = altura
        sexomaisalto = sexo


    if pessoa == 0:
        maisbaixo = altura
    else:
        if altura < maisbaixo:
            maisbaixo = altura

print("A altura do mais alto da turma e: %.2f" % maisalto)
print(" e o seu sexo e: ", sexomaisalto)

print("A altura do mais baixo da turma e: %.2f" % maisbaixo)
mediaaltf = somaaltf / contf
print("A media da altura das mulheres e: %.2f" % mediaaltf)
contm = 10 - contf
print("O numero de homens e: ", contm)
