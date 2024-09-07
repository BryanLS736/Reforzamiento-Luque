lista = ['english I', 'matematicas', 'fundamentos de programacion',
         'matematicas discreta', 'matematicas', 'matematicas']

print('El curso "matematicas" se repite {}'.format(lista.count('matematicas')))

del lista[0]
print(lista)