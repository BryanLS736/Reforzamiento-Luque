class Alumno:


    def __init__(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.apellido = input("Ingrese el apellido del alumno: ")
        self.edad = int(input('Ingrese el edad del alumno: '))


    def resultado(self):
        datos = {'nombre': self.nombre, 'apellido': self.apellido, 'edad': self.edad}
        print(datos)

alumno_1 = Alumno()
alumno_1.resultado()