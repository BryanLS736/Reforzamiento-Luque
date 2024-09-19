from datetime import date
def ejercicio_4():
    while True:
        try:
            fecha_actual = date.today()
            dia = fecha_actual.day
            mes = fecha_actual.month
            years = fecha_actual.year
            nombre = input('Escribe tu nombre: ')
            string = f'Hello {nombre}, hoy estamos {dia} de {mes} del {years}'
            print(string/0)
        except ZeroDivisionError:
            print('No puedes dividir un numero entre 0, ingresa cualquier numero excepto el 0')
        except ValueError:
            print('No puedes hacer una division de un tipo string, ingresa un ')
        except TypeError:
            print('No puedes hacer una division de un tipo string, se debe de '
                  'ingresar un tipo flotante (float) o un tipo entero (int).')

ejercicio_4()