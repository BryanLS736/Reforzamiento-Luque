nombre1 = input('Ingresa el nombre de la primera persona: ')
numero1 = int(input('Ingresa el numero de la primera persona: '))

nombre2 = input('Ingresa el nombre de la segunda persona: ')
numero2 = int(input('Ingresa el numero de la segunda persona: '))

nombre3 = input('Ingresa el nombre de la tercera persona: ')
numero3 = int(input('Ingresa el numero de la tercera persona: '))

nombre4 = input('Ingresa el nombre de la cuarta persona: ')
numero4 = int(input('Ingresa el numero de la cuarta persona: '))

nombre5 = input('Ingresa el nombre de la quinta persona: ')
numero5 = int(input('Ingresa el numero de la quinta persona: '))


agenda = {nombre1: numero1, nombre2: numero2, nombre3: numero3, nombre4: numero4, nombre5: numero5}

nombre_buscar = input('Ingresa el nombre: ')

if nombre_buscar in agenda:
    print('El numero de la persona es: {}'.format(agenda[nombre_buscar]))

else:
    print('No se encuentra registrado.')