class Circulo:
    def __init__(self):
        self.radio = float(input('Escriba su radio: '))


    def area(self):
        area = 3.1416*(self.radio**2)
        print(f'El area del circulo es: {area}')


    def perimetro(self):
        perimetro = 2 * 3.1416 * self.radio
        print(f'El perimetro del circulo es: {perimetro}')



circulo_1 = Circulo()
circulo_1.area()
circulo_1.perimetro()

circulo_2 = Circulo()
circulo_2.area()
circulo_2.perimetro()

circulo_3 = Circulo()
circulo_3.area()
circulo_3.perimetro()