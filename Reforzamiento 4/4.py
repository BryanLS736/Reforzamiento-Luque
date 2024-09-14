class Alumno:


    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.edad = int(input('Ingrese su edad: '))
        self.nota_final = float(input('Ingrese su nota final: '))


    def datos_imprimir(self):
        print(f'Su nombre es: {self.nombre}, y tiene la edad de: {self.edad} años')


    def aprobar(self):
        print(f'La nota final es: {self.nota_final}')
        if 11 <= self.nota_final <= 20:
            print('Usted aprobó!')
        elif 0 <= self.nota_final < 11:
            print('Usted desaproboó!')
        else:
            print('Su nota final no fue validada, ingrese una nota real.')


alumno_1 = Alumno()
alumno_1.datos_imprimir()
alumno_1.aprobar()

alumno_2 = Alumno()
alumno_2.datos_imprimir()
alumno_2.aprobar()

alumno_3 = Alumno()
alumno_3.datos_imprimir()
alumno_3.aprobar()