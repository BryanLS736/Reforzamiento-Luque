diccionario = {'nombre' : 'Bryan', 'edad': 18, 'salario': 250}

diccionario['DNI'] = '7654321'

print(diccionario['salario'])

del diccionario['edad']

print('El diccionario actualizado es: {}'.format(diccionario))