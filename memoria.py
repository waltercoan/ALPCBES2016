__author__ = 'Walter'
memoria = ['x','x',' ',' ',' ','x']
try:
    for i in range(6):
        if memoria[i] == ' ':
            print('achei buraco na posicao', i)
            for j in range(i+1,6):
                if memoria[j] != ' ':
                    print('achei o fim do buraco', j)
                    tamanho = j - i
                    #verificar se a informacao cabe no
                    #tamanho de buraco que voce achou
                    #gravar as letrinhas no buraco for
                    print("aqui esta o break")
                    raise Exception
                    i = j + 1
except Exception:
    #aqui eu deveria colocar o tratamento do erro
    pass