def ejercicio_3():
    while True:
        try:
            persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
            llave = (input('Ingresa la llave que desee buscar en el diccionario:\n')).lower()
            print(f'El value para la key "{llave}" es {persona[llave]}')
            break
        except KeyError:
            print('Esa llave no existe, porfavor ingrese una llave '
                  'correcta ("nombre", "apellido" o "dni")')

ejercicio_3()