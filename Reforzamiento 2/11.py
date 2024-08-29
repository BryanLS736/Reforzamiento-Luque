"""Identificamos nuestra variable"""

numero = 3
exponente = 5
division = 10
modulo = 3

"""Realizamos la operación"""

operacion = pow(numero, exponente)/10
resultado_modulo = operacion % modulo

"""imprimimos el resultado de su modulo con 3"""

print('El resultado final es: {}'.format(resultado_modulo))