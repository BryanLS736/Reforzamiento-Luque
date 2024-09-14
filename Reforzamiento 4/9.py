class Figura:
    def __init__(self, nombre):
        self.nombre = nombre


    def area_rectangulo(self, base, altura):
        area = base * altura
        return f'El área del rectangulo es: {area :.2f}'


    def perimetro_rectangulo(self, base, altura):
        perimetro = (2 * base) + (2 * altura)
        return f'El perimetro del rectangulo es: {perimetro:.2f}'


    def area_circulo(self, radio):
        area = 3.1416 * (radio ** 2)
        return f'El area del circulo es: {area:.2f}'


    def perimetro_circulo(self, radio):
        perimetro = 3.1416 * radio * 2
        return f'El perimetro del circulo es: {perimetro:.2f}'

    
figura_1 = Figura('Figura 1')
print(figura_1.area_rectangulo(5, 6))
print(figura_1.perimetro_rectangulo(5, 6))
print(figura_1.area_circulo(5))
print(figura_1.perimetro_circulo(5))

figura_2 = Figura('Figura 2')
print(figura_2.area_rectangulo(2.44, 3.56))
print(figura_2.perimetro_rectangulo(2.44, 3.56))
print(figura_2.area_circulo(4.55))
print(figura_2.perimetro_circulo(4.55))