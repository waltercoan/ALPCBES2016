__author__ = 'Walter'
sexo = [' '] * 5
corolho = [' '] * 5
corcabelo = [' '] * 5
idade = [0] * 5

def entradadados():
    for i in range(5):
        print("Digite o sexo (m/f)")
        sexo[i] = input()
        print("Digite a cor do olho (a/c/v)")
        corolho[i] = input()
        print("Digite a cor do cabelo (l/p/c)")
        corcabelo[i] = input()
        print("Digite a idade")
        idade[i] = int(input())
'''
Determine, por meio de outra funcao,
a media de idade das pessoas com
olhos castanhos e cabelos pretos.
Mostre esse resultado no programa principal.
'''
def mediaidade():
    soma = 0
    conta = 0
    for i in range(5):
        if(corolho[i] == 'c' and corcabelo[i] == 'p'):
            soma = soma + idade[i]
            conta = conta + 1

    media = soma / conta
    return media
#main - codigo principal
'''
Faca uma funcao que determine e devolva
ao programa principal a maior idade entre os habitantes.
'''
def maioridade():
    omaior=0
    corolhomaior = ''
    for i in range(5):
        if omaior < idade[i]:
            omaior = idade[i]
            corolhomaior = corolho[i]
    return omaior , corolhomaior

'''
Faca uma funcao que determine e
devolva ao programa principal a
quantidade de individuos do sexo
feminino cuja idade está entre
18 e 35 (inclusive) e que tenham
olhos azuis e cabelos louros.
'''
def contador():
    cont = 0
    for i in range(5):
        if sexo[i] == 'f' and \
            (idade[i] >= 18 and idade[i] <= 35) and \
            corolho[i] == 'a' and corcabelo[i] == 'l':
            cont = cont + 1
    return cont

entradadados()
mediacalc = mediaidade()
print("A media e", mediacalc)
maior, o = maioridade()
print("A maior idade e: ", maior)
print("E a cor do olho e", o)
ct = contador()
print("O numero de pessoas do sexo feminino " +
      "com idade 18 e 35 anos com cor do olho azul " +
      "e cabelo loiro e: ", ct)

