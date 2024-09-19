def funcion_decoradora(funcion_entrada):


    def funcion(*args,**kwargs):
        print("La cantidad de argumentos que tiene la función es")
        funcion_entrada(*args,**kwargs)
        print(len(args) + len(kwargs))
        print("La función decoradora terminó de ejecutarse.")
    return funcion


@funcion_decoradora
def numero_argumentos(*args, **kwargs):
    return numero_argumentos


numero_argumentos(13, 12, 20, 7, 14, 7, 20, 22)