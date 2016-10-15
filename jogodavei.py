__author__ = 'Walter'
print("..:Jogo da Vei:..")
velha = [[" "] * 3 for i in range(3)]
jogador = 0
while True:
    print("\n-------------")
    for lin in range(3):
        for col in range(3):
            print("|",velha[lin][col],end=" ")
        print("|\n-------------")
    lin = int(input("Digite a linha:")) - 1
    col = int(input("Digite a coluna:")) - 1
    if jogador == 0:
        velha[lin][col] = "X"
        jogador = 1
    else:
        velha[lin][col] = "O"
        jogador = 0
