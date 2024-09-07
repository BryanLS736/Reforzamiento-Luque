lista = ['SQL server', 'MySQL', 'Azure SQL Database', 'PostgreSQL', 'MariaDB']

BD = input('Ingresa el nombre de una BD con toda y las mayusculas, segun corresponda a dicha BD: ')

if BD in lista:
    lista.remove(BD)
else:
    print('El elemento escrito no existe en la lista.')
    lista.append(BD)

print('La lista actualizada es: {}'.format(lista))