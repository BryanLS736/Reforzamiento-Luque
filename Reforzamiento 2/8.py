"""Escribimos 2 variables, una lista que estará vacia y la otra no"""

lista_vacia = []
lista_no_vacia = [1, 3, 7, 10]

"""Realizamos una condicional que nos dirá si la lista esta vacia o no"""

"""Condicional para la variable lista_vacia usando 'len'"""

if len(lista_vacia) == 0:
    print('Tu lista esta vacia')
else:
    print('Tu lista no esta vacia')

"""Condicional para la variable lista_no_vacia, usando 'not'"""

if not lista_no_vacia:
    print('Tu lista esta vacia')
else:
    print('Tu lista no esta vacia')