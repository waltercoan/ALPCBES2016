contador = 5
soma = 0
while contador >= 0:
    print(contador)
    #acumulador
    if contador % 2 == 1:
        soma = soma + contador
    #contador
    contador = contador - 1
    #aqui1
print("Cai fora...")
print("A soma total e: ", soma)
