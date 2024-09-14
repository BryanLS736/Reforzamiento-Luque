class Persona:
    def __init__(self, nombre, edad, sueldo, tiempo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.tiempo = tiempo


    def datos(self):
        print(f'El nombre de la persona es: {self.nombre}, tiene {self.edad} años y su sueldo es de {self.sueldo} soles')
        if self.edad >= 18:
            print('La persona es mayor de edad.')
        else:
            print('La persona es menor de edad.')


    def bonificacion(self):
        if self.edad >= 18:
            self.sueldo = self.sueldo + (0.2 * self.sueldo)
            print(f'El nuevo sueldo de la persona es: {self.sueldo}')
        else:
            print('Su sueldo no se modifica por ser menor de edad.')


    def trabajando(self):
        print(f'La persona lleva trabajando {self.tiempo} meses en la empresa.')


persona_1 = Persona('Bryan', 17, 1200, 3)
persona_1.datos()
persona_1.bonificacion()
persona_1.trabajando()
print()
persona_2 = Persona('Alexander', 25, 1800, 14)
persona_2.datos()
persona_2.bonificacion()
persona_2.trabajando()
print()
persona_3 = Persona('Pep', 38, 4500, 28)
persona_3.datos()
persona_3.bonificacion()
persona_3.trabajando()