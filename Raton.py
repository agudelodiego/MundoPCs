"""
REALIZADO POR: Diego Agudelo
FECHA: Sep 26 2021


DESCRIPCION DEL ARCHIVO: El presente archivo esta dedicado al diseño de la clase Raton, la cual se encargara de llevar registro de la cantidad de ratones creados
"""



#Importacion de modulos
from DispositivoEntrada import DispositivoEntrada



#Creacion de clase
class Raton(DispositivoEntrada):

    #Variable de clase
    contadorRatones = 0

    #Constructor
    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        super().__init__(tipoEntrada, marca)
        self.__idRaton = Raton.contadorRatones

    
    #Metodo Get __idRaton
    @property
    def idRaton(self):
        return self.__idRaton


    #Metodo __str__
    def __str__(self):
        mensaje = f'RATON -> Id: {self.__idRaton}, Marca:{self.marca}, Tipo de entrada:{self.tipoEntrada}'
        return mensaje



#!ENTORNO DE PRUEBAS
if __name__ == '__main__':
    
    #Instanciamiento del objeto
    ejemplo1 = Raton('bluetooth','logitech')

    #Set tipoEntrada
    ejemplo1.tipoEntrada = 'USB'

    #Get tipoEntrada
    print(ejemplo1.tipoEntrada)

    #Set marca
    ejemplo1.marca = 'lenovo'

    #Get marca
    print(ejemplo1.marca)

    #Get idRaton
    print(ejemplo1.idRaton)

    #Llamado metodo __str__
    print(f'Metodo __str__: {ejemplo1}')