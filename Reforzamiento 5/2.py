def ejercicio_2():
    while True:
        try:
            orden = (int(input('Ingresa un numero entero para mostrar el valor en ese orden:\n')))-1
            lista = [2, 6, 10, 4, 5, 23, 1]
            print(lista[orden])
            break
        except IndexError:
            print('No se pudo escontrar este valor debido a que no hay ninguno '
                  'en esa posición solo existen valores del 1 al 7.')
        except ValueError:
            print('No es posible escribir un dato de tipo string (str) o flotante (float), '
                  'por favor, ingrese un dato de tipo entero')
ejercicio_2()