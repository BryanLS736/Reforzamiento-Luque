from datetime import datetime


def funcion_decoradora(funcion_entrada):
    def funcion():
        hora_hoy = datetime.now()
        hora = hora_hoy.hour
        minutos = hora_hoy.minute
        nombre_usuario = funcion_entrada()
        print(f'Buenos días {nombre_usuario}, son las {hora} con {minutos} minutos.')
        print('Hasta luego que tenga un buen día.')
    return funcion

@funcion_decoradora
def persona():
    nombre = input('Ingrese su nombre: ')
    return nombre

persona()