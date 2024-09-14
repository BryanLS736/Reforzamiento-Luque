class Persona:
    def __init__(self):
        self.nombre = input('Escriba su nombre: ')
        self.edad = int(input('Escriba su edad: '))
        print(f'Su nombre es {self.nombre}')


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input('Escriba su sueldo: '))


    def impuestos(self):
        print(f'Su sueldo es de {self.sueldo} soles.')

        if self.sueldo > 4000:
            impuesto = 0.1 * self.sueldo
            print('Usted debe pagar impuestos.')
            print(f'El impuesto a pagar es de {impuesto} soles.')
        else:
            print('Usted no debe pagar impuestos.')


empleado_1 = Empleado()
empleado_1.impuestos()

