"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 27 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de la clase Computadora, la cual se encargara de crear objetos de tipo computadoras, y ademas de ello tendra como atributos instacias de otros objetos, puesto que una computadora esta compuesta por algunos perifericos como por ejemplo un teclado(el cual debera ser previamente instanciado)
"""


#Importar modulos
from DispositivoEntrada import DispositivoEntrada
from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor


#Creacion de la clase 
class Computadora:

    #Contador
    contador = 0

    #Metodo constructor
    def __init__(self,nombre,monitor,raton,teclado):
        Computadora.contador += 1
        self.__nombre = nombre
        self.__monitor = monitor
        self.__raton = raton
        self.__teclado = teclado
        self.__idComputadora = Computadora.contador

    
    #Get y Set nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre = nuevo


    #Get y Set monitor
    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self,nuevo):
        self.__monitor = nuevo


    #Get y Set raton
    @property
    def raton(self):
        return self.__raton

    @raton.setter
    def raton(self,nuevo):
        self.__raton=nuevo

    
    #Get y Set teclado
    @property
    def teclado(self):
        return self.__teclado

    @teclado.setter
    def teclado(self,nuevo):
        self.__teclado = nuevo

    
    #Get idComputadora
    @property
    def idComputadora(self):
        return self.__idComputadora


    #Metodo __str__
    def __str__(self):
        mensaje = f'''
        ***********************COMPUTADORA************************
        NOMBRE --> {self.__nombre}
        MONITOR --> {self.__monitor}
        RATON --> {self.__raton}
        TECLADO --> {self.__teclado}
        ID_PC --> {self.__idComputadora}
        ************************************************************
        '''
        return mensaje


#!ENTRONO DE PRUEBAS
if __name__ == '__main__':

    #Instanciamiento de objetos de tipo Monitor
    monitor1 = Monitor('Hp','20 Pulgadas')
    monitor2 = Monitor('LG','19 Pulgadas')
    
    #Instaciamiento de objetos de tipo Raton 
    raton1 = Raton('bluetooth','Logitech')
    raton2 = Raton('USB','Acer')

    #Instanciamiento de objetos de tipo Teclado
    teclado1 = Teclado('USB','Logitech')
    teclado2 = Teclado('USB','Del')

    #Instanciamiento de objetos de tipo Computadora
    putador1 = Computadora('Lenovo legion v1',monitor1,raton1,teclado1)

    #Get nombre
    print(putador1.nombre)


    #Get monitor
    print(putador1.monitor)

    #Set monitor
    putador1.monitor = monitor2

    #Get raton
    print(putador1.raton)

    #Set raton
    putador1.raton = raton2

    #Get teclado
    print(putador1.teclado)

    #Set teclado
    putador1.teclado = teclado2

    #Get idComputadora
    print(putador1.idComputadora)

    #Metodo __srt__
    print(putador1)