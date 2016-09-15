__author__ = 'Walter'
janela = [0] * 24
corredor = [0] * 24

contpassvend=0
while(contpassvend < 48):
    print("Digite opcao J-anela ou C-orredor?")
    opcao = input()
    if opcao == "j" or opcao == "J":
        #aqui vai a logica da janela
        print("Posicoes livres na janela:")
        for i in range(24):
            if janela[i] == 0:
                #print(i)
                print((i+1), end=" - ")
        print("Digite o numero da poltrona desejada?")
        poscompra = int(input())
        janela[poscompra-1] = 1
        contpassvend = contpassvend + 1
        pass
    else:
        #aqui vai a logica do corredor
        pass
