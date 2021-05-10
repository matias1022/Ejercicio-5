

class Alumno:
     __nombre=""
     __año=0
     __division=""
     __inasistencias=0

     max_inasistencias=15
     cantidad_clases=120

     def __init__ (self, nombre = "", año = 0, division = "", inasistencias = 0):     
        self.__nombre = nombre
        self.__año = año
        self.__division = division
        self.__inasistencias=inasistencias
     def __getAnio__(self):
          return self.__año
     def __getDiv__(self):
          return self.__division   
     def __getInsistencias__(self):
          return self.__inasistencias
     def __getNombre__(self):
          return self.__nombre 
     def __str__ (self):
          return f"Nombre:{self.__nombre},Año:{self.__año},Division:{self.__division},Inasistencias:{self.__inasistencias} "
     @classmethod
     def getMaxInasistencias(cls):
          return cls.max_inasistencias
     @classmethod
     def getCantidadClases(cls):
          return cls.cantidad_clases
      
     def listar(self,anio,divis):
           a= Alumno.getMaxInasistencias()
           if self.__año ==anio and self.__division==divis:
                     if self.__inasistencias>a:
                         b=Alumno.getCantidadclases()
                         porcentaje= a*b/100
                         print("Alumno     Porcentaje")
                         print(f"{self.__nombre},{porcentaje}% ")
