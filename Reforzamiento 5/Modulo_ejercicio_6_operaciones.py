def numeros_usuario():
    while True:
        try:
            var_1 = int(input('Ingresa el valor 1: '))
            var_2 = int(input('Ingresa el valor 2: '))
            var_3 = int(input('Ingresa el valor 3: '))
            return var_1, var_2, var_3

        except ValueError:
            print('No se puede ingresar valores string ni flotantes, vuelva a ingresar sus valores.')


def numeros_suma(x, y):
    return x + y