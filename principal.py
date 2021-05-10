import os
from claseAlumno import Alumno
from ManejadorAlumno import ControlAlumno
from menu import Menus


if __name__ == '__main__':
     lista=ControlAlumno()
     lista.crear_Instancias()
     print(lista)
     ObjetoMenu = Menus()
     ObjetoMenu.Ejecutar(lista)  
     print ("La nueva cantidad maxima de inasistencias es:")
     print(Alumno.getMaxInasistencias())