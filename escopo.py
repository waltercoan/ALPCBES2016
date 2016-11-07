__author__ = 'Walter'
#Escopo GLOBAL
x = 10
def minhaf():
    #Escopo LOCAL
    x = 5
def minhafGLOBAL():
    #Escopo GLOBAL
    global x
    x = 5

print(x)
minhaf()
minhafGLOBAL()
print(x)

