class Agenda:

    def __init__(self):
        self.lista_nombre = []
        self.lista_telefono = []
        self.lista_email = []
        self.lista_dni = []
        self.dicc_datos = {'nombres': self.lista_nombre,
                           'telefono': self.lista_telefono,
                           'email': self.lista_email,
                           'dni': self.lista_dni}


    def agregar_contacto(self, nombre, telefono, email, dni):
        self.lista_nombre.append(nombre)
        self.lista_telefono.append(telefono)
        self.lista_email.append(email)
        self.lista_dni.append(dni)


    def mostrar_contactos(self):
        print('la lista de contactos es la siguiente: ')
        for i in range(len(self.lista_nombre)):
            print(f'Nombre: {self.lista_nombre[i]}, '
                  f'telefono: {self.lista_telefono[i]}, '
                  f'email: {self.lista_email[i]}, '
                  f'dni: {self.lista_dni[i]}')


    def buscar_contacto(self, dni):
        if dni in self.lista_dni:
            print(f'La persona con DNI: {dni} existe en la agenda.')
            posicion = (len(self.lista_dni))
            for i in range(posicion):
                if self.lista_dni[i] == dni:
                    print(f'La persona con el DNI: {dni}, tiene los siguientes datos:'
                          f'nombre: {self.lista_nombre[i]}, '
                          f'telefono: {self.lista_telefono[i]}, '
                          f'email: {self.lista_email[i]}, ')

        else:
            print(f'La persona con el DNI: {dni}, no existe en la agenda.')


persona = Agenda()
persona.agregar_contacto('Bryan', 954786592, 'bryan@gmail.com', 71236589)
persona.agregar_contacto('Alexander', 963252361, 'alexander@gmail.com', 74878212)
persona.agregar_contacto('Pedro', 996892141, 'pedro@gmail.com', 77485113)
persona.agregar_contacto('Felipe', 911423655, 'felipe@gmail.com', 77788542)
persona.mostrar_contactos()
persona.buscar_contacto(74878212)
