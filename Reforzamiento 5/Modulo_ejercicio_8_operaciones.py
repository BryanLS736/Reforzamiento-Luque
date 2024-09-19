from math import sqrt


def numero_entero():

    while True:

        try:
            numero = int(input('Ingrese un número entero: '))
            return numero

        except ValueError:
            print('Error, no puedes ingresar valores tipo flotante o string, solo escribe numeros enteros.')


def raiz_cuadrada(numero):

    if numero < 0:
        print('No es posible hacer la raiz cuadrada de un número negativo.')
        return None

    else:
        raiz = sqrt(numero)
        return raiz


def numero_elevado(numero):

    cuadrado = numero ** 2
    cubo = numero ** 3
    diccionario = {f'{numero}^2': cuadrado, f'{numero}^3': cubo}

    return diccionario