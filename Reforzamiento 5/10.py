def funcion_decoradora(funcion_entrada):


    def funcion(*args,**kwargs):

        print('Está por ejecturarse la función.')
        resultado = funcion_entrada(*args,**kwargs)
        print(f'La multiplicacion de los 6 argumentos es: {resultado}')
        print('La funcion ha sido ejercutada correctamente.')
        return resultado
    return funcion


@funcion_decoradora
def datos(var_1, var_2, var_3, **kwargs):

    multi = 1

    for i in kwargs:
        var = kwargs[i]
        multi *= var

    multiplicacion_final = var_1 * var_2 * var_3 * multi

    return multiplicacion_final

datos(2,3,4, var_4 = 5, var_5 = 6, var_6 = 7)