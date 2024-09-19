import random


def generador_numeros():
    lista_numeros = []
    for i in range(30):
        numeros_aleatorios = random.randint(0,100)
        lista_numeros.append(numeros_aleatorios)
    return lista_numeros


def orden_valores(i):
    i.sort()
    return i


def valor_maximo(j):
    valor_max = j[29]
    return valor_max