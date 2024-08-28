"""Almacenamos numero positivos y negativos en 3 variables"""

variable_uno = -154
variable_dos = 72
variable_tres = 207

"""Hallamos los modulos de cada variable con 3, 5, 7 respectivamente"""

mod_uno = variable_uno % 3
mod_dos = variable_dos % 5
mod_tres = variable_tres % 7

"""Hallamos la suma de los modulos"""

suma_modulos = mod_uno + mod_dos + mod_tres

"""Imprimimos nuestra suma de los módulos"""

print('La suma de los módulos es: {}'.format(suma_modulos))