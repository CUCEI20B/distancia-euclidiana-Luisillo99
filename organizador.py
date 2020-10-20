# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from particula import Particula

class Organizador:
    def __init__(self):
        self.org = []

    def agregar_inicio(self,part):
        self.org.insert(0,part)

    def agregar_final(self,part):
        self.org.append(part)

    def mostrar(self):
        for i in self.org:
            print(i)

particula_1 = Particula(10,100,20,200)
particula_2 = Particula(100,300,200,400)
particula_3 = Particula(50,100,20,300)
organizador_1 = Organizador()
organizador_1.agregar_inicio(particula_1)
organizador_1.agregar_final(particula_2)
organizador_1.agregar_final(particula_3)
organizador_1.mostrar()
