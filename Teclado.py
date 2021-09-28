"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 27 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de la Teclado, la cual estara encargada de crear objetos de tipo Teclado que heredaran metodos y propiedades de la clase Dispositivo entrada
"""


#Importar modulos 
from DispositivoEntrada import DispositivoEntrada


#Creacion de la clase Teclado
class Teclado(DispositivoEntrada):

    #Variable de clase contador
    contador = 0

    #Metodo constructor
    def __init__(self, tipoEntrada, marca):
        Teclado.contador += 1
        super().__init__(tipoEntrada, marca)
        self.__idTeclado = Teclado.contador

    
    #Metodo Get __idTeclado
    @property
    def idTeclado(self):
        return self.__idTeclado


    #Metodo __str__
    def __str__(self):
        mensaje = f'TECLAD -> Id:{self.__idTeclado}, Marca:{self.marca}, Tipo entrada:{self.tipoEntrada}'
        return mensaje


#!ENTRONO DE PRUEBAS
if __name__ == '__main__':
    
    #Instanciamiento de clase 
    ejemplo1 = Teclado('USB','acer')

    #Set tipoEntrada
    ejemplo1.tipoEntrada = 'bluetooth'

    #Get tipoEntrada
    print(ejemplo1.tipoEntrada)

    #Set marca
    ejemplo1.marca = 'azus'

    #Get marca
    print(ejemplo1.marca)

    #Get idTeclado
    print(ejemplo1.idTeclado)

    #Llamada a metodo __str__
    print('Metodo __str__:',ejemplo1)
