__author__ = 'Walter'

numeros = [0] * 20
for i in range(20):
    print("Digite qualquer numero")
    numeros[i] = int(input())

#primeiro for inicia em zero ate penultima posicao
for i in range(0,19):
    #segundo for inicia na posicao posterior a primeira
    #ate a ultima posicao do vetor
    for j in range(i+1,20):
        if numeros[i] > numeros[j]:
            #troca de posicao
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
            #numeros[i],numeros[j] = numeros[j],numeros[i]


print("Digite o numero procurado:")
proc = int(input())

ini = 0
fim = 19
while(ini <= fim):
    meio = int((ini + fim)/2)
    print("Ini: ", ini, " Fim: ", fim, " Meio: ", meio)
    if proc == numeros[meio]:
        print("Achei!!! [", meio,"]")
        break
    else:
        if proc > numeros[meio]:
            ini = meio + 1
        else:
            if proc < numeros[meio]:
                fim = meio - 1







