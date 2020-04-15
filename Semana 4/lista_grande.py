# Lista grande
from random import randint

def lista_grande(n):
    lista = []
    for i in range(n):
        numero = randint(0,n)
        lista.append(numero)
    return lista
