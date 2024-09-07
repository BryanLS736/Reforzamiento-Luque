departamentos = ['Lima', 'Piura', 'Tumbes', 'Arequipa', 'Ancash']

print(departamentos)

dep_1 = str(input('Ingresa un departamento ya existente en la lista: '))

if dep_1 in departamentos:
    departamentos.remove(dep_1)
    dep_2 = str(input('Escribe el departamento que sustituirá al primero: '))
    departamentos.append(dep_2)
    print(departamentos)
else:
    print('El departamento escrito no existe en la lista.')