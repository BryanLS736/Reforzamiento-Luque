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
            nuevo_sueldo = self.sueldo + (0.2 * self.sueldo)
            print(f'El nuevo sueldo de la persona es: {nuevo_sueldo} soles')
        else:
            print('Su sueldo no se modifica por ser menor de edad.')


    def trabajando(self):
        print(f'La persona lleva trabajando {self.tiempo} meses en la empresa.')


class Prestamo(Persona):


    def __init__(self, nombre, edad, sueldo, tiempo):
        super().__init__(nombre, edad, sueldo, tiempo)


    def prestamo(self):
        if self.tiempo > 12 and self.edad > 25:
            print('Usted está apto(a) para un prestamo.')
        else:
            print('Usted no esta apto(a) para un prestamo.')


    def aprobacion(self):
        if self.tiempo > 12 and self.edad > 25:
            monto_prestamo = 10 * self.sueldo
            print(f'Usted recibirá {monto_prestamo} soles en préstamos.')
        else:
            print('No se pudo hacer el préstamo')


persona_1 = Prestamo('Bryan', 17, 1200, 3)
persona_1.datos()
persona_1.bonificacion()
persona_1.trabajando()
persona_1.prestamo()
persona_1.aprobacion()
print()
persona_2 = Prestamo('Alexander', 25, 1800, 14)
persona_2.datos()
persona_2.bonificacion()
persona_2.trabajando()
persona_2.prestamo()
persona_2.aprobacion()
print()
persona_3 = Prestamo('Pep', 38, 4500, 28)
persona_3.datos()
persona_3.bonificacion()
persona_3.trabajando()
persona_3.prestamo()
persona_3.aprobacion()