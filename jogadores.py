__author__ = 'Walter'
contnovinho=0
somaidade = 0
somaalturas=0
gordinhos = 0
for time in range(0,5):
    print("Time: ", time + 1)
    for jogador in range(0,11):
        print("Jogador: ", jogador + 1)
        print("Digite a idade")
        idade = int(input())
        print("Digite o peso")
        peso = float(input())
        print("Digite a altura")
        altura = float(input())
        if peso > 80:
            gordinhos = gordinhos + 1
        if idade < 18:
            contnovinho = contnovinho + 1
        somaidade = somaidade + idade
        somaalturas = somaalturas + altura
    mediaidade = somaidade / 11
    somaidade = 0
    print("A media de idade do time e: ", mediaidade)
print("O num total de jog com menos de 18 anos e:", \
      contnovinho)
mediaaltura = somaalturas /55
print("A media das alturas e: ", mediaaltura)

pg = (gordinhos * 100) / 55
print("O perc de gordinhos e: ", pg)
