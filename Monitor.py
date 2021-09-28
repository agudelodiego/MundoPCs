"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 27 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de la clase Monitor, la cual se encargara de crear onjetos de tipo monitor y llevar un conteo de todos los objeto que se han instanciado de esta clase. Algo importante que mensionar es esta clase no hereda de ninguna otra
"""


#Creacion de clase
class Monitor:

    #Contador
    contador = 0

    #Metodo constructor
    def __init__(self,marca,tamaño):
        Monitor.contador += 1
        self.__marca = marca
        self.__tamaño = tamaño
        self.__idMonitor = Monitor.contador


    #Get y Set marca
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,nuevo):
        self.__marca = nuevo


    #Get y Set tamaño
    @property
    def tamaño(self):
        return self.__tamaño

    @tamaño.setter
    def tamaño(self,nuevo):
        self.__tamaño = nuevo


    #Get idMonitor
    @property
    def idMonitor(self):
        return self.__idMonitor


    #Metodo __str__
    def __str__(self):
        mensaje = f'MONITOR -> Id:{self.__idMonitor}, Marca:{self.__marca}, Tamaño:{self.__tamaño}'
        return mensaje


#!ENTORNO DE PRUEBAS
if __name__ == '__main__':
    
    #Instanciamiento de clase
    ejemplo1 = Monitor('acer','25 Pulgadas')

    #Set marca
    ejemplo1.marca = 'yo lo hice'

    #Get marca
    print(ejemplo1.marca)

    #Set tamaño
    ejemplo1.tamaño = 'ni puta idea'

    #Get tamaño
    print(ejemplo1.tamaño)

    #Get idMonitor
    print(ejemplo1.idMonitor)

    #Metodo __srt__
    print('Metodo __srt__:',ejemplo1)
