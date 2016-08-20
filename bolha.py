__author__ = 'Walter'
numeros = [9,8,7,3,2,2,5,10,294,2,5,635728,6]

for i in range(0,len(numeros)-1):
    print(numeros[i],end="-")
    for j in range(i+1,len(numeros)):
        print(numeros[j], end=" ")
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
            #numeros[i],numeros[j] = numeros[j],numeros[i]


    print()
#sorted(numeros)
print("Ordenado: ", numeros)