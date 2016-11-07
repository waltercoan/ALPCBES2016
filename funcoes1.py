__author__ = 'Walter'

def minhafuncao(pa, pb, pc):
    if pa > 1:
        soma=0
        cont=pb
        while(cont < pc-1):
            cont = cont + 1
            if cont % pa == 0:
                soma = soma + cont
            print(cont, end=' - ')

        print("PA", pa, " PB", pb, " PC", pc)
        return soma

print("Digite um numero")
x = int(input())
print("Digite um numero")
y = int(input())
print("Digite um numero")
z = int(input())
pegarvalor = minhafuncao(x, y, z)
print("Soma", pegarvalor)