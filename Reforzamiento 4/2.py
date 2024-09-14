class Circulo:


    def __init__(self, radio):
        self.radio=radio


    def area(self):
        area = 3.1416*(self.radio**2)
        print(f'El area del circulo es: {area}')


circulo_1 = Circulo(4)
circulo_1.area()

circulo_2 = Circulo(2)
circulo_2.area()