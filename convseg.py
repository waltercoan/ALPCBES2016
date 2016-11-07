__author__ = 'Walter'


def conv(pseg):
    print("Recebi: ", pseg, " segundos")
    horas = int(pseg / 3600)
    print("horas: ", horas)
    sobro = pseg - (horas * 3600)
    minut = int(sobro / 60)
    print("minutos", minut)
    seg = sobro - (minut * 60)
    print("segundos", seg)
    print("%d:%d:%d" %(horas,minut,seg))

conv(100000)