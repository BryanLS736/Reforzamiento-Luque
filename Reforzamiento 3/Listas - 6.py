lista = [False, True, 20.29, 5.09, 20.24, False]

print('El penultimo valor de la lista es {}'.format(lista[4]))
print('El ultimo valor de la lista es {}'.format(lista[5]))

tipos_datos = (type(lista[0]),
               type(lista[1]),
               type(lista[2]),
               type(lista[3]),
               type(lista[4]),
               type(lista[5]))

print('Los tipos de datos de los elementos de la lista es el siguiente: {}'.format(tipos_datos))