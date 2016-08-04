__author__ = 'Walter'

maiornumacid = 0
cidademaiornumero=0
menornumacid = 0
cidademenornumero=0
somacarros=0
somaacidentes=0
contacidadesacid=0

for contacidade in range(0,5):
    print("Cidade: ", contacidade+1)
    print("Digite o codigo da cidade")
    codigo = int(input())
    print("Digite o num de veiculos")
    numveic = int(input())
    print("Digite o numero de acidentes")
    numacid = int(input())
    #aqui ohhhh

    #compara cada valor com uma variavel com o maior de todos
    if numacid > maiornumacid:
        maiornumacid = numacid
        #guarda o codigo cidade toda vez que acha um maior
        cidademaiornumero = codigo

    #a logica do menor não tem NADA haver com a do maior
    if contacidade == 0:
        menornumacid = numacid
        cidademenornumero = codigo
    else:
        if numacid < menornumacid:
            menornumacid = numacid
            cidademenornumero = codigo
    #acumulador
    somacarros = somacarros + numveic

    if numveic < 2000:
        somaacidentes = somaacidentes + numacid
        contacidadesacid = contacidadesacid + 1

#poe o print aqui???
print("A cidade ", cidademaiornumero,
      "tem a maior qtd de acidentes com: ", maiornumacid)
print("A cidade ", cidademenornumero,
      "tem a menor qtd de acidentes com: ", menornumacid)
media = somacarros / 5
print("A media de carro das cinco cidades e ", media)

mediaacid = somaacidentes / contacidadesacid
print("A media de acidentes nas cidades com menos de 2mil carros e",
      mediaacid)