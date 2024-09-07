lista = ['matematicas', 'english I', 'fundamentos de programacion',
         'matematicas discreta', 'lenguaje y comunicacion I', 'calculo de una variable']

lista.append('english II')
lista.append('programacion y estructura de datos')
lista.append('teoria de computacion')
lista.append('programacion orientada a objetos')

lista.remove('english I')
lista.remove('lenguaje y comunicacion I')

print('La lista actualizada es: {}'.format(lista))
print('La cantidad total de items de nuestra lista es: {}'.format(len(lista)))