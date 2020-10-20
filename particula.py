# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from random import randint
from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, x_1,y_1,x_2,y_2):
        self.__id = randint(0,100000)+randint(0,10000)+randint(0,1000)+randint(0,100)+randint(0,10)
        self.__origen_x = x_1
        self.__origen_y = y_1
        self.__destino_x = x_2
        self.__destino_y = y_2
        self.__velocidad = 5
        self.__red = 100
        self.__green = 55
        self.__blue = 215
        self.__distancia = distancia_euclidiana(x_1,y_1,x_2,y_2)

    def __str__(self):
        return (
            'ID: '+str(self.__id)+'\n'
            'Origen en x: '+str(self.__origen_x)+'\n'
            'Origen en y: '+str(self.__origen_y)+'\n'
            'Destino en x: '+str(self.__destino_x)+'\n'
            'Destino en y: '+str(self.__destino_y)+'\n'
            'Velocidad: '+str(self.__velocidad)+'\n'
            'Red: '+str(self.__red)+'\n'
            'Green: '+str(self.__green)+'\n'
            'Blue: '+str(self.__blue)+'\n'
            'Distancia: '+str(self.__distancia)+'\n'
        )
