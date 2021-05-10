import csv, os
from claseAlumno import Alumno


class ControlAlumno:
    __listaAlumno=[]
    def __init__(self):
        self.__listaAlumno = []
    def agregarAlumno(self,alumno):
        self.__listaAlumno.append(alumno)

    def crear_Instancias(self):
        archivo = open("Alumnos_Escuel.csv" ,'r')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            nombre = fila[0]
            año = int(fila[1])
            division = fila[2]
            inasistencias = int(fila[3])
            otroAlumno = Alumno(nombre,año,division,inasistencias)
            self.agregarAlumno(otroAlumno)
        archivo.close()
 
    def __str__(self): 
             return f'{self.__listaAlumno[0]},\n{self.__listaAlumno[1]},\n{self.__listaAlumno[2]},\n{self.__listaAlumno[3]},\n{self.__listaAlumno[4]}'+'\n'
    def listar(self,anio,divis):
          a= Alumno.getMaxInasistencias()
          b= Alumno.getCantidadClases() 
          for otroAlumno in self.__listaAlumno:   
              if anio == otroAlumno.__getAnio__():
                 if divis==otroAlumno.__getDiv__():
                     
                     if otroAlumno.__getInsistencias__()>a:
                       d=otroAlumno.__getNombre__()
                       porcentaje= otroAlumno.__getInsistencias__()*b/100
                       print("Alumno     Porcentaje:")
                       print(f"{d}------{porcentaje}%:" )
          
                         
   
    
