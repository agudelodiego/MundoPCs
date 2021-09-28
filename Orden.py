"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 27 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de la clase Orden, la cual se encargara de crear cada una de las ordenes que hagan los clientes de. En una misma orden se podran tener varias computadoras
"""


#Importamos los modulos
from DispositivoEntrada import DispositivoEntrada
from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
import json


#Creacion de clase Orden
class Orden:

    #Contador de ordenes
    contador = 0

    #Metodo constructor
    def __init__(self,computadoras):
        Orden.contador += 1

        #!IMPORTANTE: __computadoras se le debe de pasar una lista de objetos de tipo computadora previamente creados, de lo contrario ocasionara errores
        self.__computadoras = computadoras
        self.__idOrden = Orden.contador

    
    #Metodo agregar mas computadoras a la orden
    def agregar(self,nuevo):
        self.__computadoras.append(nuevo)

    
    #Get lista computadoras en la orden
    @property
    def computadoras(self):
        return self.__computadoras


    #Get idOrder
    @property
    def idOrden(self):
        return self.__idOrden

    
    #Metodo __str__
    def __str__(self):
        mensaje = f'''COMPUTADORAS EN LA ORDERN: {self.__computadoras}'''
        return mensaje


#!ENTORNO DE PRUEBAS
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
    putador2 = Computadora('Acer nitro 5',monitor2,raton1,teclado2)

    #Instanciamiento de objetos de tipo Orden
    orden1 = Orden([putador1])
    orden2 = Orden([putador1,putador2])

    #Agregar computadoras a una orden
    orden1.agregar(putador2)

    #Get computadoras
    print(orden1.computadoras)
