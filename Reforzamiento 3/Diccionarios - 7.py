numero_uno = float(input('Ingresa un primer número: '))
numero_dos = float(input('Ingresa un segundo número: '))
numero_tres = float(input('Ingresa un tercer número: '))
numero_cuatro = float(input('Ingresa un cuarto número: '))

cubo_uno = numero_uno**3
cubo_dos = numero_dos**3
cubo_tres = numero_tres**3
cubo_cuatro= numero_cuatro**3

diccionario = {numero_uno: cubo_uno, numero_dos: cubo_dos, numero_tres: cubo_tres, numero_cuatro: cubo_cuatro}

print('El diccionario pedido es el siguiente: {}'.format(diccionario))