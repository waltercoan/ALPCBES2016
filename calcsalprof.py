__author__ = 'Walter'
'''Construir um programa que efetue o cálculo do
salário líquido de um professor. Para fazer este
programa, você deverá possuir alguns dados, tais
como: valor da hora aula, número de horas trabalhadas
no mês e percentual de desconto do INSS. Em primeiro
lugar, deve-se estabelecer qual será o seu salário
bruto para efetuar o desconto e ter o valor do salário
líquido.'''
print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trabalhadas")
numhoras = float(input())
print("Digite o percentual de desconto do INSS")
percdesc = float(input())
salbruto = valhora * numhoras
print("O valor do salario bruto e: ", salbruto)
valdesc = (salbruto * percdesc) / 100
salliq = salbruto - valdesc
print("O valor do salario liquido e: ", salliq)
