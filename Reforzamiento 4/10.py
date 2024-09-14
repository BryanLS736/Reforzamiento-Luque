class Soldado:


    def __init__(self, nombre):
        self.nombre = nombre
        self.pasos_historial = []
        self.posicion_x = 0
        self.posicion_y = 0


    def caminar_eje_x(self, pasos_x):
        if pasos_x < 0 and self.posicion_x + pasos_x < 0:
            print(f'El soldado {self.nombre} intentó moverse {pasos_x}, pero no se puede mover más alla de 0 '
                      f'en el eje x, los pasos no serán validados.')

        else:
            self.posicion_x += pasos_x
            self.pasos_historial.append((pasos_x, 'x'))
            print(f'El soldado {self.nombre} caminó'
                  f' {pasos_x} pasos en el eje x')
            print(f'Posición actual: X = {self.posicion_x}, Y = {self.posicion_y}')


    def caminar_eje_y(self, pasos_y):
        if pasos_y < 0 and self.posicion_y + pasos_y < 0:
            print(f'El soldado {self.nombre} intentó moverse {pasos_y}, pero no se puede mover más alla de 0 '
                  f'en el eje y, los pasos no serán validados.')

        else:
            self.posicion_y += pasos_y
            self.pasos_historial.append((pasos_y, 'y'))
            print(f'El soldado {self.nombre} caminó {pasos_y} pasos en el eje y')
            print(f'Posición actual: X = {self.posicion_x}, Y = {self.posicion_y}')


    def historial(self):
       print(f'El historial de pasos con sus respectivas direcciones son las siguientes: {self.pasos_historial}')



personaje = Soldado('Bryan')
personaje.caminar_eje_x(5)
personaje.caminar_eje_y(4)
personaje.caminar_eje_y(8)
personaje.caminar_eje_x(1)
personaje.historial()
personaje.caminar_eje_x(-6)
personaje.caminar_eje_y(-13)
personaje.historial()