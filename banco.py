__author__ = 'Walter'
contas = [0] * 10
saldos = [0.0] * 10
proxlivre = 0
#entradas....
for i in range(10):
    repete = True
    while repete == True:
        print("Digite o novo numero da conta:")
        novonumero = int(input())
        achou = False
        for j in range(10):
            if novonumero == contas[j]:
                achou = True
                print("Numero duplicado")
                break
        if achou == False:
            contas[proxlivre] = novonumero
            print("Digite o saldo da conta")
            saldos[proxlivre] = float(input())
            proxlivre = proxlivre + 1
            repete = False

#menu
opcao = 0

while(opcao != 4):
    print("1 - Deposito")
    print("2 - Saque")
    print("3 - Consultar ativos do banco")
    print("4 - Finalizar programa")
    print("Digite a opcao desejada")
    opcao = int(input())
    if opcao == 1:
        print ("...Deposito...")
    else:
        if opcao == 2:
            print ("...Saque...")
        else:
            if opcao == 3:
                print ("...Consulta...")

