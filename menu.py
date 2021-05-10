import os
from claseAlumno import Alumno
from ManejadorAlumno import ControlAlumno

class Menus:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self,listaAlu):
          os.system('cls')
          salir = False

          while salir == False:
              print('1-\tLista Alumnos con mas inasistencias de las permitidas')
              print('2-\tModificar la cantidad máxima de inasistencias permitidas')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1: 
                    listaAlu.listar(6,"A")
              elif self.__op == 2: 
                    maxi=int(input("Ingresar la cantidad de insistencias maximas permitidas:"))
                    Alumno.max_inasistencias=maxi
              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')  