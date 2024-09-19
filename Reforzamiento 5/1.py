try:
    suma = 80 + 'Hola Pythonista'
    print(suma)
except TypeError:
    print('Hubo un error al querer sumar, esto debido a que no se puede '
            'sumar un dato de tipo entero (int) y un dato de tipo string (str).')