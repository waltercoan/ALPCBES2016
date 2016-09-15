__author__ = 'Walter'

ceps = [0] * 11
valores = [0.0] * 11
atend = [False] * 11

for i in range(11):
    #print("%d horas" % (8+i))
    print(8+i)
    print("Digite o CEP")
    ceps[i] = int(input())
    print("Digite o valor")
    valores[i] = float(input())
    print("Digite se atend realizado [sim/nao]")
    #atend[i] = (input() == "sim")
    if input() == "sim":
        atend[i] = True
    else:
        atend[i] = False
'''
qual o CEP do atendimento que irá render o
maior valor para o chaveiro
e o CEP do atendimento irá render o menor
valor para o chaveiro?
'''
omaior=0
cepdomaior=0
omenor=0
cepdomenor=0
for i in range(11):
    if atend[i]:
        if valores[i] > omaior:
            omaior = valores[i]
            cepdomaior = ceps[i]
        if i == 0:
            omenor = valores[i]
            cepdomenor = ceps[i]
        else:
            if valores[i] < omenor:
                omenor = valores[i]
                cepdomenor = ceps[i]
print("O maior valor pago e: ", omaior)
print("no CEP: ", cepdomaior)
print("O menor valor pago e: ", omenor)
print("no CEP: ", cepdomenor)

'''
quantos atendimentos foram perdidos no dia
e quanto dinheiro o chaveiro deixou de receber? '''

contfalhou=0
somaperdas=0
for i in range(11):
    if atend[i] == False:
        contfalhou = contfalhou + 1
        somaperdas = somaperdas + valores[i]
print("Foram perdidos ", contfalhou, " atendimentos")
print("totalizando o valor de ", somaperdas)

'''liste em tela uma nova agenda do próximo dia de
trabalho do chaveiro para atender sequencialmente
as casas que não foram atendidas no dia anterior.'''

for i in range(11):
    if atend[i] == False:
        print("CEP: ", ceps[i], "Valor: ", valores[i])





