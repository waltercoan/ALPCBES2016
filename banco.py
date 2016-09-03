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
        #aqui comeca a logica do deposito
        print ("...Deposito...")
        print("Digite o numero da conta")
        contadepto = int(input())
        achou = False
        i=0
        for i in range(10):
            if contadepto == contas[i]:
                achou = True
                break
        if achou:
            print("Digite o valor do deposito")
            valdepto = float(input())
            saldos[i] = saldos[i] + valdepto
            print("Novo saldo de %.2f" % saldos[i])
            pass
        else:
            print("Numero da conta invalido...")
        #aqui termina a logica do deposito
    else:
        if opcao == 2:
            print ("...Saque...")
            #inicio da logica do saque
            print("Digite o numero da conta corrente:")
            contasaque = int(input())
            achou = False
            i=0
            for i in range(10):
                if contasaque == contas[i]:
                    achou = True
                    break
            if achou:
                print("Digite o valor do saque:")
                valsaque = float(input())
                if valsaque <= saldos[i]:
                    saldos[i] = saldos[i] - valsaque
                    print("Novo saldo e %.2f" % saldos[i])
                else:
                    print("Saldo insuficiente para saque")
            else:
                print("Numero da conta invalido")
            #fim da logica do saque
        else:
            if opcao == 3:
                print ("...Consulta...")
                for i in range(10):
                    print("Conta %d - Saldo %.2f" %
                          (contas[i], saldos[i]))
            else:
                print("Ate logo.. bye bye...")

