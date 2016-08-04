__author__ = 'Walter'
vetor1 = [0,0,0,0,0,0,0,0,0,0]
vetor2 = [0] * 10 #so o python faz isso por voce
intercala = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
    print("Digite um numero")
    vetor1[i] = int(input())

for i in range(0,10):
    print("Digite um numero")
    vetor2[i] = int(input())

proxlivre = 0
for i in range(0,10):
    intercala[proxlivre] = vetor1[i]
    proxlivre = proxlivre + 1
    intercala[proxlivre] = vetor2[i]
    proxlivre = proxlivre + 1

for umnumero in intercala:
    print(umnumero,end=" ")