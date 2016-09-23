ceps = [0] * 30;
codigos = [0] * 30;
qtds = [0] * 30;
valores = [0] * 30;

opcao = 0
proxlivre = 0
while(opcao != 5):
    print("1 - Registrar pedido")
    print("2 - Pedido mais caro e mais barato")
    print("3 - Contagem de pedidos")
    print("4 - Relatorio financeiro")
    print("5 - Sair")
    print("digite a opcao desejada")
    opcao = int(input())
    if opcao == 1:
        print("Registar um novo pedido")
        print("Digite o CEP")
        novocep = int(input())
        print("Digite o codigo do combo")
        novocodigo = int(input())
        print("Digita a quantidade do combo")
        novaqtd = int(input())
        if novocodigo == 10:
            novovalor = 20 * novaqtd
        if novocodigo == 30:
            novovalor = 60 * novaqtd
        if novocodigo == 50:
            novovalor = 90 * novaqtd

        ceps[proxlivre] = novocep
        codigos[proxlivre] = novocodigo
        qtds[proxlivre] = novaqtd
        valores[proxlivre] = novovalor

        proxlivre = proxlivre + 1

    if opcao == 2:
        print("Maior e menor valor")
        omaior = 0
        cepdomaior = 0
        for i in range(30):
            if valores[i] > omaior:
                omaior = valores[i]
                cepdomaior = ceps[i]
        print("O maior valor e ", omaior , " no CEP ", cepdomaior)
        omenor =0
        cepdomenor=0
        for i in range(30):
            if i == 0:
                omenor = valores[i]
                cepdomenor = ceps[i]
            else:
                if valores[i] < omenor:
                    omenor = valores[i]
                    cepdomenor = ceps[i]
        print("O menor valor e ", omenor , " no CEP ", cepdomenor)

    if opcao == 3:
        contaped10 = 0
        contaped30 = 0
        contaped50 = 0
        for i in range(30):
            if qtds[i] >= 2:
                if codigos[i] == 10:
                    contaped10 += 1
                if codigos[i] == 30:
                    contaped30 += 1
                if codigos[i] == 50:
                    contaped50 += 1
        print("A qtd do combo 10 e ", contaped10)
        print("A qtd do combo 30 e ", contaped30)
        print("A qtd do combo 50 e ", contaped50)

    '''
    iv.	Relatório financeiro: caso o usuário selecione esta opção
    o programa deverá calcular a média do valor total de pedidos
    pelo número total de pedidos já realizados.
    '''
