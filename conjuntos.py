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
d = [0,0,0,0,0,0,0,0,0,0]
s = [0,0,0,0,0,0,0,0,0,0]
p = [0,0,0,0,0,0,0,0,0,0]
inter = [0,0,0,0,0,0,0,0,0,0]

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

proxlivre = 0
for i in range(0,10):
    achou = False
    for j in range(0,10):
        if x[i] == y[j]:
            achou = True
            break
    if achou == False:
        d[proxlivre] = x[i]
        proxlivre = proxlivre + 1
print("Diferenca: ", d)

for i in range(0,10):
    s[i] = x[i] + y[i]
print("Soma: ", s)

for i in range(0,10):
    p[i] = x[i] * y[i]
print("Produto: ", p)

proxlivre = 0
for i in range(0,10):
    for j in range(0,10):
        if x[i] == y[j]:
            inter[proxlivre] = x[i]
            proxlivre = proxlivre + 1
            break
print("Intersecao : ", inter)
