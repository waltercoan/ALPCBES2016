__author__ = 'Walter'
#print("Linha 1",end="$$$")
#print("Linha 2")
#numeros = [10,20,70,120,2,33]
#print(len(numeros))
#print(numeros)
#for i in range(0,6):
#    numeros[i] = numeros[i] + 5
#    print(i, " ", numeros[i])
#print(numeros)

#numeros = [10,20,70,120,2,33]
#print("Digite o numero procurado")
#proc = int(input())
#achou = False
#for i in range(0,6):
#    if proc == numeros[i]:
#        print("Achou...")
#        achou = True
#        break
#if achou == False:
#    print("Nao achou...")

x = [0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0]
u = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    print("Digite um numero")
    x[i] = int(input())
for i in range(0,10):
    print("Digite mais um numero")
    y[i] = int(input())

for i in range(0,10):
    u[i] = x[i]

proxlivre = 10

for i in range(0,10):
    #print(y[i], end = " ")
    achou = False
    for j in range(0,10):
        #print(x[j],end=" ")
        if y[i] == x[j]:
            achou = True
            break
    if achou == False:
        u[proxlivre] = y[i]
        proxlivre = proxlivre + 1
    #print("")
print("Uniao: ", u)






