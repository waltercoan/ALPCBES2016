__author__ = 'Walter'
memoria = ['x','x',' ',' ',' ','x','x','x',' ',' ',' ','x']
try:
    i = 0
    while i < 12:
        print('i',i)
        if memoria[i] == ' ':
            print('achei buraco na posicao', i)
            j = i + 1

            while j < 12:
                if memoria[j] != ' ':
                    print('achei o fim do buraco', j)
                    tamanho = j - i
                    #verificar se a informacao cabe no
                    #tamanho de buraco que voce achou
                    #gravar as letrinhas no buraco for
                    print("aqui esta o break")
                    #raise Exception
                    i = j + 1
                    break
                j = j + 1
        i = i + 1
except Exception:
    #aqui eu deveria colocar o tratamento do erro
    pass