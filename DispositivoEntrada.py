"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 26 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de una clase DispositivoEntrada, el cual se encargara de crear objetos de tipo dispositivo de entrada, entre los cuales podremos tener Raton y Teclado, puesto que son los tipos perifericos de entrada que solemos tener en un computador
"""



#Creacion de clase
class DispositivoEntrada:

    #Constructor
    def __init__(self,tipoEntrada,marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca


    #Get y Set _tipoEntrada
    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self,nuevo):
        self._tipoEntrada = nuevo

    
    #Get y Set _marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,nuevo):
        self._marca = nuevo



#!ENTORNO DE PRUEBAS
if __name__ == '__main__':
    
    #Instaciamiento
    ejemplo1 = DispositivoEntrada('usb','logi tech')

    #Set tipoEntrada
    ejemplo1.tipoEntrada = 'bluetooth'

    #Get tipoEntrada
    print(ejemplo1.tipoEntrada)

    #Set marca
    ejemplo1.marca = 'hp'

    #Get marca
    print(ejemplo1.marca)